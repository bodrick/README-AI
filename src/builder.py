"""Builds the README Markdown file for your codebase."""

import subprocess
import tempfile
from pathlib import Path

import git
import pandas as pd

from conf import AppConfig, ConfigHelper
from factory import FileHandler
from logger import Logger

LOGGER = Logger("readmeai_logger")


def build(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    dependency_list: list,
    summaries: tuple,
) -> None:
    """Builds the README Markdown file for your codebase.

    Parameters
    ----------
    conf
        Configuration data class containing Markdown template strings.
    conf_helper
        Helper data class containing metadata to populate the README.
    dependency_list
        List of project dependencies extracted from the user's repository.
    summaries
        Tuple of code summaries generated for each file in the repository.
    """

    md_file = conf.md.head
    md_close = conf.md.close
    md_intro = conf.md.intro
    md_dropdown = conf.md.dropdown
    md_modules = conf.md.modules
    md_setup = conf.md.setup
    md_slogan = conf.md.slogan
    md_toc = conf.md.toc
    md_tree = conf.md.tree

    cwd_path = Path.cwd()
    handler = FileHandler()
    json_path = cwd_path / conf.paths.badges
    json_dict = handler.read(json_path)

    summaries = pd.DataFrame(summaries, columns=["Module", "Summary"])
    summaries = parse_pandas_cols(summaries)

    md_badges = get_badges(json_dict, dependency_list)
    md_tables = create_tables(summaries, md_dropdown)
    md_repo = create_directory_tree(conf.git.repository)
    md_setup = create_setup_guide(conf, conf_helper, summaries)

    # Store intermediate results and perform a single write operation
    md_file_parts = []
    md_file_parts.append(md_file.format(conf.git.name, md_slogan, md_badges))
    md_file_parts.append(md_toc)
    md_file_parts.append(md_intro)
    md_file_parts.append(md_tree)
    md_file_parts.append(md_repo)
    md_file_parts.append(md_modules)
    md_file_parts.append(md_tables)
    md_file_parts.append(md_setup)
    md_file_parts.append(md_close)
    md_file = "\n".join(md_file_parts)

    md_path = cwd_path / conf.paths.readme
    handler.write(md_path, md_file)

    LOGGER.info(f"README.md file created at: {md_path}")


def get_badges(badge_metadata: dict, dependency_list: list) -> str:
    """
    Generates badge icons for each dependency in the project.

    Parameters
    ----------
    badge_metadata : dict
        Dictionary containing available icons and their src.
    dependency_list : list
        List of project dependencies.

    Returns
    -------
    str
        Formatted string containing badge icons for dependencies.
    """
    badges = []
    icons_dict = {
        icon["name"].lower(): icon["src"] for icon in badge_metadata["icons"]
    }
    for dependency in dependency_list:
        dependency = dependency.lower()
        if dependency in icons_dict:
            badges.append(icons_dict[dependency])
    return format_badges(badges, dependency_list)


def format_badges(badges: list, dependencies: list) -> str:
    """
    Formats the badges into a string with a maximum of 8 badges per line.

    Parameters
    ----------
    badges : list
        List of badge icons.
    dependencies : list
        List of project dependencies.

    Returns
    -------
    str
        Formatted string with badge icons arranged.
    """
    badge_lines = []
    total_badges = len(badges)
    if total_badges < 8:
        badges_per_line = total_badges
    else:
        badges_per_line = total_badges // 2 + (total_badges % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, total_badges, badges_per_line):
        line = "\n".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}" />'
                for dep, badge in zip(
                    dependencies[i : i + badges_per_line],
                    badges[i : i + badges_per_line],
                )
            ]
        )
        badge_lines.append(line)

    return "\n\n".join([f"{line}" for line in badge_lines])


def create_setup_guide(
    conf: AppConfig, conf_helper: ConfigHelper, summaries: pd.DataFrame
):
    """
    Creates a setup guide for the project based on the top used language.

    Parameters
    ----------
    conf : object
        Configuration object containing GitHub and markdown configurations.
    conf_helper : object
        Configuration helper object containing file extensions and setup guide.
    summaries : pd.DataFrame
        DataFrame containing parsed information from project files.

    Returns
    -------
    str
        Formatted string with setup guide.
    """
    install_guide = "[INSERT_INSTALLATION_STEPS_HERE]"
    run_guide = "[INSERT-RUN_INSTRUCTIONS_HERE]"
    ignore_files = conf_helper.ignore_files
    name = conf.git.name
    source = conf.git.repository

    summaries["Language"] = summaries["Module"].apply(
        lambda x: Path(x).suffix[1:]
        if Path(x).suffix[1:] not in ignore_files
        else None
    )

    try:
        top_language = summaries["Language"].value_counts().idxmax()
        language_name = conf_helper.language_names[top_language]
        language_setup = conf_helper.language_setup[language_name]

        LOGGER.info(f"Top project language: {top_language}")
        LOGGER.info(f"{language_name} setup guide: {language_setup}")

        if language_setup:
            install_guide = language_setup[0]
            run_guide = language_setup[1]

    except KeyError as ke:
        LOGGER.warning(f"KeyError: {ke}. Using default setup guide.")

    md_setup_guide = conf.md.setup.format(
        name, source, name, install_guide, name, run_guide
    )

    return md_setup_guide


def create_directory_tree(url: str) -> str:
    """
    Creates a directory tree structure for the README.md
    file based on the provided repository path or URL.

    Parameters
    ----------
    url : str
        URL of the project's GitHub repository.

    Returns
    -------
    str
        Formatted string representing the project's directory tree structure.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_path = Path(tmp_dir) / "repo"

        try:
            git.Repo.clone_from(url, repo_path)
            tree_bytes = subprocess.check_output(["tree", "-n", repo_path])
            tree_str = tree_bytes.decode("utf-8")
            tree_lines = tree_str.split("\n")[1:]
            tree_str = "\n".join(tree_lines)
            tree_md = f"```bash\n{repo_path.name}\n{tree_str}```"
            return tree_md

        except git.exc.GitCommandError as e:
            LOGGER.warning(f"Error cloning repository: {e}")
            return ""

        except subprocess.CalledProcessError as e:
            LOGGER.warning(f"Error running 'tree' command: {e}")
            return ""

        except Exception as e:
            LOGGER.warning(f"Error creating directory tree: {e}")
            return ""


def create_tables(df: pd.DataFrame, dropdown: str) -> str:
    """
    Creates markdown tables for each sub-directory in the project.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing parsed information from project files.
    dropdown : str
        Markdown template for a dropdown menu.

    Returns
    -------
    str
        Formatted string with markdown tables for each sub-directory.
    """

    df["Sub-Directory"] = df["Module"].apply(
        lambda x: str(x).split("/")[-2].capitalize()
        if "/" in str(x)
        else "Root"
    )
    groups = df.groupby("Sub-Directory")
    tables = [
        group[["File", "Summary", "Module"]].to_markdown(index=False)
        for _, group in groups
    ]
    table_wrappers = [
        dropdown.format(sub_dir_name, table)
        for sub_dir_name, table in zip(groups.groups.keys(), tables)
    ]
    return "\n".join(table_wrappers)


def parse_pandas_cols(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parses the Module field to create two additional DataFrame
    columns to be displayed in the README code summary tables.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing parsed details from project files.

    Returns
    -------
    pd.DataFrame
        Processed DataFrame with additional columns.
    """

    df["Directory"] = df["Module"].apply(lambda x: str(Path(x).parent))
    df["File"] = df["Module"].apply(lambda x: str(Path(x).name))
    return df
