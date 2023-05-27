
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
OOP-Project
</h1>
<h3 align="center">📍 Bringing Order to your Object-Oriented Programming Projects</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="sample" />
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="h" />
<img src="https://img.shields.io/badge/CMake-064F8C.svg?style=for-the-badge&logo=CMake&logoColor=white" alt="xml" />
<img src="https://img.shields.io/badge/PowerShell-5391FE.svg?style=for-the-badge&logo=PowerShell&logoColor=white" alt="a" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The GitHub project OOP-Project is a powerful tool for developing object-oriented programming projects in Java. It is designed to help developers quickly create sophisticated programs with a library of reusable code. Additionally, it offers a powerful debugging system and a range of other useful features for the creation of efficient and reliable programs.

## 🔮 Features

> `[📌  INSERT-PROJECT-FEATURES]`

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── CMakeLists.txt
├── Dockerfile
├── LICENSE
├── README.md
├── codecov.yml
├── images
│   ├── Untitled 1.png
│   ├── Untitled 2.png
│   ├── Untitled 3.png
│   ├── Untitled.png
│   └── image1.png
├── script
│   ├── build_dependencies.sh
│   ├── build_onCS50.sh
│   └── mysql.sh
├── src
│   ├── dao
│   │   ├── PeopleDao.cpp
│   │   ├── SubjectDao.cpp
│   │   └── include
│   │       ├── PeopleDao.h
│   │       ├── SubjectDao.h
│   │       └── databaseTables.h
│   ├── main.cpp
│   ├── service
│   │   ├── PeopleCommunications.cpp
│   │   ├── PeopleServices.cpp
│   │   ├── StudentServices.cpp
│   │   ├── SubjectServices.cpp
│   │   ├── TeacherServices.cpp
│   │   ├── TutorServices.cpp
│   │   └── include
│   │       ├── PeopleCommunications.h
│   │       ├── PeopleServices.h
│   │       ├── SERVICE_PUBLIC.h
│   │       ├── StudentServices.h
│   │       ├── SubjectServices.h
│   │       ├── TeacherServices.h
│   │       └── TutorServices.h
│   └── vo
│       ├── Message.cpp
│       ├── People.cpp
│       ├── Storage.cpp
│       ├── Student.cpp
│       ├── Subject.cpp
│       ├── Teacher.cpp
│       ├── Tutor.cpp
│       └── include
│           ├── Message.h
│           ├── People.h
│           ├── Storage.h
│           ├── Student.h
│           ├── Subject.h
│           ├── Teacher.h
│           ├── Tutor.h
│           └── VO_PUBLIC.h
├── test
│   ├── PeopleDao_test.cpp
│   ├── PeopleServices_test.cpp
│   ├── SubjectDao_test.cpp
│   ├── SubjectServices_test.cpp
│   ├── database_test.cpp
│   └── input_tests
│       ├── initPassword
│       │   ├── input1.txt
│       │   ├── input2.txt
│       │   └── intpassword_test.sh
│       ├── input_test.cpp
│       ├── main_input_case-01
│       │   ├── input.txt
│       │   ├── result.txt
│       │   └── test.sh
│       └── main_input_case-02
│           ├── input.txt
│           ├── result.txt
│           └── test.sh
└── utils
    ├── VariadicTable.h
    ├── database_connection.cpp
    ├── database_connection.h
    ├── db.sql
    ├── prettyprint.hpp
    └── sqlpp11-connector-mysql
        ├── installed
        │   ├── x64-linux
        │   │   ├── debug
        │   │   │   └── lib
        │   │   │       ├── libcrypto.a
        │   │   │       ├── libdate-tz.a
        │   │   │       ├── libmariadb.a
        │   │   │       ├── libmariadbclient.a
        │   │   │       ├── libsqlpp-mysql.a
        │   │   │       ├── libssl.a
        │   │   │       ├── libz.a
        │   │   │       └── pkgconfig
        │   │   │           ├── libmariadb.pc
        │   │   │           └── zlib.pc
        │   │   ├── include
        │   │   │   ├── date
        │   │   │   │   ├── date.h
        │   │   │   │   └── tz.h
        │   │   │   ├── mysql
        │   │   │   │   ├── errmsg.h
        │   │   │   │   ├── ma_list.h
        │   │   │   │   ├── ma_pvio.h
        │   │   │   │   ├── ma_tls.h
        │   │   │   │   ├── mariadb
        │   │   │   │   │   └── ma_io.h
        │   │   │   │   ├── mariadb_com.h
        │   │   │   │   ├── mariadb_ctype.h
        │   │   │   │   ├── mariadb_dyncol.h
        │   │   │   │   ├── mariadb_rpl.h
        │   │   │   │   ├── mariadb_stmt.h
        │   │   │   │   ├── mariadb_version.h
        │   │   │   │   ├── mysql
        │   │   │   │   │   ├── client_plugin.h
        │   │   │   │   │   ├── plugin_auth.h
        │   │   │   │   │   └── plugin_auth_common.h
        │   │   │   │   ├── mysql.h
        │   │   │   │   └── mysqld_error.h
        │   │   │   ├── openssl
        │   │   │   │   ├── aes.h
        │   │   │   │   ├── asn1.h
        │   │   │   │   ├── asn1_mac.h
        │   │   │   │   ├── asn1err.h
        │   │   │   │   ├── asn1t.h
        │   │   │   │   ├── async.h
        │   │   │   │   ├── asyncerr.h
        │   │   │   │   ├── bio.h
        │   │   │   │   ├── bioerr.h
        │   │   │   │   ├── blowfish.h
        │   │   │   │   ├── bn.h
        │   │   │   │   ├── bnerr.h
        │   │   │   │   ├── buffer.h
        │   │   │   │   ├── buffererr.h
        │   │   │   │   ├── camellia.h
        │   │   │   │   ├── cast.h
        │   │   │   │   ├── cmac.h
        │   │   │   │   ├── cms.h
        │   │   │   │   ├── cmserr.h
        │   │   │   │   ├── comp.h
        │   │   │   │   ├── comperr.h
        │   │   │   │   ├── conf.h
        │   │   │   │   ├── conf_api.h
        │   │   │   │   ├── conferr.h
        │   │   │   │   ├── crypto.h
        │   │   │   │   ├── cryptoerr.h
        │   │   │   │   ├── ct.h
        │   │   │   │   ├── cterr.h
        │   │   │   │   ├── des.h
        │   │   │   │   ├── dh.h
        │   │   │   │   ├── dherr.h
        │   │   │   │   ├── dsa.h
        │   │   │   │   ├── dsaerr.h
        │   │   │   │   ├── dtls1.h
        │   │   │   │   ├── e_os2.h
        │   │   │   │   ├── ebcdic.h
        │   │   │   │   ├── ec.h
        │   │   │   │   ├── ecdh.h
        │   │   │   │   ├── ecdsa.h
        │   │   │   │   ├── ecerr.h
        │   │   │   │   ├── engine.h
        │   │   │   │   ├── engineerr.h
        │   │   │   │   ├── err.h
        │   │   │   │   ├── evp.h
        │   │   │   │   ├── evperr.h
        │   │   │   │   ├── hmac.h
        │   │   │   │   ├── idea.h
        │   │   │   │   ├── kdf.h
        │   │   │   │   ├── kdferr.h
        │   │   │   │   ├── lhash.h
        │   │   │   │   ├── md2.h
        │   │   │   │   ├── md4.h
        │   │   │   │   ├── md5.h
        │   │   │   │   ├── mdc2.h
        │   │   │   │   ├── modes.h
        │   │   │   │   ├── obj_mac.h
        │   │   │   │   ├── objects.h
        │   │   │   │   ├── objectserr.h
        │   │   │   │   ├── ocsp.h
        │   │   │   │   ├── ocsperr.h
        │   │   │   │   ├── opensslconf.h
        │   │   │   │   ├── opensslv.h
        │   │   │   │   ├── ossl_typ.h
        │   │   │   │   ├── pem.h
        │   │   │   │   ├── pem2.h
        │   │   │   │   ├── pemerr.h
        │   │   │   │   ├── pkcs12.h
        │   │   │   │   ├── pkcs12err.h
        │   │   │   │   ├── pkcs7.h
        │   │   │   │   ├── pkcs7err.h
        │   │   │   │   ├── rand.h
        │   │   │   │   ├── rand_drbg.h
        │   │   │   │   ├── randerr.h
        │   │   │   │   ├── rc2.h
        │   │   │   │   ├── rc4.h
        │   │   │   │   ├── rc5.h
        │   │   │   │   ├── ripemd.h
        │   │   │   │   ├── rsa.h
        │   │   │   │   ├── rsaerr.h
        │   │   │   │   ├── safestack.h
        │   │   │   │   ├── seed.h
        │   │   │   │   ├── sha.h
        │   │   │   │   ├── srp.h
        │   │   │   │   ├── srtp.h
        │   │   │   │   ├── ssl.h
        │   │   │   │   ├── ssl2.h
        │   │   │   │   ├── ssl3.h
        │   │   │   │   ├── sslerr.h
        │   │   │   │   ├── stack.h
        │   │   │   │   ├── store.h
        │   │   │   │   ├── storeerr.h
        │   │   │   │   ├── symhacks.h
        │   │   │   │   ├── tls1.h
        │   │   │   │   ├── ts.h
        │   │   │   │   ├── tserr.h
        │   │   │   │   ├── txt_db.h
        │   │   │   │   ├── ui.h
        │   │   │   │   ├── uierr.h
        │   │   │   │   ├── whrlpool.h
        │   │   │   │   ├── x509.h
        │   │   │   │   ├── x509_vfy.h
        │   │   │   │   ├── x509err.h
        │   │   │   │   ├── x509v3.h
        │   │   │   │   └── x509v3err.h
        │   │   │   ├── sqlpp11
        │   │   │   │   ├── aggregate_function_operators.h
        │   │   │   │   ├── aggregate_functions
        │   │   │   │   │   ├── avg.h
        │   │   │   │   │   ├── count.h
        │   │   │   │   │   ├── max.h
        │   │   │   │   │   ├── min.h
        │   │   │   │   │   └── sum.h
        │   │   │   │   ├── aggregate_functions.h
        │   │   │   │   ├── alias.h
        │   │   │   │   ├── alias_operators.h
        │   │   │   │   ├── alias_provider.h
        │   │   │   │   ├── all_of.h
        │   │   │   │   ├── any.h
        │   │   │   │   ├── assignment.h
        │   │   │   │   ├── auto_alias.h
        │   │   │   │   ├── bad_expression.h
        │   │   │   │   ├── basic_expression_operators.h
        │   │   │   │   ├── boolean_expression.h
        │   │   │   │   ├── case.h
        │   │   │   │   ├── char_sequence.h
        │   │   │   │   ├── chrono.h
        │   │   │   │   ├── column.h
        │   │   │   │   ├── column_fwd.h
        │   │   │   │   ├── column_types.h
        │   │   │   │   ├── connection.h
        │   │   │   │   ├── connection_pool.h
        │   │   │   │   ├── consistent.h
        │   │   │   │   ├── cte.h
        │   │   │   │   ├── custom_query.h
        │   │   │   │   ├── data_types
        │   │   │   │   │   ├── blob
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── blob.h
        │   │   │   │   │   ├── boolean
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── boolean.h
        │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   ├── day_point
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── day_point.h
        │   │   │   │   │   ├── floating_point
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── floating_point.h
        │   │   │   │   │   ├── integral
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── integral.h
        │   │   │   │   │   ├── no_value
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── no_value.h
        │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   ├── parameter_value_base.h
        │   │   │   │   │   ├── text
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── concat.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── like.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   ├── return_type_like.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── text.h
        │   │   │   │   │   ├── time_of_day
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── time_of_day.h
        │   │   │   │   │   ├── time_point
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   ├── time_point.h
        │   │   │   │   │   ├── unsigned_integral
        │   │   │   │   │   │   ├── column_operators.h
        │   │   │   │   │   │   ├── data_type.h
        │   │   │   │   │   │   ├── expression_operators.h
        │   │   │   │   │   │   ├── operand.h
        │   │   │   │   │   │   ├── parameter_value.h
        │   │   │   │   │   │   ├── result_field.h
        │   │   │   │   │   │   └── wrap_operand.h
        │   │   │   │   │   └── unsigned_integral.h
        │   │   │   │   ├── data_types.h
        │   │   │   │   ├── default_value.h
        │   │   │   │   ├── detail
        │   │   │   │   │   ├── copy_tuple_args.h
        │   │   │   │   │   ├── enable_if.h
        │   │   │   │   │   ├── field_index_sequence.h
        │   │   │   │   │   ├── get_first.h
        │   │   │   │   │   ├── get_last.h
        │   │   │   │   │   ├── index_sequence.h
        │   │   │   │   │   ├── pick_arg.h
        │   │   │   │   │   ├── sum.h
        │   │   │   │   │   ├── type_set.h
        │   │   │   │   │   ├── type_vector.h
        │   │   │   │   │   └── void.h
        │   │   │   │   ├── dynamic_join.h
        │   │   │   │   ├── dynamic_pre_join.h
        │   │   │   │   ├── dynamic_select_column_list.h
        │   │   │   │   ├── eval.h
        │   │   │   │   ├── exception.h
        │   │   │   │   ├── exists.h
        │   │   │   │   ├── expression.h
        │   │   │   │   ├── expression_fwd.h
        │   │   │   │   ├── expression_operators.h
        │   │   │   │   ├── expression_return_types.h
        │   │   │   │   ├── field_spec.h
        │   │   │   │   ├── for_update.h
        │   │   │   │   ├── from.h
        │   │   │   │   ├── functions.h
        │   │   │   │   ├── group_by.h
        │   │   │   │   ├── having.h
        │   │   │   │   ├── hidden.h
        │   │   │   │   ├── in.h
        │   │   │   │   ├── in_fwd.h
        │   │   │   │   ├── inconsistent.h
        │   │   │   │   ├── insert.h
        │   │   │   │   ├── insert_value.h
        │   │   │   │   ├── insert_value_list.h
        │   │   │   │   ├── interpret.h
        │   │   │   │   ├── interpret_tuple.h
        │   │   │   │   ├── interpretable.h
        │   │   │   │   ├── interpretable_list.h
        │   │   │   │   ├── interpreter.h
        │   │   │   │   ├── into.h
        │   │   │   │   ├── is_not_null.h
        │   │   │   │   ├── is_null.h
        │   │   │   │   ├── is_null_fwd.h
        │   │   │   │   ├── join.h
        │   │   │   │   ├── join_types.h
        │   │   │   │   ├── limit.h
        │   │   │   │   ├── logic.h
        │   │   │   │   ├── multi_column.h
        │   │   │   │   ├── mysql
        │   │   │   │   │   ├── bind_result.h
        │   │   │   │   │   ├── char_result.h
        │   │   │   │   │   ├── char_result_row.h
        │   │   │   │   │   ├── connection.h
        │   │   │   │   │   ├── connection_config.h
        │   │   │   │   │   ├── mysql.h
        │   │   │   │   │   ├── prepared_statement.h
        │   │   │   │   │   └── serializer.h
        │   │   │   │   ├── named_interpretable.h
        │   │   │   │   ├── no_data.h
        │   │   │   │   ├── no_name.h
        │   │   │   │   ├── noop.h
        │   │   │   │   ├── noop_fwd.h
        │   │   │   │   ├── not_in.h
        │   │   │   │   ├── null.h
        │   │   │   │   ├── offset.h
        │   │   │   │   ├── on.h
        │   │   │   │   ├── operand_check.h
        │   │   │   │   ├── order_by.h
        │   │   │   │   ├── over.h
        │   │   │   │   ├── parameter.h
        │   │   │   │   ├── parameter_list.h
        │   │   │   │   ├── policy_update.h
        │   │   │   │   ├── pool_connection.h
        │   │   │   │   ├── portable_static_assert.h
        │   │   │   │   ├── ppgen
        │   │   │   │   │   ├── colops
        │   │   │   │   │   │   ├── auto_increment.h
        │   │   │   │   │   │   ├── blob.h
        │   │   │   │   │   │   ├── bool.h
        │   │   │   │   │   │   ├── comment.h
        │   │   │   │   │   │   ├── datetime.h
        │   │   │   │   │   │   ├── default.h
        │   │   │   │   │   │   ├── floating_point.h
        │   │   │   │   │   │   ├── foreign_key.h
        │   │   │   │   │   │   ├── index.h
        │   │   │   │   │   │   ├── integer.h
        │   │   │   │   │   │   ├── not_null.h
        │   │   │   │   │   │   ├── null.h
        │   │   │   │   │   │   ├── primary_key.h
        │   │   │   │   │   │   ├── text.h
        │   │   │   │   │   │   ├── timestamp.h
        │   │   │   │   │   │   ├── unique_index.h
        │   │   │   │   │   │   ├── unsigned_integer.h
        │   │   │   │   │   │   └── varchar.h
        │   │   │   │   │   ├── tblops
        │   │   │   │   │   │   ├── character_set.h
        │   │   │   │   │   │   ├── comment.h
        │   │   │   │   │   │   ├── default.h
        │   │   │   │   │   │   └── engine.h
        │   │   │   │   │   └── tools
        │   │   │   │   │       ├── tuple_pop_front.h
        │   │   │   │   │       └── wrap_seq.h
        │   │   │   │   ├── ppgen.h
        │   │   │   │   ├── pre_join.h
        │   │   │   │   ├── prepared_execute.h
        │   │   │   │   ├── prepared_insert.h
        │   │   │   │   ├── prepared_remove.h
        │   │   │   │   ├── prepared_select.h
        │   │   │   │   ├── prepared_update.h
        │   │   │   │   ├── remove.h
        │   │   │   │   ├── result.h
        │   │   │   │   ├── result_field.h
        │   │   │   │   ├── result_field_base.h
        │   │   │   │   ├── result_row.h
        │   │   │   │   ├── result_row_fwd.h
        │   │   │   │   ├── rhs_wrap.h
        │   │   │   │   ├── schema.h
        │   │   │   │   ├── schema_qualified_table.h
        │   │   │   │   ├── select.h
        │   │   │   │   ├── select_column_list.h
        │   │   │   │   ├── select_flag_list.h
        │   │   │   │   ├── select_flags.h
        │   │   │   │   ├── select_pseudo_table.h
        │   │   │   │   ├── serialize.h
        │   │   │   │   ├── serializer.h
        │   │   │   │   ├── serializer_context.h
        │   │   │   │   ├── simple_column.h
        │   │   │   │   ├── single_table.h
        │   │   │   │   ├── some.h
        │   │   │   │   ├── sort_order.h
        │   │   │   │   ├── sqlpp11.h
        │   │   │   │   ├── statement.h
        │   │   │   │   ├── statement_fwd.h
        │   │   │   │   ├── table.h
        │   │   │   │   ├── table_alias.h
        │   │   │   │   ├── table_ref.h
        │   │   │   │   ├── transaction.h
        │   │   │   │   ├── trim.h
        │   │   │   │   ├── tvin.h
        │   │   │   │   ├── type_traits.h
        │   │   │   │   ├── unconditional.h
        │   │   │   │   ├── union.h
        │   │   │   │   ├── union_data.h
        │   │   │   │   ├── union_flags.h
        │   │   │   │   ├── update.h
        │   │   │   │   ├── update_list.h
        │   │   │   │   ├── using.h
        │   │   │   │   ├── value.h
        │   │   │   │   ├── value_or_null.h
        │   │   │   │   ├── value_type.h
        │   │   │   │   ├── value_type_fwd.h
        │   │   │   │   ├── verbatim.h
        │   │   │   │   ├── verbatim_table.h
        │   │   │   │   ├── where.h
        │   │   │   │   ├── with.h
        │   │   │   │   ├── without_table_check.h
        │   │   │   │   ├── wrap_operand.h
        │   │   │   │   └── wrong.h
        │   │   │   ├── zconf.h
        │   │   │   └── zlib.h
        │   │   ├── lib
        │   │   │   ├── libcrypto.a
        │   │   │   ├── libdate-tz.a
        │   │   │   ├── libmariadb.a
        │   │   │   ├── libmariadbclient.a
        │   │   │   ├── libsqlpp-mysql.a
        │   │   │   ├── libssl.a
        │   │   │   ├── libz.a
        │   │   │   └── pkgconfig
        │   │   │       ├── libmariadb.pc
        │   │   │       └── zlib.pc
        │   │   ├── scripts
        │   │   │   └── sqlpp11-ddl2cpp
        │   │   └── share
        │   │       ├── date
        │   │       │   ├── copyright
        │   │       │   ├── dateConfig.cmake
        │   │       │   ├── dateConfigVersion.cmake
        │   │       │   ├── dateTargets-debug.cmake
        │   │       │   ├── dateTargets-release.cmake
        │   │       │   ├── dateTargets.cmake
        │   │       │   └── vcpkg_abi_info.txt
        │   │       ├── libmariadb
        │   │       │   ├── copyright
        │   │       │   └── vcpkg_abi_info.txt
        │   │       ├── openssl
        │   │       │   ├── usage
        │   │       │   ├── vcpkg-cmake-wrapper.cmake
        │   │       │   └── vcpkg_abi_info.txt
        │   │       ├── openssl-unix
        │   │       │   ├── copyright
        │   │       │   └── vcpkg_abi_info.txt
        │   │       ├── sqlpp11
        │   │       │   ├── FindHinnantDate.cmake
        │   │       │   ├── Sqlpp11Config.cmake
        │   │       │   ├── Sqlpp11ConfigVersion.cmake
        │   │       │   ├── Sqlpp11Targets.cmake
        │   │       │   ├── copyright
        │   │       │   └── vcpkg_abi_info.txt
        │   │       ├── sqlpp11-connector-mysql
        │   │       │   ├── copyright
        │   │       │   └── vcpkg_abi_info.txt
        │   │       └── zlib
        │   │           ├── copyright
        │   │           ├── usage
        │   │           └── vcpkg_abi_info.txt
        │   └── x64-osx
        │       ├── debug
        │       │   └── lib
        │       │       ├── libcrypto.a
        │       │       ├── libdate-tz.a
        │       │       ├── libmariadb.a
        │       │       ├── libmariadbclient.a
        │       │       ├── libsqlpp-mysql.a
        │       │       ├── libssl.a
        │       │       ├── libz.a
        │       │       └── pkgconfig
        │       │           ├── libmariadb.pc
        │       │           └── zlib.pc
        │       ├── include
        │       │   ├── date
        │       │   │   ├── date.h
        │       │   │   └── tz.h
        │       │   ├── mysql
        │       │   │   ├── errmsg.h
        │       │   │   ├── ma_list.h
        │       │   │   ├── ma_pvio.h
        │       │   │   ├── ma_tls.h
        │       │   │   ├── mariadb
        │       │   │   │   └── ma_io.h
        │       │   │   ├── mariadb_com.h
        │       │   │   ├── mariadb_ctype.h
        │       │   │   ├── mariadb_dyncol.h
        │       │   │   ├── mariadb_rpl.h
        │       │   │   ├── mariadb_stmt.h
        │       │   │   ├── mariadb_version.h
        │       │   │   ├── mysql
        │       │   │   │   ├── client_plugin.h
        │       │   │   │   ├── plugin_auth.h
        │       │   │   │   └── plugin_auth_common.h
        │       │   │   ├── mysql.h
        │       │   │   └── mysqld_error.h
        │       │   ├── openssl
        │       │   │   ├── __DECC_INCLUDE_EPILOGUE.H
        │       │   │   ├── __DECC_INCLUDE_PROLOGUE.H
        │       │   │   ├── aes.h
        │       │   │   ├── asn1.h
        │       │   │   ├── asn1_mac.h
        │       │   │   ├── asn1err.h
        │       │   │   ├── asn1t.h
        │       │   │   ├── async.h
        │       │   │   ├── asyncerr.h
        │       │   │   ├── bio.h
        │       │   │   ├── bioerr.h
        │       │   │   ├── blowfish.h
        │       │   │   ├── bn.h
        │       │   │   ├── bnerr.h
        │       │   │   ├── buffer.h
        │       │   │   ├── buffererr.h
        │       │   │   ├── camellia.h
        │       │   │   ├── cast.h
        │       │   │   ├── cmac.h
        │       │   │   ├── cms.h
        │       │   │   ├── cmserr.h
        │       │   │   ├── comp.h
        │       │   │   ├── comperr.h
        │       │   │   ├── conf.h
        │       │   │   ├── conf_api.h
        │       │   │   ├── conferr.h
        │       │   │   ├── crypto.h
        │       │   │   ├── cryptoerr.h
        │       │   │   ├── ct.h
        │       │   │   ├── cterr.h
        │       │   │   ├── des.h
        │       │   │   ├── dh.h
        │       │   │   ├── dherr.h
        │       │   │   ├── dsa.h
        │       │   │   ├── dsaerr.h
        │       │   │   ├── dtls1.h
        │       │   │   ├── e_os2.h
        │       │   │   ├── ebcdic.h
        │       │   │   ├── ec.h
        │       │   │   ├── ecdh.h
        │       │   │   ├── ecdsa.h
        │       │   │   ├── ecerr.h
        │       │   │   ├── engine.h
        │       │   │   ├── engineerr.h
        │       │   │   ├── err.h
        │       │   │   ├── evp.h
        │       │   │   ├── evperr.h
        │       │   │   ├── hmac.h
        │       │   │   ├── idea.h
        │       │   │   ├── kdf.h
        │       │   │   ├── kdferr.h
        │       │   │   ├── lhash.h
        │       │   │   ├── md2.h
        │       │   │   ├── md4.h
        │       │   │   ├── md5.h
        │       │   │   ├── mdc2.h
        │       │   │   ├── modes.h
        │       │   │   ├── obj_mac.h
        │       │   │   ├── objects.h
        │       │   │   ├── objectserr.h
        │       │   │   ├── ocsp.h
        │       │   │   ├── ocsperr.h
        │       │   │   ├── opensslconf.h
        │       │   │   ├── opensslv.h
        │       │   │   ├── ossl_typ.h
        │       │   │   ├── pem.h
        │       │   │   ├── pem2.h
        │       │   │   ├── pemerr.h
        │       │   │   ├── pkcs12.h
        │       │   │   ├── pkcs12err.h
        │       │   │   ├── pkcs7.h
        │       │   │   ├── pkcs7err.h
        │       │   │   ├── rand.h
        │       │   │   ├── rand_drbg.h
        │       │   │   ├── randerr.h
        │       │   │   ├── rc2.h
        │       │   │   ├── rc4.h
        │       │   │   ├── rc5.h
        │       │   │   ├── ripemd.h
        │       │   │   ├── rsa.h
        │       │   │   ├── rsaerr.h
        │       │   │   ├── safestack.h
        │       │   │   ├── seed.h
        │       │   │   ├── sha.h
        │       │   │   ├── srp.h
        │       │   │   ├── srtp.h
        │       │   │   ├── ssl.h
        │       │   │   ├── ssl2.h
        │       │   │   ├── ssl3.h
        │       │   │   ├── sslerr.h
        │       │   │   ├── stack.h
        │       │   │   ├── store.h
        │       │   │   ├── storeerr.h
        │       │   │   ├── symhacks.h
        │       │   │   ├── tls1.h
        │       │   │   ├── ts.h
        │       │   │   ├── tserr.h
        │       │   │   ├── txt_db.h
        │       │   │   ├── ui.h
        │       │   │   ├── uierr.h
        │       │   │   ├── whrlpool.h
        │       │   │   ├── x509.h
        │       │   │   ├── x509_vfy.h
        │       │   │   ├── x509err.h
        │       │   │   ├── x509v3.h
        │       │   │   └── x509v3err.h
        │       │   ├── sqlpp11
        │       │   │   ├── aggregate_function_operators.h
        │       │   │   ├── aggregate_functions
        │       │   │   │   ├── avg.h
        │       │   │   │   ├── count.h
        │       │   │   │   ├── max.h
        │       │   │   │   ├── min.h
        │       │   │   │   └── sum.h
        │       │   │   ├── aggregate_functions.h
        │       │   │   ├── alias.h
        │       │   │   ├── alias_operators.h
        │       │   │   ├── alias_provider.h
        │       │   │   ├── all_of.h
        │       │   │   ├── any.h
        │       │   │   ├── assignment.h
        │       │   │   ├── auto_alias.h
        │       │   │   ├── bad_expression.h
        │       │   │   ├── basic_expression_operators.h
        │       │   │   ├── boolean_expression.h
        │       │   │   ├── case.h
        │       │   │   ├── char_sequence.h
        │       │   │   ├── chrono.h
        │       │   │   ├── column.h
        │       │   │   ├── column_fwd.h
        │       │   │   ├── column_types.h
        │       │   │   ├── connection.h
        │       │   │   ├── connection_pool.h
        │       │   │   ├── consistent.h
        │       │   │   ├── cte.h
        │       │   │   ├── custom_query.h
        │       │   │   ├── data_types
        │       │   │   │   ├── blob
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── blob.h
        │       │   │   │   ├── boolean
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── boolean.h
        │       │   │   │   ├── column_operators.h
        │       │   │   │   ├── day_point
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── day_point.h
        │       │   │   │   ├── floating_point
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── floating_point.h
        │       │   │   │   ├── integral
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── integral.h
        │       │   │   │   ├── no_value
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── no_value.h
        │       │   │   │   ├── parameter_value.h
        │       │   │   │   ├── parameter_value_base.h
        │       │   │   │   ├── text
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── concat.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── like.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   ├── return_type_like.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── text.h
        │       │   │   │   ├── time_of_day
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── time_of_day.h
        │       │   │   │   ├── time_point
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   ├── time_point.h
        │       │   │   │   ├── unsigned_integral
        │       │   │   │   │   ├── column_operators.h
        │       │   │   │   │   ├── data_type.h
        │       │   │   │   │   ├── expression_operators.h
        │       │   │   │   │   ├── operand.h
        │       │   │   │   │   ├── parameter_value.h
        │       │   │   │   │   ├── result_field.h
        │       │   │   │   │   └── wrap_operand.h
        │       │   │   │   └── unsigned_integral.h
        │       │   │   ├── data_types.h
        │       │   │   ├── default_value.h
        │       │   │   ├── detail
        │       │   │   │   ├── copy_tuple_args.h
        │       │   │   │   ├── enable_if.h
        │       │   │   │   ├── field_index_sequence.h
        │       │   │   │   ├── get_first.h
        │       │   │   │   ├── get_last.h
        │       │   │   │   ├── index_sequence.h
        │       │   │   │   ├── pick_arg.h
        │       │   │   │   ├── sum.h
        │       │   │   │   ├── type_set.h
        │       │   │   │   ├── type_vector.h
        │       │   │   │   └── void.h
        │       │   │   ├── dynamic_join.h
        │       │   │   ├── dynamic_pre_join.h
        │       │   │   ├── dynamic_select_column_list.h
        │       │   │   ├── eval.h
        │       │   │   ├── exception.h
        │       │   │   ├── exists.h
        │       │   │   ├── expression.h
        │       │   │   ├── expression_fwd.h
        │       │   │   ├── expression_operators.h
        │       │   │   ├── expression_return_types.h
        │       │   │   ├── field_spec.h
        │       │   │   ├── for_update.h
        │       │   │   ├── from.h
        │       │   │   ├── functions.h
        │       │   │   ├── group_by.h
        │       │   │   ├── having.h
        │       │   │   ├── hidden.h
        │       │   │   ├── in.h
        │       │   │   ├── in_fwd.h
        │       │   │   ├── inconsistent.h
        │       │   │   ├── insert.h
        │       │   │   ├── insert_value.h
        │       │   │   ├── insert_value_list.h
        │       │   │   ├── interpret.h
        │       │   │   ├── interpret_tuple.h
        │       │   │   ├── interpretable.h
        │       │   │   ├── interpretable_list.h
        │       │   │   ├── interpreter.h
        │       │   │   ├── into.h
        │       │   │   ├── is_not_null.h
        │       │   │   ├── is_null.h
        │       │   │   ├── is_null_fwd.h
        │       │   │   ├── join.h
        │       │   │   ├── join_types.h
        │       │   │   ├── limit.h
        │       │   │   ├── logic.h
        │       │   │   ├── multi_column.h
        │       │   │   ├── mysql
        │       │   │   │   ├── bind_result.h
        │       │   │   │   ├── char_result.h
        │       │   │   │   ├── char_result_row.h
        │       │   │   │   ├── connection.h
        │       │   │   │   ├── connection_config.h
        │       │   │   │   ├── mysql.h
        │       │   │   │   ├── prepared_statement.h
        │       │   │   │   └── serializer.h
        │       │   │   ├── named_interpretable.h
        │       │   │   ├── no_data.h
        │       │   │   ├── no_name.h
        │       │   │   ├── noop.h
        │       │   │   ├── noop_fwd.h
        │       │   │   ├── not_in.h
        │       │   │   ├── null.h
        │       │   │   ├── offset.h
        │       │   │   ├── on.h
        │       │   │   ├── operand_check.h
        │       │   │   ├── order_by.h
        │       │   │   ├── over.h
        │       │   │   ├── parameter.h
        │       │   │   ├── parameter_list.h
        │       │   │   ├── policy_update.h
        │       │   │   ├── pool_connection.h
        │       │   │   ├── portable_static_assert.h
        │       │   │   ├── ppgen
        │       │   │   │   ├── colops
        │       │   │   │   │   ├── auto_increment.h
        │       │   │   │   │   ├── blob.h
        │       │   │   │   │   ├── bool.h
        │       │   │   │   │   ├── comment.h
        │       │   │   │   │   ├── datetime.h
        │       │   │   │   │   ├── default.h
        │       │   │   │   │   ├── floating_point.h
        │       │   │   │   │   ├── foreign_key.h
        │       │   │   │   │   ├── index.h
        │       │   │   │   │   ├── integer.h
        │       │   │   │   │   ├── not_null.h
        │       │   │   │   │   ├── null.h
        │       │   │   │   │   ├── primary_key.h
        │       │   │   │   │   ├── text.h
        │       │   │   │   │   ├── timestamp.h
        │       │   │   │   │   ├── unique_index.h
        │       │   │   │   │   ├── unsigned_integer.h
        │       │   │   │   │   └── varchar.h
        │       │   │   │   ├── tblops
        │       │   │   │   │   ├── character_set.h
        │       │   │   │   │   ├── comment.h
        │       │   │   │   │   ├── default.h
        │       │   │   │   │   └── engine.h
        │       │   │   │   └── tools
        │       │   │   │       ├── tuple_pop_front.h
        │       │   │   │       └── wrap_seq.h
        │       │   │   ├── ppgen.h
        │       │   │   ├── pre_join.h
        │       │   │   ├── prepared_execute.h
        │       │   │   ├── prepared_insert.h
        │       │   │   ├── prepared_remove.h
        │       │   │   ├── prepared_select.h
        │       │   │   ├── prepared_update.h
        │       │   │   ├── remove.h
        │       │   │   ├── result.h
        │       │   │   ├── result_field.h
        │       │   │   ├── result_field_base.h
        │       │   │   ├── result_row.h
        │       │   │   ├── result_row_fwd.h
        │       │   │   ├── rhs_wrap.h
        │       │   │   ├── schema.h
        │       │   │   ├── schema_qualified_table.h
        │       │   │   ├── select.h
        │       │   │   ├── select_column_list.h
        │       │   │   ├── select_flag_list.h
        │       │   │   ├── select_flags.h
        │       │   │   ├── select_pseudo_table.h
        │       │   │   ├── serialize.h
        │       │   │   ├── serializer.h
        │       │   │   ├── serializer_context.h
        │       │   │   ├── simple_column.h
        │       │   │   ├── single_table.h
        │       │   │   ├── some.h
        │       │   │   ├── sort_order.h
        │       │   │   ├── sqlpp11.h
        │       │   │   ├── statement.h
        │       │   │   ├── statement_fwd.h
        │       │   │   ├── table.h
        │       │   │   ├── table_alias.h
        │       │   │   ├── table_ref.h
        │       │   │   ├── transaction.h
        │       │   │   ├── trim.h
        │       │   │   ├── tvin.h
        │       │   │   ├── type_traits.h
        │       │   │   ├── unconditional.h
        │       │   │   ├── union.h
        │       │   │   ├── union_data.h
        │       │   │   ├── union_flags.h
        │       │   │   ├── update.h
        │       │   │   ├── update_list.h
        │       │   │   ├── using.h
        │       │   │   ├── value.h
        │       │   │   ├── value_or_null.h
        │       │   │   ├── value_type.h
        │       │   │   ├── value_type_fwd.h
        │       │   │   ├── verbatim.h
        │       │   │   ├── verbatim_table.h
        │       │   │   ├── where.h
        │       │   │   ├── with.h
        │       │   │   ├── without_table_check.h
        │       │   │   ├── wrap_operand.h
        │       │   │   └── wrong.h
        │       │   ├── zconf.h
        │       │   └── zlib.h
        │       ├── lib
        │       │   ├── libcrypto.a
        │       │   ├── libdate-tz.a
        │       │   ├── libmariadb.a
        │       │   ├── libmariadbclient.a
        │       │   ├── libsqlpp-mysql.a
        │       │   ├── libssl.a
        │       │   ├── libz.a
        │       │   └── pkgconfig
        │       │       ├── libmariadb.pc
        │       │       └── zlib.pc
        │       ├── scripts
        │       │   └── sqlpp11-ddl2cpp
        │       └── share
        │           ├── date
        │           │   ├── copyright
        │           │   ├── dateConfig.cmake
        │           │   ├── dateConfigVersion.cmake
        │           │   ├── dateTargets-debug.cmake
        │           │   ├── dateTargets-release.cmake
        │           │   ├── dateTargets.cmake
        │           │   └── vcpkg_abi_info.txt
        │           ├── libmariadb
        │           │   ├── copyright
        │           │   └── vcpkg_abi_info.txt
        │           ├── openssl
        │           │   ├── usage
        │           │   ├── vcpkg-cmake-wrapper.cmake
        │           │   └── vcpkg_abi_info.txt
        │           ├── openssl-unix
        │           │   ├── copyright
        │           │   └── vcpkg_abi_info.txt
        │           ├── sqlpp11
        │           │   ├── FindHinnantDate.cmake
        │           │   ├── Sqlpp11Config.cmake
        │           │   ├── Sqlpp11ConfigVersion.cmake
        │           │   ├── Sqlpp11Targets.cmake
        │           │   ├── copyright
        │           │   └── vcpkg_abi_info.txt
        │           ├── sqlpp11-connector-mysql
        │           │   ├── copyright
        │           │   └── vcpkg_abi_info.txt
        │           └── zlib
        │               ├── copyright
        │               ├── usage
        │               └── vcpkg_abi_info.txt
        └── scripts
            ├── buildsystems
            │   ├── msbuild
            │   │   ├── applocal.ps1
            │   │   ├── vcpkg-general.xml
            │   │   ├── vcpkg.props
            │   │   └── vcpkg.targets
            │   └── vcpkg.cmake
            └── cmake
                └── vcpkg_get_windows_sdk.cmake

102 directories, 949 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Aggregate_functions</summary>

| File    | Summary                                                                                                                                                                                                                                 | Module                                                                                        |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| min.h   | This code provides a definition for the min() aggregate function in the SQL++ library. It allows users to find the minimum value of an expression in a SQL query.                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions/min.h     |
| count.h | This code provides a template for the COUNT aggregate function in SQL. It allows for the use of the COUNT function with a distinct flag, and requires an expression as an argument.                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions/count.h   |
| avg.h   | This code provides a template for the SQL aggregate function AVG, which calculates the average of a given numeric expression. It includes support for the DISTINCT flag, which can be used to calculate the average of distinct values. | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions/avg.h     |
| sum.h   | This code provides a template for the SQL aggregate function SUM, which returns the sum of a numeric expression. It includes support for the DISTINCT flag, which returns the sum of distinct values of the expression.                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions/sum.h     |
| max.h   | This code provides a template for the MAX aggregate function in SQL. It allows for the expression of the MAX function in a type- safe manner.                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions/max.h     |
| min.h   | This code provides a definition for the min() aggregate function in the SQL++ library. It allows users to find the minimum value of an expression in a SQL query.                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions/min.h   |
| count.h | This code provides a template for the COUNT aggregate function in SQL. It allows for the use of the COUNT function with or without the DISTINCT flag. It also provides an alias for the COUNT function.                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions/count.h |
| avg.h   | This code provides a template for the SQL aggregate function AVG, which calculates the average of a given set of values. It includes support for the DISTINCT flag, which can be used to calculate the average of distinct values.      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions/avg.h   |
| sum.h   | This code provides a template for the SQL aggregate function SUM, which returns the sum of a numeric expression. It includes support for the DISTINCT flag, which returns the sum of distinct values of the expression.                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions/sum.h   |
| max.h   | This code provides a template for the MAX aggregate function in SQL. It allows for the expression of the MAX function in a type- safe manner.                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions/max.h   |

</details>

<details closed><summary>Buildsystems</summary>

| File        | Summary                 | Module                                                         |
|:------------|:------------------------|:---------------------------------------------------------------|
| vcpkg.cmake | Error fetching summary. | utils/sqlpp11-connector-mysql/scripts/buildsystems/vcpkg.cmake |

</details>

<details closed><summary>Cmake</summary>

| File                        | Summary                                                                                                                    | Module                                                                  |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| vcpkg_get_windows_sdk.cmake | This function retrieves the Windows SDK number from the environment variable and stores it in the output variable " ret ". | utils/sqlpp11-connector-mysql/scripts/cmake/vcpkg_get_windows_sdk.cmake |

</details>

<details closed><summary>Colops</summary>

| File               | Summary                                                                                                                                                                                                     | Module                                                                                            |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| index.h            | This code provides a macro for declaring column get and generate traits for an index in a table. It is not currently implemented.                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/index.h              |
| primary_key.h      | This code defines a macro for declaring a column's traits for a primary key. It specifies that the primary key must not be updated.                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/primary_key.h        |
| floating_point.h   | This code defines traits for the floating point data types float, real, and double. It allows for the use of these data types in SQL++.                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/floating_point.h     |
| text.h             | This code defines a macro for declaring a column get trait and a column gen trait for a text type. It is used to create a column type for a text type in SQL++.                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/text.h               |
| bool.h             | This code defines the traits for a boolean column type, allowing for the column to be used in SQL queries.                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/bool.h               |
| blob.h             | This code defines traits for columns of type blob, including tinyblob, blob, mediumblob, and longblob. It allows for the columns to be declared as:: sqlpp::blob.                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/blob.h               |
| null.h             | This code defines a macro for declaring a trait for a column that allows it to be null. It is used to enable the use of null values in SQL queries.                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/null.h               |
| comment.h          | This code defines a macro for the SQLPP library which is used to generate traits for a column with a comment. It is not currently implemented.                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/comment.h            |
| datetime.h         | This code defines two traits for columns of type date and datetime, allowing them to be used with the SQLPP library. It defines the return type of the columns as day_point and time_point respectively.    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/datetime.h           |
| varchar.h          | This code defines a macro for declaring a column with a varchar type. It is used to create a column with a varchar type in a SQL database.                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/varchar.h            |
| unique_index.h     | This code provides a macro for declaring a unique index on a table, which is not yet implemented.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/unique_index.h       |
| auto_increment.h   | This code provides a macro for declaring traits for a column with auto- increment values. It defines the tags must_not_insert and must_not_update, which prevent the column from being inserted or updated. | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/auto_increment.h     |
| foreign_key.h      | This code defines a macro for declaring a foreign key column in a SQL database. It is not currently implemented.                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/foreign_key.h        |
| integer.h          | This code defines macros for the traits of different types of integer columns in SQLPP. It provides a way to declare the traits of tinyint, smallint, int, and bigint columns.                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/integer.h            |
| timestamp.h        | This code defines a macro for declaring a column get trait for a timestamp type. It also declares a column generation trait for a timestamp type, which is a time_point.                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/timestamp.h          |
| default.h          | This code defines a macro for declaring column get and gen traits for the SQLPP_DEFAULT operation. It is used to provide a default value for a column in a SQL query.                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/default.h            |
| unsigned_integer.h | This code defines macros for declaring traits for unsigned integer columns in SQL. It provides macros for declaring traits for tinyint, smallint, int, and bigint columns.                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/unsigned_integer.h   |
| not_null.h         | This code provides a macro for declaring a column get and gen traits for the " not null " operation. It is used to ensure that a column is not null when inserting into a database.                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/colops/not_null.h           |
| index.h            | This code provides a macro for declaring column traits related to an index in a table. It is not currently implemented.                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/index.h            |
| primary_key.h      | This code defines a macro for declaring a column's traits for a primary key. It specifies that the primary key must not be updated.                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/primary_key.h      |
| floating_point.h   | This code defines traits for the floating point data types float, real, and double. It allows for the use of these data types in SQL++.                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/floating_point.h   |
| text.h             | This code defines a macro for declaring a column get trait for a text type. It also declares a macro for generating a column trait for a text type.                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/text.h             |
| bool.h             | This code defines the traits for a boolean column type, allowing for the column to be used in SQL queries.                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/bool.h             |
| blob.h             | This code defines traits for columns of type blob, including tinyblob, blob, mediumblob, and longblob. It allows for the columns to be declared as:: sqlpp::blob.                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/blob.h             |
| null.h             | This code defines a macro for declaring a trait for a column that allows it to be null. It is used to enable the use of the SQL NULL keyword in queries.                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/null.h             |
| comment.h          | This code defines a macro for the SQLPP library which is used to generate traits for a column with a comment. It is not currently implemented.                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/comment.h          |
| datetime.h         | This code defines two traits for columns of type date and datetime, allowing them to be used with the SQLPP library. It defines the return type of the columns as day_point and time_point respectively.    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/datetime.h         |
| varchar.h          | This code provides a macro for declaring a column with a varchar type in the SQL++ library. It defines a macro for declaring a column get trait and a macro for declaring a column gen trait.               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/varchar.h          |
| unique_index.h     | This code provides a macro for declaring a unique index on a table, which is not yet implemented.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/unique_index.h     |
| auto_increment.h   | This code defines a macro for declaring traits for a column with auto- increment values. It specifies that the column must not be inserted or updated.                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/auto_increment.h   |
| foreign_key.h      | This code defines a macro for declaring a foreign key column in a SQL database. It is not currently implemented.                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/foreign_key.h      |
| integer.h          | This code defines macros for declaring traits for different types of integer columns in SQL. It provides a way to define the traits for tinyint, smallint, int, and bigint columns.                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/integer.h          |
| timestamp.h        | This code defines a macro for declaring a column get trait for a timestamp type. It also declares a column generation trait for a timestamp type, which is a time_point.                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/timestamp.h        |
| default.h          | This code defines a macro for declaring column get and gen traits for the SQLPP_DEFAULT operation. It is used to provide a default value for a column in a SQL query.                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/default.h          |
| unsigned_integer.h | This code defines macros for declaring traits for unsigned integer columns in SQL. It provides macros for declaring traits for tinyint, smallint, int, and bigint columns.                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/unsigned_integer.h |
| not_null.h         | This code provides a macro for declaring a column get and gen traits for the " not null " operation. It is used to ensure that a column is not null when inserting into a database.                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/colops/not_null.h         |

</details>

<details closed><summary>Dao</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                        | Module                 |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| SubjectDao.cpp | This code is a program written in C++ that implements a Subject Data Access Object( DAO) for a Object- Oriented Programming( OOP) project. It contains functions to list all subjects, select one subject, select subjects by name, add a new subject, update people to a subject, and update a subject's name | src/dao/SubjectDao.cpp |
| PeopleDao.cpp  | Error fetching summary.                                                                                                                                                                                                                                                                                        | src/dao/PeopleDao.cpp  |

</details>

<details closed><summary>Date</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                             | Module                                                                                 |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| date.h                    | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/date/date.h                    |
| tz.h                      | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/date/tz.h                      |
| dateTargets.cmake         | This code is a CMake target import file that checks for the existence of certain files and creates imported targets for them. It also checks that the CMake version is greater than or equal to 2.6.0.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/dateTargets.cmake           |
| dateTargets-debug.cmake   | This code creates a CMake target import file for the configuration " Debug " for the target " date::date- tz ". It sets the imported configuration to " Debug ", the imported link interface languages to " CXX ", and the imported location to " $ { _ IMPORT_PREFIX}/debug / lib / libdate- tz                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/dateTargets-debug.cmake     |
| dateTargets-release.cmake | This code creates a CMake target import file for the configuration " Release " of the target " date::date- tz ". It sets the properties of the target, appends it to a list of targets, and appends a list of files associated with the target.                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/dateTargets-release.cmake   |
| vcpkg_abi_info.txt        | This code is a patch for a UWP application, using cmake 3.17.2 and core features. It includes a portfile.cmake, post_build_checks, triplet, vcpkg_check_features, vcpkg_configure_cmake, vcpkg_copy_pdbs,                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/vcpkg_abi_info.txt          |
| copyright                 | This project is released using the MIT License, with each file individually licensed. Contributors must add their name to the license of each file they modify, and can submit a new pull request to add their name to the license of any files they have already modified. The MIT License is included in each file without author names or dates. | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/copyright                   |
| dateConfig.cmake          | This code includes a CMakeFindDependencyMacro and a dateTargets.cmake file. If the compiler is not MSVC and the target is date::date- tz, it finds the dependency of Threads and checks if the target property matches libcurl. If it does, it finds the dependency of CURL                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/dateConfig.cmake            |
| dateConfigVersion.cmake   | This code is used to create a version- file which can be installed along a config.cmake file. It sets the PACKAGE_VERSION_EXACT and PACKAGE_VERSION_COMPATIBLE variables depending on the current version string and the requested version string. It also checks the 32/64bit- ness of the installed                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/share/date/dateConfigVersion.cmake     |
| date.h                    | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/date/date.h                  |
| tz.h                      | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/date/tz.h                    |
| dateTargets.cmake         | This code is a CMake target import file that checks for the existence of certain files and creates imported targets for them. It also checks that the CMake version is greater than or equal to 2.6.0.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/dateTargets.cmake         |
| dateTargets-debug.cmake   | This code creates a CMake target import file for the configuration " Debug " for the target " date::date- tz ". It sets the imported configuration to " Debug ", the imported link interface languages to " CXX ", and the imported location to " $ { _ IMPORT_PREFIX}/debug / lib / libdate- tz                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/dateTargets-debug.cmake   |
| dateTargets-release.cmake | This code creates a CMake target import file for the configuration " Release " of the target " date::date- tz ". It sets the properties of the target, appends it to a list of targets, and appends a list of files associated with the target.                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/dateTargets-release.cmake |
| vcpkg_abi_info.txt        | This code is a patch for a UWP application, using cmake 3.17.2 and core features. It includes a portfile.cmake, post_build_checks, triplet, vcpkg_check_features, vcpkg_configure_cmake, vcpkg_copy_pdbs,                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/vcpkg_abi_info.txt        |
| copyright                 | This project is released using the MIT License, with each file individually licensed. Contributors must add their name to the license of each file they modify, and can submit a new pull request to add their name to the license of any files they have already modified. A copy of the MIT License is included in each file.                     | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/copyright                 |
| dateConfig.cmake          | This code includes a CMakeFindDependencyMacro and a dateTargets.cmake file. If the compiler is not MSVC and the target is date::date- tz, it finds the dependency of Threads and checks if the target property of date::date- tz matches libcurl. If it does, it                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/dateConfig.cmake          |
| dateConfigVersion.cmake   | This code is used to create a version- file which can be installed along a config.cmake file. It sets the PACKAGE_VERSION_EXACT and PACKAGE_VERSION_COMPATIBLE variables depending on the current version string and the requested version string. It also checks the 32/64bit- ness of the installed                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/share/date/dateConfigVersion.cmake   |

</details>

<details closed><summary>Detail</summary>

| File                   | Summary                                                                                                                                                                                                                                                                                                                                         | Module                                                                                          |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| pick_arg.h             | This code provides a template function to pick an argument from either a statement or a new term. It is copyright( c) 2013- 2015, Roland Bock and is used to provide a consistent way to pick an argument from either a statement or a new term.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/pick_arg.h               |
| get_last.h             | This code provides a template for retrieving the last element in a list of types that satisfies a given predicate, or a default type if no such element is found.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/get_last.h               |
| enable_if.h            | This code provides a template for enabling a type if a boolean condition is met. It is part of the SQLPP11 library, written by Roland Bock, and is used to enable certain types depending on the given condition.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/enable_if.h              |
| type_vector.h          | This code provides a template for type_vector, which is a type that stores a list of types. It also provides functions for concatenating two type_vectors and for getting the size of a type_vector.                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/type_vector.h            |
| field_index_sequence.h | This code provides a template for creating a field index sequence, which is used to keep track of the order of fields in a database table. It is used to ensure that the fields are correctly indexed and can be used to access the data in the table.                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/field_index_sequence.h   |
| void.h                 | This code provides a template for a type alias called void_t, which is used to represent a void type. It is used to provide a type- safe way to represent a void type in a template.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/void.h                   |
| sum.h                  | This code provides a template function for calculating the sum of a variable number of arguments. It is a non- recursive C++14 version of the sum function.                                                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/sum.h                    |
| get_first.h            | This code provides a template for retrieving the first type from a list of types that satisfies a given predicate, or a default type if none of the types satisfy the predicate.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/get_first.h              |
| type_set.h             | This code provides a set of functions for manipulating type sets, which are collections of types. It includes functions for creating type sets, checking if a type is an element of a set, joining two sets, checking if one set is a subset of another, checking if two sets are disjoint, creating a difference set, creating an intersection | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/type_set.h               |
| index_sequence.h       | This code provides a minimalistic implementation of index_sequence, a type available in C++14, for use in C++11. It provides a template for creating a sequence of integers of a given size, which can be used to index into a tuple or other data structure.                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/index_sequence.h         |
| copy_tuple_args.h      | This code provides a template for merging multiple columns into a single tuple. It is used to create a tuple of columns from a single column or a tuple of columns. It is copyright( c) 2013- 2015, Roland Bock and is provided under the terms of the BSD 3- Clause License.                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/detail/copy_tuple_args.h        |
| pick_arg.h             | This code provides a template function to pick an argument from either a statement or a new term. It is copyright( c) 2013- 2015, Roland Bock and is used to provide a consistent way to pick an argument from either a statement or a new term.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/pick_arg.h             |
| get_last.h             | This code provides a template for retrieving the last element in a list of types that satisfies a given predicate, or a default type if no such element is found.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/get_last.h             |
| enable_if.h            | This code provides a template for enabling a type if a boolean condition is met. It is part of the SQLPP11 library, written by Roland Bock, and is used to enable certain types depending on the given condition.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/enable_if.h            |
| type_vector.h          | This code provides a template for type_vector, which is a type that stores a list of types. It also provides functions for combining type_vectors, and for getting the size of a type_vector.                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/type_vector.h          |
| field_index_sequence.h | This code provides a template for creating a field index sequence, which is used to keep track of the order of fields in a database table. It is used to ensure that the fields are correctly indexed and can be used to access the data in the table.                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/field_index_sequence.h |
| void.h                 | This code provides a template for a type alias called void_t, which is used to represent a void type. It is used to provide a type- safe way to represent a void type in a template.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/void.h                 |
| sum.h                  | This code provides a template function for calculating the sum of a given set of numbers. It is a non- recursive C++14 version of the sum function.                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/sum.h                  |
| get_first.h            | This code provides a template for retrieving the first type from a list of types that satisfies a given predicate, or a default type if none of the types satisfy the predicate.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/get_first.h            |
| type_set.h             | This code provides a set of functions for manipulating type sets, which are collections of types. It includes functions for creating type sets, checking if a type is an element of a set, joining two sets, checking if one set is a subset of another, checking if two sets are disjoint, creating a difference set, creating an intersection | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/type_set.h             |
| index_sequence.h       | This code provides a minimalistic implementation of index_sequence, a type available in C++14, for use in C++11. It provides a template for creating a sequence of integers of a given size, which can be used to index into a tuple or other data structure.                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/index_sequence.h       |
| copy_tuple_args.h      | This code provides a template for merging multiple columns into a single tuple. It is used to create a tuple of columns from a single column or a tuple of columns. It is copyright( c) 2013- 2015, Roland Bock and is provided under the terms of the BSD 3- Clause License.                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/detail/copy_tuple_args.h      |

</details>

<details closed><summary>Include</summary>

| File                   | Summary                                                                                                                                                                                                                                                                                                                                                                                      | Module                                                            |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| zlib.h                 | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/zlib.h    |
| zconf.h                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/zconf.h   |
| zlib.h                 | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/zlib.h  |
| zconf.h                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/zconf.h |
| VO_PUBLIC.h            | This code is a header file for an Object- Oriented Programming project created by Akide Liu, Andrew Wang, and Chi Wang on 24/9/20. It includes the necessary libraries and header files for the project, such as People.h, Storage.h, Student.h, Subject.h, Teacher.h,                                                                                                                       | src/vo/include/VO_PUBLIC.h                                        |
| Teacher.h              | This code is a C++ class definition for a Teacher class, which is a subclass of the People class. It contains a private userLevel variable and a public getUserLevel() method. It also contains a constructor which takes in userId, name, password, title, isActive, and userLevel as parameters.                                                                                           | src/vo/include/Teacher.h                                          |
| Message.h              | This code is a class definition for a Message object, written by Akide Liu on 20/10/20 and released under the GNU General Public License v3.0. The Message object contains attributes such as messageID, studentID, requestSubjectID, tutorID, subjectName, studentName, tutorName, approve, and tutor                                                                                       | src/vo/include/Message.h                                          |
| Tutor.h                | This code is a C++ class definition for a Tutor object, which is a subclass of the People class. It contains a private userLevel variable and a public getUserLevel() method. It also contains a constructor which takes in userId, name, password, title, isActive, and userLevel as parameters.                                                                                            | src/vo/include/Tutor.h                                            |
| Storage.h              | This code is a C++ class that implements a Storage object. It contains methods to get and set user and subject IDs, as well as a vector of Message objects. It also includes a GNU General Public License.                                                                                                                                                                                   | src/vo/include/Storage.h                                          |
| People.h               | This code is a class definition for a People object, which contains attributes such as user_id, name, password, title, and isActive. It also contains methods to get and set these attributes. The userLevel attribute is used to determine the user's level( student, tutor, or teacher). The code also includes a friend operator                                                          | src/vo/include/People.h                                           |
| Student.h              | This code is a C++ class for a Student object, which is a subclass of the People class. It contains a constructor, a getUserLevel() method, and an overloaded operator for outputting the Student object. It is part of an OOP- Project and is released under the GNU General Public License.                                                                                                | src/vo/include/Student.h                                          |
| Subject.h              | This code is a C++ program written by Akide Liu, Andrew Wang, and Chi Wang on 24/9/20. It is a part of an OOP- Project and is distributed under the GNU General Public License. It defines a class called Subject which contains private variables subject_id and subject_name, and public functions to                                                                                      | src/vo/include/Subject.h                                          |
| PeopleDao.h            | This code is a class called PeopleDao which provides functions to list, select, insert and update people information. It includes functions to list all users, show all students, tutors and teachers, select one people by i d, select people by name, select subjects people enrolled by user i d, add new student, tutor and teacher, and                                                 | src/dao/include/PeopleDao.h                                       |
| SubjectDao.h           | This code is a class called SubjectDao which provides functions to list, select, insert and update subjects. It is written by Akide Liu, Andrew Wang and Chi Wang on 24/9/20 and is distributed under the GNU General Public License.                                                                                                                                                        | src/dao/include/SubjectDao.h                                      |
| PeopleServices.h       | This code is a class definition for PeopleServices, which provides static utility functions and user action functions for managing users, tutors, students, and subjects. It includes functions for logging in and out, changing passwords, listing all users, checking user levels, resetting passwords, locking and unlocking users, and showing communication. It also includes functions | src/service/include/PeopleServices.h                              |
| SubjectServices.h      | This code is a class called SubjectServices which provides functions to list all subjects, display one subject, display subject by name, add new subject and add student to subject. It is written by Akide Liu, Andrew Wang and Chi Wang on 24/9/20 and is released under the GNU General Public License.                                                                                   | src/service/include/SubjectServices.h                             |
| StudentServices.h      | This code is a class definition for StudentServices, which is a subclass of PeopleServices and PeopleCommunications. It contains functions to show subjects, show subjects enrolled by a user ID, and communicate with a user by their ID.                                                                                                                                                   | src/service/include/StudentServices.h                             |
| TeacherServices.h      | This code is a header file for a class called TeacherServices, which is a subclass of PeopleServices and PeopleCommunications. It contains functions to add new tutors, change user names, add new students, add new subjects, change subject names, show students, show tutors, show subjects, show subjects enrolled by ID, and communicate                                                | src/service/include/TeacherServices.h                             |
| PeopleCommunications.h | This code is a header file written by Akide Liu on 20/10/20 and is released under the GNU General Public License v3.0. It defines a class PeopleCommunications which provides a virtual function communicate() to communicate with people.                                                                                                                                                   | src/service/include/PeopleCommunications.h                        |
| TutorServices.h        | This code is a class definition for TutorServices, which is a subclass of PeopleServices and PeopleCommunications. It contains functions to change a user's name, add a new student, show students, show subjects, show subjects enrolled by a user, and communicate with a user.                                                                                                            | src/service/include/TutorServices.h                               |
| SERVICE_PUBLIC.h       | This code is a C++ header file for an Object- Oriented Programming project created by Akide Liu, Andrew Wang, and Chi Wang on 24/9/20. It includes the necessary libraries and header files for the project, such as PeopleServices.h, StudentServices.h, SubjectServices.h, TeacherServices.                                                                                                | src/service/include/SERVICE_PUBLIC.h                              |

</details>

<details closed><summary>Lib</summary>

| File               | Summary                                                                                                           | Module                                                                         |
|:-------------------|:------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| libmariadbclient.a | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libmariadbclient.a         |
| libcrypto.a        | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libcrypto.a                |
| libdate-tz.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libdate-tz.a               |
| libz.a             | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libz.a                     |
| libsqlpp-mysql.a   | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libsqlpp-mysql.a           |
| libmariadb.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libmariadb.a               |
| libssl.a           | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/libssl.a                   |
| libmariadbclient.a | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libmariadbclient.a   |
| libcrypto.a        | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libcrypto.a          |
| libdate-tz.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libdate-tz.a         |
| libz.a             | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libz.a               |
| libsqlpp-mysql.a   | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libsqlpp-mysql.a     |
| libmariadb.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libmariadb.a         |
| libssl.a           | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/libssl.a             |
| libmariadbclient.a | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libmariadbclient.a       |
| libcrypto.a        | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libcrypto.a              |
| libdate-tz.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libdate-tz.a             |
| libz.a             | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libz.a                   |
| libsqlpp-mysql.a   | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libsqlpp-mysql.a         |
| libmariadb.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libmariadb.a             |
| libssl.a           | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/libssl.a                 |
| libmariadbclient.a | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libmariadbclient.a |
| libcrypto.a        | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libcrypto.a        |
| libdate-tz.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libdate-tz.a       |
| libz.a             | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libz.a             |
| libsqlpp-mysql.a   | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libsqlpp-mysql.a   |
| libmariadb.a       | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libmariadb.a       |
| libssl.a           | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/libssl.a           |

</details>

<details closed><summary>Libmariadb</summary>

| File               | Summary                                                                                                                                                                                                                                                                                             | Module                                                                                |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| vcpkg_abi_info.txt | This code is a set of patches and files used to configure and build a CMake 3.17.2 project with features such as core, OpenSSL, and zlib. It includes patches to disable test builds, fix install paths, and post build checks, as well as files for porting, configuring, installing, and checking | utils/sqlpp11-connector-mysql/installed/x64-osx/share/libmariadb/vcpkg_abi_info.txt   |
| copyright          | Prompt too long to generate summary.                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/share/libmariadb/copyright            |
| vcpkg_abi_info.txt | This code is a set of patches and features for CMake 3.17.2, including core, OpenSSL, and Zlib. It includes patches to disable test builds, fix install paths, and post build checks. It also includes a triplet, vcpkg check features, vcpkg configure cmake, vcpkg                                | utils/sqlpp11-connector-mysql/installed/x64-linux/share/libmariadb/vcpkg_abi_info.txt |
| copyright          | Prompt too long to generate summary.                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/share/libmariadb/copyright          |

</details>

<details closed><summary>Mariadb</summary>

| File    | Summary                                                                                                                                                                                                                                  | Module                                                                          |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| ma_io.h | This code provides functions for opening, closing, reading, and getting data from files, either locally or remotely. It is part of the MariaDB Corporation AB copyright and is free to use under the GNU Library General Public License. | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb/ma_io.h   |
| ma_io.h | This code provides functions for opening, closing, reading, and getting data from files, either locally or remotely. It is copyright( C) 2015 MariaDB Corporation AB and is released under the GNU Library General Public License.       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb/ma_io.h |

</details>

<details closed><summary>Msbuild</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                | Module                                                                   |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| applocal.ps1  | This code is a PowerShell script that deploys binaries and their dependencies to a target directory. It resolves the base path of the target binary, checks if the binary is already present in the target directory, and if not, copies it from the source directory. It also checks for the presence of plugins and other dependencies, and copies them if necessary | utils/sqlpp11-connector-mysql/scripts/buildsystems/msbuild/applocal.ps1  |
| vcpkg.targets | This code is a Microsoft Build project that sets up the environment for using Vcpkg, a package manager for C and C++ libraries. It sets reasonable defaults, sets the OS and platform targets, and imports a property page for Vcpkg. It also checks for manifest files, installs dependencies, and sets up app local dependencies.                                    | utils/sqlpp11-connector-mysql/scripts/buildsystems/msbuild/vcpkg.targets |
| vcpkg.props   | This code sets up the default properties for a Microsoft Build project, including the VcpkgRoot, VcpkgConfiguration, VcpkgPageSchema, VcpkgOSTarget, VcpkgPlatformTarget, VcpkgUserTriplet, and VcpkgTriplet. It also sets up the VcpkgEnableMan                                                                                                                       | utils/sqlpp11-connector-mysql/scripts/buildsystems/msbuild/vcpkg.props   |

</details>

<details closed><summary>Mysql</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                                                                                                               | Module                                                                                       |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| ma_tls.h             | This code provides functions for initializing, connecting, reading, writing, and closing a secure socket layer( SSL) connection. It also provides functions for verifying server certificates, getting the cipher in use, getting the fingerprint of the server certificate, and getting the protocol version in use. It is used to provide secure communication between a MariaDB client             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/ma_tls.h                       |
| mariadb_ctype.h      | This code provides an implementation of the UNIX ctype(3) library, with additional functions for character set encoding and escaping. It includes functions for finding compiled character sets, escaping quotes and slashes, and getting the operating system character set.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_ctype.h                |
| mariadb_dyncol.h     | This code provides functions for creating and manipulating dynamic columns in MariaDB. It includes functions for creating and updating dynamic columns, checking if a column exists, listing columns, getting column values, and converting values to strings, longs, and doubles. It also includes functions for packing and unpacking dynamic columns, comparing column names, and counting columns | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_dyncol.h               |
| ma_pvio.h            | This code defines the interface for MariaDB's Protocol- VIO( PVIO) which provides an abstraction layer for different types of communication protocols. It includes functions for setting and getting timeouts, reading and writing data, connecting, and keeping the connection alive. It also defines constants for read ahead cache size, EINTR tries,                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/ma_pvio.h                      |
| mariadb_stmt.h       | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_stmt.h                 |
| ma_list.h            | This code provides a library of functions for manipulating a doubly- linked list data structure. It includes functions for adding, deleting, reversing, and walking through the list, as well as functions for calculating the length of the list and freeing the list.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/ma_list.h                      |
| mysql.h              | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mysql.h                        |
| mariadb_com.h        | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_com.h                  |
| mysqld_error.h       | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mysqld_error.h                 |
| mariadb_rpl.h        | This code is a library for MariaDB Corporation AB that provides replication functionality for MariaDB. It includes functions for initializing a replication handle, setting and getting options, opening and closing a replication handle, and fetching replication events. It also includes structures for different types of replication events, such as rotate, query, GTID list, format           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_rpl.h                  |
| mariadb_version.h    | This code defines version numbers and other information for the MariaDB database management system. It includes the protocol version, client version string, base version, port, unix address, configuration name, server version, package version, system type, machine type, and plugin directory.                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mariadb_version.h              |
| errmsg.h             | This code provides error messages for MySQL clients and MariaDB Connector / C. It includes functions to initialize client errors, an array of client errors, and an array of MariaDB client errors. It also defines error codes for various errors, such as connection errors, socket errors, and authentication errors.                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/errmsg.h                       |
| plugin_auth_common.h | This code defines constants and data structures for client- and server- side authentication plugins. It includes constants for the maximum allowed length for a user name, return values for the plugin authenticate_user() method, and a structure for providing plugin access to communication channels.                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mysql/plugin_auth_common.h     |
| plugin_auth.h        | This code defines constants and data structures for client- and server- side authentication plugins. It includes the max allowed length for a user name, return values of the plugin authenticate_user() method, and a struct for providing plugin access to communication channel.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mysql/plugin_auth.h            |
| client_plugin.h      | This code defines the API for plugins that work on the client side. It includes declarations for authentication, communication IO, trace, and connection plugins. It also includes functions for loading, finding, and registering plugins.                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/mysql/mysql/client_plugin.h          |
| connection.h         | This code provides a class for creating a connection to a MySQL database. It includes functions for executing SQL statements, preparing statements, and managing transactions. It also provides a serializer for escaping strings.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/connection.h           |
| connection_config.h  | This code defines a struct for a MySQL connection configuration, including parameters such as host, user, password, database, port, unix_socket, client_flag, charset, auto_reconnect, and debug. It also provides an operator to compare two connection configurations.                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/connection_config.h    |
| bind_result.h        | This code provides a class for binding results from a MySQL prepared statement. It includes functions for binding different types of data, such as booleans, floating points, integers, and text, as well as functions for post- binding data.                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/bind_result.h          |
| char_result.h        | This code is a header file for a char_result_t class in the SQLPP library for MySQL. It provides functions for binding data from a MySQL result set to variables, and a next() function to iterate through the result set.                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/char_result.h          |
| serializer.h         | This code is a serializer for the MySQL database which provides support for the concat and insert_default_values_data data types. It allows for the concatenation of multiple values and the insertion of default values into the database.                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/serializer.h           |
| char_result_row.h    | This code defines a struct called char_result_row_t which contains two members, data and len, both of which are pointers. It also contains an operator== function which compares two char_result_row_t objects.                                                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/char_result_row.h      |
| mysql.h              | This code provides the necessary components to connect to a MySQL database and retrieve character results. It is copyright( c) 2013- 2015, Roland Bock and is distributed under the terms of the BSD license.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/mysql.h                |
| prepared_statement.h | This code is a header file for a prepared_statement_t class in the sqlpp::mysql namespace. It provides functions for binding parameters to the statement, and is used to create a prepared statement for a MySQL database connection.                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/mysql/prepared_statement.h   |
| ma_tls.h             | This code provides functions for secure connections using TLS / SSL. It defines enumerations, constants, and structures for the TLS / SSL connection, as well as functions for initializing, connecting, reading, writing, and closing the connection, and for verifying the server certificate. It also provides functions for getting the cipher, fingerprint, and protocol version                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/ma_tls.h                     |
| mariadb_ctype.h      | This code provides an implementation of the UNIX ctype(3) library, with additional functions for character set encoding and escaping. It includes functions for finding compiled character sets, escaping quotes and slashes, and getting the operating system character set.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_ctype.h              |
| mariadb_dyncol.h     | This code provides functions for creating and manipulating dynamic columns in MariaDB. It includes functions for creating and updating dynamic columns, checking if a column exists, listing columns, getting column values, and converting values to strings, longs, and doubles. It also includes functions for packing and unpacking dynamic columns, comparing column names, and counting columns | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_dyncol.h             |
| ma_pvio.h            | This code defines the interface for MariaDB's Protocol- VIO( PVIO) which provides an abstraction layer for different types of communication protocols. It includes functions for setting and getting timeouts, reading and writing data, connecting, and keeping the connection alive. It also defines constants for read ahead cache size, EINTR tries,                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/ma_pvio.h                    |
| mariadb_stmt.h       | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_stmt.h               |
| ma_list.h            | This code provides a library of functions for manipulating a doubly- linked list data structure. It includes functions for adding, deleting, reversing, and walking through the list, as well as functions for calculating the length of the list and freeing the list.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/ma_list.h                    |
| mysql.h              | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mysql.h                      |
| mariadb_com.h        | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_com.h                |
| mysqld_error.h       | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mysqld_error.h               |
| mariadb_rpl.h        | This code is a library for MariaDB Corporation AB that provides replication functionality for MariaDB. It includes functions for initializing a replication handle, setting and getting options, opening and closing a replication handle, and fetching replication events. It also includes structures for different types of replication events, such as rotate, query, GTID list, format           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_rpl.h                |
| mariadb_version.h    | This code defines version numbers and other information for the MariaDB database management system. It includes the protocol version, client version string, base version, port, unix address, configuration name, server version, package version, system type, machine type, and plugin directory.                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mariadb_version.h            |
| errmsg.h             | This code provides error messages for MySQL clients and MariaDB Connector / C. It includes functions to initialize client errors, an array of client errors, and an array of MariaDB client errors. It also defines error codes for various errors, such as connection errors, socket errors, and authentication errors.                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/errmsg.h                     |
| plugin_auth_common.h | This code defines constants and data structures for client- and server- side authentication plugins. It includes constants for the maximum user name length, return values for the authenticate_user() method, and structures for plugin access to communication channels.                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mysql/plugin_auth_common.h   |
| plugin_auth.h        | This code defines constants and data structures for client- and server- side authentication plugins. It includes the max allowed length for a user name, return values of the plugin authenticate_user() method, and a struct for providing plugin access to communication channel.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mysql/plugin_auth.h          |
| client_plugin.h      | This code defines the API for plugins that work on the client side. It includes declarations for authentication, communication IO, trace, and connection plugins. It also includes functions for loading and registering plugins.                                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/mysql/mysql/client_plugin.h        |
| connection.h         | This code provides a class for creating a connection to a MySQL database. It includes functions for executing SQL statements, preparing statements, and managing transactions. It also provides a serializer for escaping strings.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/connection.h         |
| connection_config.h  | This code defines a struct for a MySQL connection configuration, including parameters such as host, user, password, database, port, unix_socket, client_flag, charset, auto_reconnect, and debug. It also provides an operator to compare two connection configurations.                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/connection_config.h  |
| bind_result.h        | This code provides a class for binding results from a MySQL prepared statement. It includes functions for binding different types of data, such as booleans, floating points, integers, and text, as well as functions for post- binding data.                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/bind_result.h        |
| char_result.h        | This code is a header file for a char_result_t class in the SQLPP library for MySQL. It provides functions for binding data from a MySQL result set to variables, and a next() function to iterate through the result set.                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/char_result.h        |
| serializer.h         | This code is a serializer for the MySQL database system, providing support for the CONCAT and INSERT DEFAULT VALUES data types. It allows for the serialization of these data types into the MySQL database system.                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/serializer.h         |
| char_result_row.h    | This code defines a struct called char_result_row_t which contains two members, data and len, both of which are pointers. It also contains an operator== function which compares two char_result_row_t objects. This code is part of the SQLPP library for MySQL.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/char_result_row.h    |
| mysql.h              | This code provides the necessary components to connect to a MySQL database and retrieve character results. It is copyright( c) 2013- 2015, Roland Bock and is distributed under the terms of the BSD license.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/mysql.h              |
| prepared_statement.h | This code is a header file for a prepared statement class for the MySQL database. It provides functions for binding parameters to the statement, such as booleans, integers, floating points, strings, dates, and date- times. It is copyright( c) 2013- 2015, Roland Bock and is protected by the BSD 3-                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/mysql/prepared_statement.h |

</details>

<details closed><summary>Openssl</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module                                                                                    |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| pem2.h                    | This code is a header file for the OpenSSL Project, which provides a secure cryptographic library. It includes the PEM2 header file and the PEMERR header file, which are used to provide secure encryption and authentication services.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pem2.h                    |
| kdf.h                     | This code is a header file for the OpenSSL Project, which provides a set of functions for deriving keys from passwords. It includes functions for TLS, HKDF, and SCRYPT, which are used to generate secure keys from passwords.                                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/kdf.h                     |
| pem.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pem.h                     |
| asyncerr.h                | This code is a header file for the OpenSSL library which contains definitions for function codes and reason codes related to the ASYNC module. It also includes a function to load the ASYNC strings.                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/asyncerr.h                |
| md2.h                     | This code provides an implementation of the MD2 cryptographic hash function. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash directly. It also includes a constant for the length of the hash and a structure for the MD2 context.                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/md2.h                     |
| ssl3.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ssl3.h                    |
| ossl_typ.h                | This code defines various data types used by the OpenSSL library, such as ASN1_INTEGER, BIGNUM, EVP_CIPHER, X509, and RSA. It also includes functions for parsing arguments, such as ossl_intmax_t and ossl_uintmax_t.                                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ossl_typ.h                |
| dtls1.h                   | This code is a header file for the OpenSSL Project, which provides cryptographic functions for secure communication. It defines constants related to the DTLS protocol, such as the version numbers, header lengths, and timeout multipliers.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/dtls1.h                   |
| err.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/err.h                     |
| bn.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/bn.h                      |
| blowfish.h                | This code is a header file for the Blowfish encryption algorithm. It includes functions for setting a key, encrypting and decrypting data, and other encryption methods such as ECB, CBC, CFB64, and OFB64. It also includes a function for displaying options.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/blowfish.h                |
| cms.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cms.h                     |
| engine.h                  | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/engine.h                  |
| conf_api.h                | This code provides functions for working with OpenSSL configuration files. It includes functions for creating and accessing sections, adding strings, getting strings and numbers, and creating and freeing data.                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/conf_api.h                |
| x509.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/x509.h                    |
| asn1_mac.h                | This code is a copyright notice for the OpenSSL Project Authors, and is a warning that the file is obsolete and should be updated.                                                                                                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/asn1_mac.h                |
| objectserr.h              | This code is a header file for the OpenSSL library which contains functions and reason codes related to the OBJ module. It provides functions such as OBJ_F_OBJ_ADD_OBJECT, OBJ_F_OBJ_ADD_SIGID, OBJ_F_OBJ_CREATE, OB                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/objectserr.h              |
| cmserr.h                  | This code is part of the OpenSSL library and provides functions and reason codes for the Cryptographic Message Syntax( CMS) module. It includes functions for creating, signing, encrypting, decrypting, and verifying CMS messages, as well as functions for managing certificates and keys. It also includes error codes for when something goes wrong.                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cmserr.h                  |
| ui.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ui.h                      |
| sha.h                     | This code provides functions for computing SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 cryptographic hash values. It includes functions for initializing, updating, and finalizing the hash values, as well as functions for computing the hash values directly from data. It also defines the SHA_CTX,                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/sha.h                     |
| symhacks.h                | This code is a header file for OpenSSL which provides a workaround for case insensitive linking issues on the VMS operating system. It defines macros to rename certain functions and data structures to avoid conflicts.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/symhacks.h                |
| asn1.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/asn1.h                    |
| bioerr.h                  | This code is a header file for the OpenSSL library, containing definitions for BIO function codes and reason codes. It is used to generate error messages for the library.                                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/bioerr.h                  |
| opensslconf.h             | This code is a generated file from include / openssl / opensslconf.h.in and is used to configure OpenSSL with various options such as disabling certain algorithms, enabling threads, and setting the minimum API compatibility. It also contains definitions for various constants and functions.                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/opensslconf.h             |
| bio.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/bio.h                     |
| rc2.h                     | This code provides functions for encrypting and decrypting data using the RC2 algorithm. It includes functions for setting the key, encrypting and decrypting data in ECB, CBC, CFB64, and OFB64 modes. It also defines constants for the block size, key length, and encryption / decryption modes.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rc2.h                     |
| dh.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/dh.h                      |
| __DECC_INCLUDE_PROLOGUE.H | This code is a file used by HP C / C++ on VMS, which is included automatically after each header file from the same directory. It contains pragmas that save the state and shorten symbols larger than 31 characters to 23 characters followed by an 8 hex character CRC.                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/__DECC_INCLUDE_PROLOGUE.H |
| x509v3.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/x509v3.h                  |
| conf.h                    | This code provides functions for loading and manipulating configuration files. It includes functions for creating and initializing a configuration object, loading a configuration file, accessing and manipulating configuration values, and dumping a configuration object to a file or BIO. It also provides functions for loading and unloading modules, and for setting and getting user data. | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/conf.h                    |
| rand_drbg.h               | This code is a header file for the OpenSSL Project's Deterministic Random Bit Generator( DRBG). It contains functions for creating, setting, and using the DRBG, as well as functions for setting the default security strength, type, and flags. It also contains callback functions for getting entropy and nonce values.                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rand_drbg.h               |
| __DECC_INCLUDE_EPILOGUE.H | This code is a file used by HP C / C++ on VMS which is included automatically after each header file from the same directory. It restores the state of the compiler and prevents the C++ compiler from understanding certain pragmas, even though it understands the corresponding command line qualifier.                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/__DECC_INCLUDE_EPILOGUE.H |
| md5.h                     | This code provides an implementation of the MD5 cryptographic hash function. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash directly. It also defines the MD5_CTX structure, which is used to store the state of the hash.                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/md5.h                     |
| pemerr.h                  | This code is a header file for the OpenSSL library which contains definitions for PEM function codes and reason codes. It also contains the function ERR_load_PEM_strings() which is used to load the PEM error strings into the error table.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pemerr.h                  |
| x509_vfy.h                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/x509_vfy.h                |
| txt_db.h                  | This code provides functions for creating, reading, writing, and manipulating a text database( TXT_DB). It includes functions for creating an index, inserting data, and retrieving data by index. It also defines constants for errors that may occur when manipulating the database.                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/txt_db.h                  |
| comperr.h                 | This code is a header file for the OpenSSL library which provides functions and reason codes for compression. It includes functions such as BIO_ZLIB_FLUSH, BIO_ZLIB_NEW, BIO_ZLIB_READ, BIO_ZLIB_WRITE, and COMP_CTX_NEW, as                                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/comperr.h                 |
| cterr.h                   | This code is a header file for the Certificate Transparency( CT) library in OpenSSL. It contains function codes and reason codes for the CT library, as well as a function to load CT strings. It is used to provide support for the CT library in OpenSSL.                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cterr.h                   |
| safestack.h               | This code provides macros for creating and manipulating stacks of various types, such as strings, blocks of characters, and other types. It includes functions for creating, deleting, sorting, and copying stacks, as well as functions for manipulating the elements of the stack.                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/safestack.h               |
| ecdsa.h                   | This code is a header file for OpenSSL's EC library, which provides cryptographic functions for elliptic curves. It is copyright 2002- 2016 The OpenSSL Project Authors and is licensed under the OpenSSL license.                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ecdsa.h                   |
| sslerr.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/sslerr.h                  |
| rc5.h                     | This code is a header file for the RC5 encryption algorithm. It provides functions for setting the key, encrypting and decrypting data, and encrypting and decrypting data in CBC, CFB, and OFB modes. It supports RC5- 32/12/16 and RC5- 32/16/8 modes.                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rc5.h                     |
| uierr.h                   | This code is part of OpenSSL and provides functions and reason codes for user interface( UI) operations. It includes functions for opening and closing the console, echoing and no- echoing the console, creating methods, controlling the UI, duplicating strings, setting and getting results, and allocating booleans and prompts. It also includes                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/uierr.h                   |
| x509v3err.h               | This code is a header file for X509V3, which is a part of the OpenSSL Project. It contains function codes and reason codes for X509V3, which are used to generate errors.                                                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/x509v3err.h               |
| objects.h                 | This code provides functions for managing OpenSSL objects, such as creating, adding, and removing objects, as well as searching for objects. It also provides functions for finding signature algorithms and adding signature identifiers.                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/objects.h                 |
| pkcs12.h                  | This code provides functions for creating, parsing, and manipulating PKCS12 objects, which are used for secure data transfer. It includes functions for creating and decrypting PKCS12 safebags, adding friendly names, setting key usage, and generating and verifying MACs. It also provides functions for converting between ASCII and Unicode strings.                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pkcs12.h                  |
| crypto.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/crypto.h                  |
| opensslv.h                | This code is part of the OpenSSL Project and is used to define the version number and version history of the OpenSSL library. It also defines the version number and version history of the shared library.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/opensslv.h                |
| evperr.h                  | This code is the header file for the OpenSSL library's EVP error codes and function codes. It contains definitions for error codes and function codes related to encryption, decryption, key generation, and other cryptographic operations.                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/evperr.h                  |
| pkcs7.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pkcs7.h                   |
| obj_mac.h                 | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/obj_mac.h                 |
| ct.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ct.h                      |
| async.h                   | This code provides an API for asynchronous job execution and management. It includes functions for creating and managing jobs, setting and getting file descriptors, and pausing and resuming jobs. It also provides functions for initializing and cleaning up threads.                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/async.h                   |
| buffer.h                  | This code provides functions for creating and managing a buffer memory structure, which is used to store data in a secure manner. It includes functions for creating a new buffer memory structure, freeing it, growing it, and reversing the data stored in it. It also provides macros for duplicating strings and copying strings.                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/buffer.h                  |
| ssl.h                     | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ssl.h                     |
| srp.h                     | This code is a header file for the OpenSSL Project's SRP library, which provides functions for creating and verifying SRP verifiers and calculating client and server keys. It includes functions for creating and managing SRP user passwords, as well as functions for verifying A and B mod N. It also defines constants for SRP parameters and status                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/srp.h                     |
| camellia.h                | This code is a header file for the OpenSSL library, which provides an implementation of the Camellia encryption algorithm. It includes functions for setting a key, encrypting and decrypting data, and various modes of operation such as ECB, CBC, CFB, OFB, and CTR.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/camellia.h                |
| dherr.h                   | This code is a header file for the OpenSSL library, which provides functions for Diffie- Hellman key exchange. It contains definitions for various functions and error codes related to Diffie- Hellman key exchange.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/dherr.h                   |
| evp.h                     | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/evp.h                     |
| e_os2.h                   | This header file provides macros to detect operating systems and define global variables for use in OpenSSL. It also provides macros for I / O and exit functions, as well as standard integer types and attributes for use in public headers.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/e_os2.h                   |
| md4.h                     | This code provides an implementation of the MD4 cryptographic hash algorithm. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash of a given data set. It also defines the MD4_CTX structure, which is used to store the state of the hash computation.                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/md4.h                     |
| hmac.h                    | This code provides functions for creating and using HMAC( Hash- based Message Authentication Code) in OpenSSL. It includes functions for creating a new HMAC context, resetting an existing context, updating the context with data, and finalizing the context to generate the HMAC. It also provides a function for copying an existing context and setting                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/hmac.h                    |
| aes.h                     | This code provides an implementation of the Advanced Encryption Standard( AES) algorithm. It includes functions for encryption and decryption, as well as functions for key generation and wrapping / unwrapping. It also provides support for various modes of operation, such as ECB, CBC, CFB, OFB, and IGE.                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/aes.h                     |
| engineerr.h               | This code is a header file for the OpenSSL library which contains definitions for various functions and reason codes related to the ENGINE module. It also includes the ERR_load_ENGINE_strings() function which is used to load the ENGINE error strings into the error table.                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/engineerr.h               |
| comp.h                    | This code provides functions for compression and decompression using the OpenSSL library. It includes functions for creating and freeing a compression context, getting the type and name of a compression method, and compressing and decompressing blocks of data. It also provides a function for getting the zlib compression method. Finally, it provides a function for getting the           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/comp.h                    |
| pkcs12err.h               | This file is a header file for the OpenSSL library which contains error codes and function codes related to the PKCS12 module. It also contains functions for creating and verifying MACs, encrypting and decrypting data, and setting up and verifying authentication.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pkcs12err.h               |
| cast.h                    | This code is a header file for the CAST encryption algorithm, which is used to encrypt and decrypt data. It includes functions for setting the key, encrypting and decrypting data, and encrypting and decrypting data using the CBC, CFB, and OFB modes. It also defines constants for the block size and key length.                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cast.h                    |
| rc4.h                     | This code provides an implementation of the RC4 encryption algorithm. It includes functions to set a key, encrypt data, and obtain options for the algorithm. It is licensed under the OpenSSL license.                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rc4.h                     |
| stack.h                   | This code provides functions for creating and manipulating a stack data structure. It includes functions for creating a stack, adding and removing elements, sorting, and finding elements. It also provides functions for freeing and copying the stack.                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/stack.h                   |
| des.h                     | This code is a header file for the OpenSSL library, which provides encryption and decryption functions for data. It includes functions for DES encryption, such as DES_ecb2_encrypt, DES_cbc_encrypt, DES_cfb_encrypt, and DES_ofb_encrypt, as well as                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/des.h                     |
| ocsp.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ocsp.h                    |
| ec.h                      | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ec.h                      |
| ecdh.h                    | This code is a header file for OpenSSL's EC library, which provides cryptographic functions for elliptic curves. It is copyright 2002- 2016 The OpenSSL Project Authors and is licensed under the OpenSSL license.                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ecdh.h                    |
| rand.h                    | This code is a header file for the OpenSSL library, which provides functions for generating random numbers. It includes functions for setting and getting the random number method, generating random bytes, seeding, adding randomness, and checking the status of the random number generator.                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rand.h                    |
| ecerr.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ecerr.h                   |
| ts.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ts.h                      |
| cryptoerr.h               | This code is a header file for the OpenSSL library which contains function and reason codes for the CRYPTO module. It includes functions such as CRYPTO_F_CMAC_CTX_NEW, CRYPTO_F_CRYPTO_DUP_EX_DATA, and CRYPTO_F_CR                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cryptoerr.h               |
| storeerr.h                | This code is a header file for the OpenSSL Store library, which provides functions for loading and searching for certificates, CRLs, keys, and names. It contains function codes and reason codes for errors that may occur when using the library.                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/storeerr.h                |
| buffererr.h               | This code is a header file for the OpenSSL library which contains function and reason codes for the BUF module. It is used to generate error messages and is not meant to be edited.                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/buffererr.h               |
| seed.h                    | This code is a header file for the SEED encryption algorithm, which is used to encrypt and decrypt data. It includes functions for setting the key, encrypting and decrypting data, and functions for encrypting and decrypting data using the ECB, CBC, CFB128, and OFB128 modes. It is licensed under the Open                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/seed.h                    |
| modes.h                   | This code provides functions for encryption and decryption using various modes, such as CBC, CTR, CCM, GCM, XTS, and OCB. It also provides functions for wrapping and unwrapping data, as well as setting IVs and tags.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/modes.h                   |
| ssl2.h                    | This code is a header file for the OpenSSL Project, which provides a secure communications layer over the internet. It defines the SSL2 version and the client hello message type.                                                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ssl2.h                    |
| tserr.h                   | This code is a header file for the OpenSSL library which contains definitions for functions and reason codes related to the Time Stamp Protocol( TSP). It is used to generate error messages and verify the validity of time stamps.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/tserr.h                   |
| rsa.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rsa.h                     |
| ripemd.h                  | This code provides an implementation of the RIPEMD-160 cryptographic hash function. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash directly. It also defines the RIPEMD160_CTX structure, which is used to store the intermediate state of the hash computation.                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ripemd.h                  |
| whrlpool.h                | This code is a header file for the Whirlpool cryptographic hash function. It provides functions for initializing, updating, and finalizing the hash, as well as a one- step function for hashing data. The Whirlpool hash has a digest length of 512 bits and a block size of 512 bits.                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/whrlpool.h                |
| tls1.h                    | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/tls1.h                    |
| rsaerr.h                  | This code is a header file for the RSA error codes and functions used in OpenSSL. It contains definitions for various RSA functions and reason codes, such as RSA_F_RSA_SIGN, RSA_R_WRONG_SIGNATURE_LENGTH, and RSA_F_RSA_VERIFY_PKCS1                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/rsaerr.h                  |
| randerr.h                 | This code is a header file for the OpenSSL Project which contains definitions for function codes and reason codes related to the RAND module. It also includes the ERR_load_RAND_strings() function which is used to load the RAND error strings into the error table.                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/randerr.h                 |
| mdc2.h                    | This code is a header file for the MDC2 cryptographic hash function. It provides functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash in one step. It also defines constants for the block size and digest length of the hash.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/mdc2.h                    |
| ocsperr.h                 | This code is a header file for OpenSSL's OCSP( Online Certificate Status Protocol) error codes and function codes. It contains error codes such as OCSP_R_CERTIFICATE_VERIFY_ERROR and function codes such as OCSP_F_OCSP_BASIC_VERIFY. It is                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ocsperr.h                 |
| x509err.h                 | This code is the header file for X509 errors and functions. It contains definitions for X509 function codes and reason codes, as well as the function ERR_load_X509_strings() which is used to load X509 error strings.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/x509err.h                 |
| pkcs7err.h                | This code is a header file for the OpenSSL library which contains the function codes and reason codes for the PKCS7 module. It is used to generate error messages for the PKCS7 module.                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/pkcs7err.h                |
| dsa.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/dsa.h                     |
| kdferr.h                  | This code is a header file for the OpenSSL KDF( Key Derivation Function) library. It contains function codes and reason codes for the KDF library, as well as a function to load the KDF strings.                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/kdferr.h                  |
| srtp.h                    | This code provides an implementation of the Secure Real- Time Transport Protocol( SRTP) for OpenSSL. It includes functions for setting and getting SRTP profiles, as well as constants for various SRTP protection profiles.                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/srtp.h                    |
| asn1t.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/asn1t.h                   |
| dsaerr.h                  | This code is part of OpenSSL and provides functions and reason codes for the DSA algorithm. It includes functions such as DSA_F_DSA_DO_SIGN, DSA_F_DSA_DO_VERIFY, and DSA_F_DSA_METH_NEW, as well as reason                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/dsaerr.h                  |
| bnerr.h                   | This code is a header file for the OpenSSL library, containing definitions for BN function codes and BN reason codes. It is used to generate error messages for the library.                                                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/bnerr.h                   |
| conferr.h                 | This code is a header file for the OpenSSL library which contains constants and functions related to the configuration of the library. It includes codes for functions such as CONF_F_CONF_LOAD, CONF_F_NCONF_GET_STRING, and CONF_F_SSL_MODULE_INIT                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/conferr.h                 |
| cmac.h                    | This code provides functions for the implementation of the Cipher- based Message Authentication Code( CMAC) algorithm. It includes functions for creating and managing CMAC contexts, copying contexts, initializing and finalizing CMAC operations, and resuming operations. It is subject to the OpenSSL license.                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/cmac.h                    |
| ebcdic.h                  | This code provides functions for converting between ASCII and EBCDIC character sets. It includes functions for os_toascii, os_toebcdic, ebcdic2ascii, and ascii2ebcdic, as well as constants for each character set. It is covered by the OpenSSL license                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/ebcdic.h                  |
| store.h                   | This code provides functions for opening a channel to a resource with supported data( keys, certs, crls, etc.), reading the data a piece at a time, and closing the channel. It also provides functions for extracting OpenSSL types from and creating new OSSL_STORE_INFOs, constructing a search URI from a base URI                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/store.h                   |
| idea.h                    | This code is a header file for the IDEA encryption algorithm. It provides functions for encrypting and decrypting data using the IDEA algorithm, as well as functions for setting encryption and decryption keys. It also provides functions for encrypting data using the IDEA algorithm in ECB, CBC, CFB64, and OFB64 modes                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/idea.h                    |
| lhash.h                   | This header file provides type- safe wrappers for dynamic hash table routines written by Eric Young. It includes functions for creating and freeing a hash table, inserting, deleting, and retrieving data, and various other functions for managing the hash table.                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/lhash.h                   |
| asn1err.h                 | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/openssl/asn1err.h                 |
| usage                     | This code enables the use of the OpenSSL package with CMake targets. It finds the OpenSSL package and links it to the main target, allowing the use of OpenSSL's SSL and Crypto libraries.                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/share/openssl/usage                       |
| vcpkg_abi_info.txt        | This code is for CMake 3.17.2, a cross- platform, open- source build system. It features core components, OpenSSL- Unix, Portfile.cmake, post- build checks, and triplet usage. It is identified by the unique identifier CONTROL 6053e838eb89ae1b                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/share/openssl/vcpkg_abi_info.txt          |
| vcpkg-cmake-wrapper.cmake | This code finds the OpenSSL package and library, and adds the dynamic library and thread library to the list of OpenSSL libraries. It also sets the property of the OpenSSL::Crypto and OpenSSL::SSL targets to link the thread library.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/share/openssl/vcpkg-cmake-wrapper.cmake   |
| pem2.h                    | This code is a header file for the OpenSSL Project, which provides a secure cryptographic library. It includes the PEM2 header file and the PEMERR header file, which are used to provide secure encryption and authentication services.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pem2.h                  |
| kdf.h                     | This code is a header file for the OpenSSL Project, which provides a set of functions for deriving keys from passwords. It includes functions for TLS, HKDF, and SCRYPT, which are used to generate secure keys from passwords.                                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/kdf.h                   |
| pem.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pem.h                   |
| asyncerr.h                | This code is a header file for the OpenSSL library which contains definitions for function codes and reason codes related to the ASYNC module. It also includes a function to load the ASYNC strings.                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/asyncerr.h              |
| md2.h                     | This code provides an implementation of the MD2 cryptographic hash function. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash directly. It also includes a constant for the length of the hash and a structure for the MD2 context.                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/md2.h                   |
| ssl3.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ssl3.h                  |
| ossl_typ.h                | This code is a header file for OpenSSL, which defines various types used in the OpenSSL library, such as ASN1_INTEGER, BIGNUM, EVP_CIPHER, X509, and RSA. It also includes functions for parsing arguments, such as ossl_intmax_t and ossl                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ossl_typ.h              |
| dtls1.h                   | This code is a header file for the OpenSSL Project, which provides cryptographic functions for secure communication. It defines constants related to the DTLS protocol, such as the version numbers, header lengths, and timeout multipliers.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/dtls1.h                 |
| err.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/err.h                   |
| bn.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/bn.h                    |
| blowfish.h                | This code is a header file for the Blowfish encryption algorithm. It includes functions for setting a key, encrypting and decrypting data, and other encryption methods such as ECB, CBC, CFB64, and OFB64. It also includes a function for displaying options.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/blowfish.h              |
| cms.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cms.h                   |
| engine.h                  | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/engine.h                |
| conf_api.h                | This code provides functions for working with OpenSSL configuration files. It includes functions for creating and accessing sections, adding strings, getting strings and numbers, and creating and freeing data.                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/conf_api.h              |
| x509.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/x509.h                  |
| asn1_mac.h                | This code is a copyright notice for the OpenSSL Project Authors, and is a warning that the file is obsolete and should be updated.                                                                                                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/asn1_mac.h              |
| objectserr.h              | This code is a header file for the OpenSSL library which contains functions and reason codes related to the OBJ module. It provides functions such as OBJ_F_OBJ_ADD_OBJECT, OBJ_F_OBJ_ADD_SIGID, OBJ_F_OBJ_CREATE, OB                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/objectserr.h            |
| cmserr.h                  | This code is part of the OpenSSL library and provides functions and reason codes for the Cryptographic Message Syntax( CMS) module. It includes functions for creating, signing, encrypting, decrypting, and verifying CMS messages, as well as functions for managing certificates and keys. It also includes error codes for when something goes wrong.                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cmserr.h                |
| ui.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ui.h                    |
| sha.h                     | This code provides functions for computing SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 cryptographic hash values. It includes functions for initializing, updating, and finalizing the hash values, as well as functions for computing the hash values directly from data. It also defines the SHA_CTX,                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/sha.h                   |
| symhacks.h                | This code is a header file for OpenSSL which provides a workaround for case insensitive linking issues on the VMS operating system. It defines macros to rename certain functions and data structures to avoid conflicts.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/symhacks.h              |
| asn1.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/asn1.h                  |
| bioerr.h                  | This code is a header file for the OpenSSL library, containing definitions for BIO function codes and reason codes. It is used to generate error messages for the library.                                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/bioerr.h                |
| opensslconf.h             | This code is a generated file from include / openssl / opensslconf.h.in and is used to configure OpenSSL with various options. It defines constants for various algorithms, threading, and debugging, as well as functions that are deprecated in certain versions of OpenSSL.                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/opensslconf.h           |
| bio.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/bio.h                   |
| rc2.h                     | This code is a header file for the RC2 encryption algorithm. It provides functions for setting the key, encrypting and decrypting data, and encrypting and decrypting data in CBC, CFB, and OFB modes. It is subject to the OpenSSL license.                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rc2.h                   |
| dh.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/dh.h                    |
| x509v3.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/x509v3.h                |
| conf.h                    | This code provides functions for loading and manipulating configuration files. It includes functions for creating and initializing a configuration object, loading a configuration file, accessing and manipulating configuration values, and dumping a configuration object to a file or BIO. It also provides functions for loading and unloading modules, and for setting and getting user data. | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/conf.h                  |
| rand_drbg.h               | This code provides functions for the OpenSSL Random Number Generator( RAND_DRBG) to generate random numbers securely. It includes functions for setting the default security strength, type, and flags, as well as functions for instantiating, reseeding, and generating random numbers. It also includes functions for setting and getting external data, and setting                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rand_drbg.h             |
| md5.h                     | This code provides an implementation of the MD5 cryptographic hash function. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash of a given data set. It also defines the MD5_CTX structure, which is used to store the state of the hash computation.                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/md5.h                   |
| pemerr.h                  | This code is a header file for the OpenSSL library which contains definitions for PEM function codes and reason codes. It also contains the function ERR_load_PEM_strings() which is used to load the PEM error strings into the error table.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pemerr.h                |
| x509_vfy.h                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/x509_vfy.h              |
| txt_db.h                  | This code provides functions for creating, reading, writing, and manipulating a text database( TXT_DB). It includes functions for creating an index, inserting data, and retrieving data by index. It also defines constants for errors that may occur when manipulating the database.                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/txt_db.h                |
| comperr.h                 | This code is a header file for the OpenSSL library which provides functions and reason codes for compression. It includes functions such as BIO_ZLIB_FLUSH, BIO_ZLIB_NEW, BIO_ZLIB_READ, BIO_ZLIB_WRITE, and COMP_CTX_NEW, as                                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/comperr.h               |
| cterr.h                   | This code is a header file for the Certificate Transparency( CT) library in OpenSSL. It contains function codes and reason codes for the CT library, as well as a function to load CT strings. It is used to provide support for the CT library in OpenSSL.                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cterr.h                 |
| safestack.h               | This code provides macros for creating and manipulating stacks of various types, such as strings, blocks of characters, and other types. It includes functions for creating, deleting, sorting, and copying stacks, as well as functions for manipulating the elements of the stack.                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/safestack.h             |
| ecdsa.h                   | This code is a header file for OpenSSL's EC library, which provides cryptographic functions for elliptic curves. It is copyright 2002- 2016 The OpenSSL Project Authors and is licensed under the OpenSSL license.                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ecdsa.h                 |
| sslerr.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/sslerr.h                |
| rc5.h                     | This code is a header file for the RC5 encryption algorithm. It provides functions for setting the key, encrypting and decrypting data, and encrypting and decrypting data in CBC, CFB, and OFB modes. It supports RC5- 32/12/16 and RC5- 32/16/8 modes.                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rc5.h                   |
| uierr.h                   | This code is part of OpenSSL and provides functions and reason codes for user interface( UI) operations. It includes functions for opening and closing the console, echoing and no- echoing the console, creating methods, controlling the UI, duplicating strings, setting and getting results, and allocating booleans and prompts. It also includes                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/uierr.h                 |
| x509v3err.h               | This code is a header file for X509V3, which is a part of the OpenSSL Project. It contains function codes and reason codes for X509V3, which are used to generate errors.                                                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/x509v3err.h             |
| objects.h                 | This code provides functions for managing OpenSSL objects, such as creating, adding, and removing objects, as well as searching for objects. It also provides functions for finding signature algorithms and adding signature identifiers.                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/objects.h               |
| pkcs12.h                  | This code provides functions for creating, parsing, and manipulating PKCS12 objects, which are used for secure data transfer. It includes functions for creating and decrypting PKCS12 safebags, adding friendly names, setting key usage, and generating and verifying MACs. It also provides functions for converting between ASCII and Unicode strings.                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pkcs12.h                |
| crypto.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/crypto.h                |
| opensslv.h                | This code is part of the OpenSSL Project and is used to define the version number and version history of the OpenSSL library. It also defines the version number and version history of the shared library.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/opensslv.h              |
| evperr.h                  | This code is the header file for the OpenSSL library's EVP error codes and function codes. It contains definitions for error codes and function codes related to encryption, decryption, key generation, and other cryptographic operations.                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/evperr.h                |
| pkcs7.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pkcs7.h                 |
| obj_mac.h                 | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/obj_mac.h               |
| ct.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ct.h                    |
| async.h                   | This code provides an API for asynchronous job execution and management. It includes functions for creating and managing jobs, setting and getting file descriptors, and pausing and resuming jobs. It also provides functions for initializing and cleaning up threads.                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/async.h                 |
| buffer.h                  | This code provides functions for creating and managing a buffer memory structure, which is used to store data in a secure manner. It includes functions for creating a new buffer memory structure, freeing it, growing it, and reversing the data stored in it. It also provides macros for duplicating strings and copying strings.                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/buffer.h                |
| ssl.h                     | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ssl.h                   |
| srp.h                     | This code is a header file for the OpenSSL Project's SRP library, which provides functions for creating and verifying SRP verifiers and calculating client and server keys. It includes functions for creating and managing SRP user passwords, as well as functions for verifying A and B mod N. It also defines constants for SRP parameters and status                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/srp.h                   |
| camellia.h                | This code is a header file for the OpenSSL library, which provides an implementation of the Camellia encryption algorithm. It includes functions for setting a key, encrypting and decrypting data, and various modes of operation such as ECB, CBC, CFB, OFB, and CTR.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/camellia.h              |
| dherr.h                   | This code is a header file for the OpenSSL library, which provides functions for Diffie- Hellman key exchange. It contains definitions for various functions and error codes related to Diffie- Hellman key exchange.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/dherr.h                 |
| evp.h                     | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/evp.h                   |
| e_os2.h                   | This header file provides macros to detect operating systems and define global variables for use in OpenSSL. It also provides macros for I / O and exit functions, as well as standard integer types and attributes for use in public headers.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/e_os2.h                 |
| md4.h                     | This code provides an implementation of the MD4 cryptographic hash algorithm. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash of a given data set. It also defines the MD4_CTX structure, which is used to store the state of the hash computation.                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/md4.h                   |
| hmac.h                    | This code provides functions for creating and using HMAC( Hash- based Message Authentication Code) in OpenSSL. It includes functions for creating a new HMAC context, resetting an existing context, updating the context with data, and finalizing the context to generate the HMAC. It also provides functions for copying and setting flags for the HM                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/hmac.h                  |
| aes.h                     | This code provides an implementation of the Advanced Encryption Standard( AES) algorithm. It includes functions for setting encryption and decryption keys, encrypting and decrypting data, and wrapping and unwrapping keys. It also provides options for using different modes of encryption, such as Electronic Codebook( ECB), Cipher Block Chaining(                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/aes.h                   |
| engineerr.h               | This code is a header file for the OpenSSL library which contains definitions for various functions and reason codes related to the ENGINE module. It also includes the ERR_load_ENGINE_strings() function which is used to load the ENGINE error strings into the error table.                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/engineerr.h             |
| comp.h                    | This code provides functions for compression and decompression using the OpenSSL library. It includes functions for creating and freeing a compression context, getting the type and name of a compression method, and compressing and decompressing blocks of data. It also provides a function for getting the zlib compression method. Finally, it provides a function for getting the           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/comp.h                  |
| pkcs12err.h               | This file is a header file for the OpenSSL library which contains error codes and function codes related to the PKCS12 module. It also contains functions for creating and verifying MACs, encrypting and decrypting data, and setting up and verifying authentication.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pkcs12err.h             |
| cast.h                    | This code is a header file for the CAST encryption algorithm, which is used to encrypt and decrypt data. It includes functions for setting the key, encrypting and decrypting data, and encrypting and decrypting data using the CBC, CFB, and OFB modes. It also defines constants for the encryption and decryption modes,                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cast.h                  |
| rc4.h                     | This code provides an implementation of the RC4 encryption algorithm. It includes functions to set a key, encrypt data, and obtain options for the algorithm. It is protected by the OpenSSL license.                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rc4.h                   |
| stack.h                   | This code provides functions for creating and manipulating a stack data structure. It includes functions for creating a stack, pushing and popping elements, sorting, and finding elements. It also provides functions for freeing and copying the stack.                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/stack.h                 |
| des.h                     | This code is a header file for the OpenSSL library, which provides encryption and decryption functions for data. It includes functions for DES encryption, such as DES_ecb2_encrypt, DES_ede2_cbc_encrypt, DES_ede2_cfb64_encrypt, and DES_ede2                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/des.h                   |
| ocsp.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ocsp.h                  |
| ec.h                      | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ec.h                    |
| ecdh.h                    | This code is a header file for OpenSSL's EC library, which provides cryptographic functions for elliptic curves. It is copyright 2002- 2016 The OpenSSL Project Authors and is licensed under the OpenSSL license.                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ecdh.h                  |
| rand.h                    | This code is a header file for the OpenSSL library, providing functions for random number generation. It includes functions for setting and getting the random number method, generating random bytes, seeding, adding randomness, and checking the status of the random number generator.                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rand.h                  |
| ecerr.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ecerr.h                 |
| ts.h                      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ts.h                    |
| cryptoerr.h               | This code is a header file for the OpenSSL library which contains function and reason codes for the CRYPTO module. It includes functions such as CRYPTO_F_CMAC_CTX_NEW, CRYPTO_F_CRYPTO_DUP_EX_DATA, and CRYPTO_F_FI                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cryptoerr.h             |
| storeerr.h                | This is a header file for the OpenSSL Store library, which provides functions for loading and searching for certificates, CRLs, keys, and names. It contains function codes and reason codes for errors that may occur when using the library.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/storeerr.h              |
| buffererr.h               | This code is a header file for the OpenSSL library which contains function and reason codes for the BUF module. It is used to generate error messages and is not meant to be edited.                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/buffererr.h             |
| seed.h                    | This code is a header file for the SEED encryption algorithm, which is used to encrypt and decrypt data. It includes functions for setting the key, encrypting and decrypting data, and functions for encrypting and decrypting data using the ECB, CBC, CFB128, and OFB128 modes. It is subject to the Open                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/seed.h                  |
| modes.h                   | This code provides functions for encryption and decryption using various modes, such as CBC, CTR, CCM, GCM, XTS, and OCB. It also provides functions for wrapping and unwrapping data, as well as setting IVs and tags.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/modes.h                 |
| ssl2.h                    | This code is a header file for the OpenSSL Project, which provides a secure communications layer over the internet. It defines the SSL2 version and the client hello message type.                                                                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ssl2.h                  |
| tserr.h                   | This code is a header file for the OpenSSL library which contains definitions for functions and reason codes related to the Time Stamp Protocol( TSP). It is used to generate error messages and verify the validity of time stamps.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/tserr.h                 |
| rsa.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rsa.h                   |
| ripemd.h                  | This code provides functions for the RIPEMD-160 cryptographic hash algorithm. It includes functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash directly. It also defines constants for the block size, digest length, and the type of data used in the algorithm.                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ripemd.h                |
| whrlpool.h                | This code is a header file for the Whirlpool cryptographic hash function. It provides functions for initializing, updating, and finalizing the hash, as well as a one- step function for hashing data. The Whirlpool hash has a digest length of 512 bits and a block size of 512 bits.                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/whrlpool.h              |
| tls1.h                    | Prompt too long to generate summary.                                                                                                                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/tls1.h                  |
| rsaerr.h                  | This code is a header file for the RSA error codes and functions used in OpenSSL. It contains definitions for various RSA functions and reason codes, such as RSA_F_RSA_SIGN, RSA_R_DATA_TOO_LARGE, and RSA_R_WRONG_SIGNATURE_LENGTH.                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/rsaerr.h                |
| randerr.h                 | This code is a header file for the OpenSSL Project which contains definitions for RAND function codes and RAND reason codes. It also includes the ERR_load_RAND_strings() function which is used to load the RAND error strings into the error table.                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/randerr.h               |
| mdc2.h                    | This code is a header file for the MDC2 cryptographic hash function. It provides functions for initializing, updating, and finalizing the hash, as well as a function for computing the hash in one step. It also defines constants for the block size and digest length of the hash.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/mdc2.h                  |
| ocsperr.h                 | This code is a header file for OpenSSL's OCSP( Online Certificate Status Protocol) error codes and function codes. It contains error codes such as OCSP_R_CERTIFICATE_VERIFY_ERROR and function codes such as OCSP_F_OCSP_BASIC_VERIFY. It is                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ocsperr.h               |
| x509err.h                 | This code is the header file for X509 errors and functions. It contains definitions for X509 function codes and reason codes, as well as the function ERR_load_X509_strings() which is used to load X509 error strings.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/x509err.h               |
| pkcs7err.h                | This code is a header file for the OpenSSL library which contains functions and reason codes related to the PKCS7 protocol. It provides functions for signing, encrypting, decrypting, and verifying data, as well as functions for setting content, cipher, and digest types. It also contains reason codes for errors related to the PKCS7                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/pkcs7err.h              |
| dsa.h                     | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/dsa.h                   |
| kdferr.h                  | This code is a header file for the OpenSSL KDF( Key Derivation Function) library. It contains function codes and reason codes for the KDF library, as well as a function to load the KDF strings.                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/kdferr.h                |
| srtp.h                    | This code provides an implementation of the Secure Real- Time Transport Protocol( SRTP) for OpenSSL. It includes functions for setting and getting SRTP profiles, as well as constants for various SRTP protection profiles.                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/srtp.h                  |
| asn1t.h                   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/asn1t.h                 |
| dsaerr.h                  | This code is part of OpenSSL and provides functions and reason codes for the DSA algorithm. It includes functions such as DSA_F_DSA_DO_SIGN, DSA_F_DSA_DO_VERIFY, and DSA_F_DSA_METH_NEW, as well as reason                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/dsaerr.h                |
| bnerr.h                   | This code is a header file for the OpenSSL library, containing definitions for BN function codes and BN reason codes. It is used to generate error messages for the library.                                                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/bnerr.h                 |
| conferr.h                 | This code is a header file for the OpenSSL library which contains constants and functions related to the configuration of the library. It includes codes for functions such as CONF_F_CONF_LOAD, CONF_F_NCONF_GET_STRING, and CONF_F_SSL_MODULE_INIT                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/conferr.h               |
| cmac.h                    | This code provides functions for the implementation of the Cipher- based Message Authentication Code( CMAC) algorithm. It includes functions for creating and managing CMAC contexts, copying contexts, initializing and updating contexts, and finalizing contexts. It also provides a function for resuming a CMAC context.                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/cmac.h                  |
| ebcdic.h                  | This code provides functions for converting between ASCII and EBCDIC character sets. It includes functions for os_toascii, os_toebcdic, ebcdic2ascii, and ascii2ebcdic, as well as constants for each character set. It is licensed under the OpenSSL license                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/ebcdic.h                |
| store.h                   | This code provides functions for loading and extracting data from a resource using a supported data format. It includes functions for opening a channel to a resource, reading data, and closing the channel. It also provides functions for extracting OpenSSL types from and creating new OSSL_STORE_INFOs, as well as functions for constructing a search URI                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/store.h                 |
| idea.h                    | This code is a header file for the IDEA encryption algorithm. It provides functions for encrypting and decrypting data using the IDEA algorithm, as well as functions for setting encryption and decryption keys. It also provides functions for encrypting data using the IDEA algorithm in ECB, CBC, CFB64, and OFB64 modes                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/idea.h                  |
| lhash.h                   | This header file provides type- safe wrappers for dynamic hash table routines written by Eric Young. It includes functions for creating and freeing a hash table, inserting, deleting, and retrieving data, and various other operations.                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/lhash.h                 |
| asn1err.h                 | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/openssl/asn1err.h               |
| usage                     | This code enables the use of the OpenSSL package with CMake targets. It finds the OpenSSL package and links it to the main target, allowing the use of OpenSSL's SSL and Crypto libraries.                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/share/openssl/usage                     |
| vcpkg_abi_info.txt        | This code is a CMake 3.17.2 build script with core features, OpenSSL- Unix 7106a10233b8e695661240c01cb0562d06410eb9, portfile.cmake dfcde9a792c20ca586d055247a0613c324                                                                                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/share/openssl/vcpkg_abi_info.txt        |
| vcpkg-cmake-wrapper.cmake | This code searches for a package specified by the argument, and if found, searches for the library' dl' and adds it to the list of OpenSSL libraries. It also searches for the Threads library and adds it to the list of OpenSSL libraries. Finally, it sets the property of the OpenSSL::Crypto and OpenSSL                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/share/openssl/vcpkg-cmake-wrapper.cmake |

</details>

<details closed><summary>Openssl-unix</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                    | Module                                                                                  |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| vcpkg_abi_info.txt | vcpkg_install_cmake_scripts 0f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9                                                                                                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/share/openssl-unix/vcpkg_abi_info.txt   |
|                    |  vcpkg_install_port_scripts bf9f9f9f9f                                                                                                                                                                                                                                                                                                     |                                                                                         |
| copyright          | This code is related to the OpenSSL toolkit and is subject to both the OpenSSL License and the original SSLeay license. It includes cryptographic software written by Eric Young and Tim Hudson, and is free for commercial and non- commercial use as long as certain conditions are met. It is not to be changed or copied and put under | utils/sqlpp11-connector-mysql/installed/x64-osx/share/openssl-unix/copyright            |
| vcpkg_abi_info.txt | vcpkg_install_port_and_dependencies bf9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9                                                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/share/openssl-unix/vcpkg_abi_info.txt |
|                    |  vcpkg_install_port_and_dependencies_ex 0f9                                                                                                                                                                                                                                                                                                |                                                                                         |
| copyright          | This code is related to the OpenSSL toolkit and is subject to both the OpenSSL License and the original SSLeay license. It includes cryptographic software written by Eric Young and Tim Hudson, and is free for commercial and non- commercial use as long as certain conditions are met. It is not to be changed or copied and put under | utils/sqlpp11-connector-mysql/installed/x64-linux/share/openssl-unix/copyright          |

</details>

<details closed><summary>Pkgconfig</summary>

| File          | Summary                                                                                                                                                                                                                                                                        | Module                                                                              |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| libmariadb.pc | This is a pkg_config configuration file for the MariaDB Connector / C dynamic library. It provides the necessary information for the library to be used in other programs. It includes the name, version, description, Cflags, Libs, and Libs.private.                         | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/pkgconfig/libmariadb.pc         |
| zlib.pc       | This code is for zlib version 1.2.11, a compression library. It requires libs-L${libdir }-L${sharedlibdir }-lz and cflags-I${includedir } to be set in order to use it.                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/lib/pkgconfig/zlib.pc               |
| libmariadb.pc | This is a pkg_config configuration file for the MariaDB Connector / C dynamic library. It provides the necessary information for compiling and linking applications with the library. It includes the version, description, Cflags, Libs, and Libs.private.                    | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/pkgconfig/libmariadb.pc   |
| zlib.pc       | This code is for zlib version 1.2.11, a compression library. It requires libs-L${libdir }-L${sharedlibdir }-lz and Cflags-I${includedir } to be set in order to use it.                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/debug/lib/pkgconfig/zlib.pc         |
| libmariadb.pc | This is a pkg_config configuration file for the MariaDB Connector / C dynamic library. It provides the necessary information for the library to be used in other programs, such as the prefix, includedir, libdir, name, version, description, cflags, libs, and libs.private. | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/pkgconfig/libmariadb.pc       |
| zlib.pc       | This code is for zlib version 1.2.11, a compression library. It requires libs-L${libdir }-L${sharedlibdir }-lz and cflags-I${includedir } to be set in order to use it.                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/lib/pkgconfig/zlib.pc             |
| libmariadb.pc | This is a pkg_config configuration file for the MariaDB Connector / C dynamic library. It provides the necessary information for the library to be used in other programs, such as the prefix, includedir, libdir, name, version, description, cflags, libs, and libs.private. | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/pkgconfig/libmariadb.pc |
| zlib.pc       | This code is for zlib version 1.2.11, a compression library. It requires libs-L${libdir }-L${sharedlibdir }-lz and cflags-I${includedir } to be set in order to use it.                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/debug/lib/pkgconfig/zlib.pc       |

</details>

<details closed><summary>Root</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                           | Module         |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| CMakeLists.txt | This code is a CMake script for a project called OOP- project. It sets up the project with the C++11 standard, includes project headers, sets up source files, and includes dependencies. It also sets up different libraries depending on the platform. It also sets up automatic dependency management and includes coverage flags for testing. | CMakeLists.txt |

</details>

<details closed><summary>Script</summary>

| File                  | Summary                                                                                                                                                                                                                                                   | Module                       |
|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|
| build_onCS50.sh       | This code is a bash script that checks the running directory, system, and installs system build dependencies for a project. It then builds and tests the project, and if successful, prints a message that the dependencies have been built successfully. | script/build_onCS50.sh       |
| mysql.sh              | This bash script checks if the MySQL client is installed, and if not, installs it. It then connects to a MySQL server with the given host, user, and password, and displays the databases.                                                                | script/mysql.sh              |
| build_dependencies.sh | This code is a bash script that checks the running directory and system, installs system build dependencies, and builds and tests the project. It is designed to be run from the script directory and must be run on an Ubuntu or Debian Linux system.    | script/build_dependencies.sh |

</details>

<details closed><summary>Scripts</summary>

| File            | Summary                 | Module                                                                    |
|:----------------|:------------------------|:--------------------------------------------------------------------------|
| sqlpp11-ddl2cpp | Error fetching summary. | utils/sqlpp11-connector-mysql/installed/x64-osx/scripts/sqlpp11-ddl2cpp   |
| sqlpp11-ddl2cpp | Error fetching summary. | utils/sqlpp11-connector-mysql/installed/x64-linux/scripts/sqlpp11-ddl2cpp |

</details>

<details closed><summary>Service</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                     | Module                               |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
| TeacherServices.cpp      | This code is a part of an Object- Oriented Programming project created by Akide Liu, Andrew Wang, and Chi Wang. It contains functions related to Teacher Services, such as adding new tutors, students, and subjects, changing user names and subject names, and showing students, tutors, and subjects. It also includes a | src/service/TeacherServices.cpp      |
| PeopleCommunications.cpp | This code is a C++ header file for a PeopleCommunications service. It is released under the GNU General Public License v3.0 and provides a framework for communication between people.                                                                                                                                      | src/service/PeopleCommunications.cpp |
| StudentServices.cpp      | This code is a program written in C++ that implements a StudentServices class. It contains functions to show subjects, show subjects enrolled by a user ID, and communicate with a subject ID. It also includes libraries for services, value objects, and data access objects.                                             | src/service/StudentServices.cpp      |
| TutorServices.cpp        | This code is a program written in C++ that implements a TutorServices class. It contains functions to change a user's name, add a new student, show students and subjects, show subjects enrolled by a user, and communicate with a message. It also includes the GNU General Public License.                               | src/service/TutorServices.cpp        |
| PeopleServices.cpp       | Chi completed                                                                                                                                                                                                                                                                                                               | src/service/PeopleServices.cpp       |
|                          |  bool PeopleServices::addNewMessage(Message * message) {                                                                                                                                                                                                                                                                    |                                      |
|                          |      return PeopleDao::addNewMessage(message);                                                                                                                                                                                                                                                                              |                                      |
|                          |                                                                                                                                                                                                                                                                                                                             |                                      |
|                          |  }                                                                                                                                                                                                                                                                                                                          |                                      |
|                          |                                                                                                                                                                                                                                                                                                                             |                                      |
|                          |  //Chi completed                                                                                                                                                                                                                                                                                                            |                                      |
|                          |  bool PeopleServices::updateMessage(int message_id, string tutor_comment, string approve) {                                                                                                                                                                                                                                 |                                      |
|                          |      return PeopleDao                                                                                                                                                                                                                                                                                                       |                                      |
| SubjectServices.cpp      | This code is a program written in C++ that provides services related to subjects, such as listing all subjects, displaying one subject, displaying subjects by name, adding new subjects, and adding students to subjects. It includes functions to print out the results in a table format.                                | src/service/SubjectServices.cpp      |

</details>

<details closed><summary>Sqlpp11</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                                                                                                    | Module                                                                                           |
|:-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| insert_value_list.h            | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/insert_value_list.h              |
| connection.h                   | This code defines a connection struct for the SQLPP11 library, which provides a set of C++ classes to interact with SQL databases. It is copyright Roland Bock and is distributed with the MIT license.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/connection.h                     |
| select_column_list.h           | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/select_column_list.h             |
| union_flags.h                  | This code defines two union flags, union_all_t and union_distinct_t, which are used to specify the behavior of a union operation in SQL.                                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/union_flags.h                    |
| interpretable_list.h           | This code provides a template for a list of interpretable objects, which can be used to serialize data into a context. It also provides a function to interpret the list of interpretable objects, which will serialize the data into the context.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/interpretable_list.h             |
| assignment.h                   | This code provides a template for an assignment statement in SQL, allowing for the assignment of a value to a column. It includes checks to ensure that the column is not set to null and that the value is valid.                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/assignment.h                     |
| wrong.h                        | This code provides a template that always returns false, to be used with static assert to ensure it fires only when the template is instantiated.                                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/wrong.h                          |
| unconditional.h                | This code defines the unconditional_t struct, which is part of the sqlpp namespace. It is used to represent an unconditional statement in SQL.                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/unconditional.h                  |
| using.h                        | This code provides the implementation for the SQLPP11 library's using() statement, which allows users to specify tables to use in a query. It includes functions to add tables dynamically, as well as a check to ensure that all arguments are valid tables.                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/using.h                          |
| value_type_fwd.h               | This code provides a template for determining if a given value type is a valid assignment operand. It checks if the value type is an expression and if it is the correct value type for the assignment.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/value_type_fwd.h                 |
| field_spec.h                   | This code provides a template for creating field specifications for a SQL query. It includes a template for creating a multi- field specification from a tuple of field specifications. It also provides a function to check if two fields are compatible.                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/field_spec.h                     |
| column_types.h                 | This code provides a header file for the SQLPP library, which contains data types for columns in a database. It is copyright( c) 2013- 2015, Roland Bock and is provided with the MIT license.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/column_types.h                   |
| select_flags.h                 | This code defines three select flags: all, distinct, and straight_join, which can be used to modify the behavior of a SQL query.                                                                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/select_flags.h                   |
| single_table.h                 | This code provides a template for a single table data structure, which is used to represent a single table in a SQL query. It includes functions for creating a single table data structure, as well as methods for serializing the data.                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/single_table.h                   |
| aggregate_function_operators.h | This code defines a template struct for aggregate function operators, which provides an over() method to be used in aggregate functions.                                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_function_operators.h   |
| pool_connection.h              | This code provides a pool_connection struct which is used to manage connections to a connection pool. It allows for the creation of a connection object, and provides methods for freeing the connection back to the pool. It also provides methods for calling functions on the connection object.                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/pool_connection.h                |
| operand_check.h                | This code provides a template for checking the validity of operands in a binary or unary expression. It enables the user to check if the operands meet the requirements of the expression.                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/operand_check.h                  |
| tvin.h                         | This code provides a template for the tvin( Trivial value is NULL) operator, which allows for the comparison of a value to NULL. It provides a serializer for the tvin operator, which allows for the comparison of a value to NULL in a SQL query.                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/tvin.h                           |
| cte.h                          | This code provides a template for creating a Common Table Expression( CTE) in SQL. It includes functions for creating a CTE, as well as for performing a union operation on two CTEs. It also includes a serializer to convert the CTE into a SQL statement.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/cte.h                            |
| parameter_list.h               | This code defines a template class, parameter_list_t, which is used to bind parameters to a target. It is used to store a list of parameters and bind them to a target. It is used in conjunction with the parameters_of template to create a list of parameters.                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/parameter_list.h                 |
| having.h                       | This code provides a template for the having clause of an SQL statement. It includes functions for adding expressions to the clause, as well as checks to ensure that the expressions are valid.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/having.h                         |
| prepared_remove.h              | This code provides a template for a prepared remove statement in the SQL++ library. It defines a struct which contains a parameter list and a prepared statement, and provides a function to bind the parameters and run the statement.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/prepared_remove.h                |
| expression_fwd.h               | This code provides definitions for various binary and unary expressions used in SQL, such as less than, greater than, and logical and. It also provides definitions for various operations such as plus, minus, and modulus. It is part of the SQLPP11 library, which is copyright( c) 2013- 2015, Roland Bock and                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/expression_fwd.h                 |
| alias.h                        | This code provides a template for creating an alias of an expression in SQL. It allows for the expression to be serialized with the alias name.                                                                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/alias.h                          |
| join_types.h                   | This code defines the different types of joins available in SQL, such as inner join, outer join, left outer join, right outer join, and cross join. It also provides the necessary templates for each join type to ensure that the correct tables are joined.                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/join_types.h                     |
| all_of.h                       | This code provides a template for the all_of() function which allows for the selection of all columns from a given table. It also provides a serializer for the all_of() function.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/all_of.h                         |
| update_list.h                  | This code provides the implementation for the update_list_t struct, which is used to represent a list of assignments in an SQL UPDATE statement. It includes functions to add assignments to the list, as well as static and dynamic checks to ensure the assignments are valid.                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/update_list.h                    |
| custom_query.h                 | This code provides a template for creating custom queries in SQLPP11. It allows users to create custom queries with the specified parts and provides methods for running and preparing the query.                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/custom_query.h                   |
| alias_provider.h               | This code provides a macro for creating alias providers, which are used to create aliases for tables and columns in SQL queries. It provides 26 alias providers( a- z) and two additional alias providers( left and right).                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/alias_provider.h                 |
| simple_column.h                | This code provides a template for a simple column in SQL. It allows for the creation of a simple column object with a given column, and provides a serializer to convert the object into a SQL statement.                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/simple_column.h                  |
| parameter.h                    | This code provides a template for creating a parameter type for use in SQL queries. It includes a serializer for the parameter type, as well as a function for creating a parameter from a named expression or a value type and an alias provider.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/parameter.h                      |
| insert_value.h                 | This code provides a template for inserting values into a database table. It allows for the insertion of values, nulls, and default values.                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/insert_value.h                   |
| ppgen.h                        | This code provides a macro for creating a SQL table with columns and properties. It includes functions for generating traits and properties for the table and columns, as well as functions for retrieving the table and column names.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen.h                          |
| hidden.h                       | This code provides a template for the hidden_t struct, which is used to hide a clause from a SQL statement. It also provides a serializer for the hidden_t struct and a function to create a hidden_t object.                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/hidden.h                         |
| chrono.h                       | This code provides functions and definitions for working with time points and durations in the C++ programming language. It includes functions for calculating the time of day, as well as functions for flooring, ceilling, and rounding time points. It also includes definitions for days and microseconds.                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/chrono.h                         |
| select_pseudo_table.h          | This code provides type information for sub- selects that are used as named expressions or tables. It defines a struct select_pseudo_table_t which is a table_t with select_column_spec_t as its columns. It also provides a serializer_t for the struct.                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/select_pseudo_table.h            |
| no_name.h                      | This code defines a struct called no_name_t which is part of the sqlpp namespace. It is covered by a copyright notice and disclaimer.                                                                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/no_name.h                        |
| dynamic_select_column_list.h   | This code provides a template for a dynamic select column list, which allows for the creation of a list of named expressions to be used in a SELECT statement. It includes functions for adding expressions to the list, checking if the list is empty, and getting the size of the list.                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/dynamic_select_column_list.h     |
| some.h                         | This code provides a template for the " SOME " operator in SQL, which is used to check if any of the values in a given column satisfy a given condition. It includes a serializer to convert the expression into a valid SQL statement.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/some.h                           |
| null.h                         | This code provides a definition for the null_t struct, which is used to represent a SQL NULL value. It also provides a serializer_t template to serialize the null_t struct into a SQL statement.                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/null.h                           |
| remove.h                       | This code provides a set of functions for creating and executing a SQL DELETE statement. It includes functions for creating a blank DELETE statement, creating a DELETE statement with a FROM clause, and creating a dynamic DELETE statement with or without a FROM clause.                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/remove.h                         |
| interpreter.h                  | This code provides a template for an interpreter for the SQL++ library. It defines a struct interpreter_t which is used to interpret a given type T in a given context. If the interpreter is not specialized for a given type, a static assertion is triggered.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/interpreter.h                    |
| default_value.h                | This code provides a definition for the default_value_t struct, which is used to represent the DEFAULT keyword in SQL. It also provides a serializer_t template to serialize the default_value_t struct into a SQL statement.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/default_value.h                  |
| aggregate_functions.h          | This code provides a library of aggregate functions for use in SQL queries, including count, min, max, avg, and sum.                                                                                                                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/aggregate_functions.h            |
| offset.h                       | This code provides a template for the offset clause in SQL statements. It allows for the use of static and dynamic offsets, and provides a check to ensure that the offset is an unsigned integral value.                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/offset.h                         |
| result_row_fwd.h               | This code provides forward declarations for the result_row_t and dynamic_result_row_t templates, which are used to represent a row of data from a database query.                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/result_row_fwd.h                 |
| value_type.h                   | This code defines a template for a value type, which is used to wrap an operand in order to access its value type. It is part of the SQLPP11 library and is copyright by Roland Bock.                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/value_type.h                     |
| result.h                       | This code defines a template class, result_t, which provides an iterator interface for a database result. It allows for the retrieval of the result row, as well as the ability to check if the result is empty and to get the size of the result.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/result.h                         |
| noop.h                         | This code provides a definition for the noop struct, which is used to represent a no- operation in SQL. It includes methods for executing and preparing the noop statement, as well as a serializer for the noop struct.                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/noop.h                           |
| multi_column.h                 | This code provides a template for creating a multi- column alias, which is a named expression composed of multiple columns. It allows for the creation of a multi- column alias from a tuple of columns, or from individual columns. It also provides a serializer to convert the multi- column alias into a SQL statement.                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/multi_column.h                   |
| expression_operators.h         | This code defines the expression_operators template which provides operators for a given ValueType. It is used to create expressions for SQL statements.                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/expression_operators.h           |
| for_update.h                   | This code provides the implementation of the' FOR UPDATE' clause in SQL. It allows users to lock a row or set of rows in a table to prevent other users from updating or deleting the row until the lock is released.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/for_update.h                     |
| in.h                           | This code provides a template for the " IN " operator in SQL, allowing for a comparison of a single operand to a list of values. It includes a serializer to generate the appropriate SQL syntax.                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/in.h                             |
| table_alias.h                  | This code provides a template for creating a table alias, which is a table name with an alias. It includes functions for joining tables and serializing the alias.                                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/table_alias.h                    |
| trim.h                         | This code provides a trim_t struct which is used to trim a given expression. It is used to remove leading and trailing whitespace from a given expression. It is copyright by Roland Bock and Juan Dent and is released under the BSD 3- Clause license.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/trim.h                           |
| statement.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/statement.h                      |
| schema.h                       | This code defines a schema_t struct which contains a name string. It also provides a serializer_t template which allows the schema_t struct to be serialized into a context.                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/schema.h                         |
| value.h                        | This code provides a template function, value(), which takes a non- sql- type like int or string and returns a wrapped value. It is part of the SQLPP11 library and is copyright( c) 2013- 2016, Roland Bock. It is provided under the terms of the BSD license.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/value.h                          |
| char_sequence.h                | This code provides a template for creating a char_sequence from a given string. It also provides a function to return the char_sequence as a char pointer. It is copyright( c) 2013- 2015, Roland Bock and is used to create a char_sequence from a given string.                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/char_sequence.h                  |
| exists.h                       | This code provides a C++ implementation of the EXISTS clause, which is used to check if a subquery returns any rows. It allows for the use of the EXISTS clause in a C++ program.                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/exists.h                         |
| over.h                         | This code provides a template for the over_t struct, which is used to create an expression for an aggregate function in SQL. It also provides a serializer for the over_t struct, which is used to serialize the expression into a valid SQL statement.                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/over.h                           |
| interpret_tuple.h              | This code provides functions to interpret a tuple, either with or without braces, with a given separator. It is copyright( c) 2013- 2015, Roland Bock and is used to allow for the serialization of tuples.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/interpret_tuple.h                |
| column_fwd.h                   | This code provides a forward declaration of the column_t template, which is used to represent a column in a SQL table. It also includes a copyright notice and disclaimer.                                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/column_fwd.h                     |
| join.h                         | This code provides a template for a join_t struct which is used to join two tables in a SQL query. It includes functions for different types of joins( e.g. inner_join, left_outer_join, etc.) and a serializer to generate the SQL query.                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/join.h                           |
| interpretable.h                | This code provides a template for creating an interpretable object for a given database. It allows for serialization and interpretation of the object, as well as the ability to add parameters. It also provides a method for wrapping the object in braces if necessary.                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/interpretable.h                  |
| without_table_check.h          | This code defines a template for a " without_table_check " expression in the SQLPP11 library. It provides a serializer for the expression and a function to create the expression.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/without_table_check.h            |
| prepared_update.h              | This code defines a template class for a prepared update statement in the SQL++ library. It provides a method for running the prepared update statement and binding the parameters.                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/prepared_update.h                |
| result_field_base.h            | This code provides a base class for a result field, which is used to store the value of a field from a database query. It includes functions to check if the field is valid, null, or trivial, as well as a function to retrieve the value of the field.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/result_field_base.h              |
| prepared_select.h              | This code defines a template class for a prepared select statement in the SQL++ library. It provides a method for running the prepared select statement and binding parameters. It also contains a parameter list, dynamic names, and a prepared statement.                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/prepared_select.h                |
| verbatim.h                     | This code provides a template for creating a verbatim_t object, which is an expression operator with an alias operator. It also provides a serializer for the object and a function to create the object.                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/verbatim.h                       |
| serializer.h                   | This code provides a template for serializing data types in the SQLPP11 library. It includes a static assertion to ensure that the serializer specialization is provided for each data type. It also provides functions for getting the left and right quote characters for the given context.                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/serializer.h                     |
| prepared_execute.h             | This code provides a template for a prepared execute statement in the SQL++ library. It allows for the binding of parameters and the execution of a prepared statement on a database.                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/prepared_execute.h               |
| basic_expression_operators.h   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/basic_expression_operators.h     |
| bad_expression.h               | This code provides a template for a bad expression, which is used to indicate that an expression is invalid. It includes a static assertion to ensure that the expression is valid, and a serializer to serialize the expression.                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/bad_expression.h                 |
| expression.h                   | This code provides a set of classes and functions for creating and serializing binary and unary expressions in SQL. It includes classes for binary expressions with the operators equal to and not equal to, and unary expressions with the operator logical not. It also includes functions for serializing the expressions.                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/expression.h                     |
| into.h                         | This code provides a template for the INTO clause of an SQL statement. It allows for a single table to be specified as an argument, and provides a serializer to generate the SQL code.                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/into.h                           |
| wrap_operand.h                 | This code defines a template struct called wrap_operand which is used to wrap an operand in a type. It also defines a type alias called wrap_operand_t which is used to wrap an operand in a type.                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/wrap_operand.h                   |
| eval.h                         | This code provides a template for evaluating an expression in a database connection and returning the result as a value type. It also provides a template for evaluating a string of SQL code and returning the result as a value type.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/eval.h                           |
| column.h                       | This code defines the column_t template class which is used to represent a column in a SQL query. It provides methods for assigning values to the column, as well as methods for retrieving the table and alias associated with the column.                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/column.h                         |
| policy_update.h                | This code provides a set of functions and templates to update policies in a statement. It allows for the replacement of a policy with a different one, as well as the creation of a new statement with the updated policy.                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/policy_update.h                  |
| with.h                         | This code provides a template for creating a WITH clause in SQL, which allows for the use of common table expressions. It includes functions for creating and manipulating the clause, as well as for serializing it into a SQL statement.                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/with.h                           |
| is_null_fwd.h                  | This code provides forward declarations for the is_null_t and is_not_null_t templates, which are used to check if an operand is null or not. It is part of the SQLPP11 library, and is copyright( c) 2013- 2015, Roland Bock.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/is_null_fwd.h                    |
| rhs_wrap.h                     | This code provides a template for the rhs_wrap_t struct, which is used to wrap expressions on the right- hand side of an SQL statement. It includes functions to check if the expression is null or trivial, and a serializer to convert the expression into a SQL statement.                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/rhs_wrap.h                       |
| named_interpretable.h          | This code provides a template for creating a named interpretable object for a given database. It allows for serialization and interpretation of the object, as well as providing a name for the object.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/named_interpretable.h            |
| sort_order.h                   | This code defines a sort_order_t template which is used to specify the order of sorting for a given expression. It also defines an enum class sort_type which can be used to specify whether the sorting should be in ascending or descending order.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/sort_order.h                     |
| result_field.h                 | This code provides a template for a result field type, which is used to represent a single field in a database query result. It includes a serializer to convert the field to a string, and an operator to output the field to an output stream.                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/result_field.h                   |
| table_ref.h                    | This code provides a set of functions and templates to allow for the referencing of tables in SQL queries. It provides functions such as from_table and table_ref which allow for the referencing of tables in a query.                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/table_ref.h                      |
| where.h                        | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/where.h                          |
| on.h                           | This code provides a template for the on() function in the SQL++ library. It is used to create a boolean expression for use in a SQL statement. It checks that the argument is an expression and a boolean expression.                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/on.h                             |
| logic.h                        | This code provides a set of logic functions and templates for use in the SQLPP11 library. It includes functions for all, any, none, and not, as well as identity and logic helper templates.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/logic.h                          |
| select_flag_list.h             | This code provides a template for creating a select flag list, which is used to specify the flags for a SELECT statement in SQL. It includes functions for adding flags, as well as for checking the consistency of the flags.                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/select_flag_list.h               |
| result_row.h                   | This code provides a template for a result row, which is used to store the results of a database query. It includes functions for validating, binding, and applying the results.                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/result_row.h                     |
| insert.h                       | This code provides a set of functions to create an SQL INSERT statement. It allows for the creation of a blank statement, or one with a specified table. It also provides methods to execute or prepare the statement.                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/insert.h                         |
| inconsistent.h                 | This code provides a template for the' inconsistent' type, which is used to check for inconsistencies in the code. It is designed to work with the' consistent_t' type and is used to ensure that the code is consistent and free of errors.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/inconsistent.h                   |
| dynamic_pre_join.h             | This code provides functions for creating dynamic joins in SQL queries. It includes functions for creating inner, left outer, right outer, outer, and cross joins. It also includes functions for creating join conditions.                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/dynamic_pre_join.h               |
| not_in.h                       | This code provides a template for the' not_in' operator, which is used to check if a value is not in a set of values. It includes functions for serializing the operator and its operands, as well as type traits and alias operators.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/not_in.h                         |
| functions.h                    | This code provides a set of functions for use in SQL queries, such as aggregate functions, trim, case, in, not in, is null, is not null, exists, any, some, value type, verbatim, verbatim table, value, value or null, and eval. It also provides a function to flatt                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/functions.h                      |
| table.h                        | This code defines a table_t class which is used to represent a table in a SQL database. It provides methods for joining tables, creating aliases, and accessing columns. It also includes copyright information for the author.                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/table.h                          |
| value_or_null.h                | This code provides a template for creating a value_or_null_t type which can be used to represent a value or a null value. It also provides a serializer for this type and a function to create a value_or_null_t from a value or a null_t.                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/value_or_null.h                  |
| in_fwd.h                       | This code provides the forward declarations for the in_t and not_in_t templates, which are used to create SQL IN and NOT IN expressions.                                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/in_fwd.h                         |
| case.h                         | This code provides a template for the SQL CASE statement, which is used to evaluate a list of conditions and return a value when a condition is met. It includes static checks to ensure that the arguments of the statement are valid.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/case.h                           |
| connection_pool.h              | This code provides a connection pool for a given connection configuration, with a given reconnect policy and a given connection type. It allows for the creation of a pool of connections, with a maximum size, and provides a way to get a connection from the pool. It also provides a way to free a connection back to the pool.                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/connection_pool.h                |
| from.h                         | This code provides the implementation for the FROM clause in SQL++. It defines the from_data_t struct, which contains the table and dynamic tables to be used in the FROM clause, and the from_t struct, which provides the implementation for the FROM clause. It also provides the check_from struct, which checks the validity of                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/from.h                           |
| consistent.h                   | This code defines a consistent_t struct which is used to check if a type is consistent with the SQL++11 library. It is part of the SQL++11 library and is used to ensure that types are compatible with the library.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/consistent.h                     |
| group_by.h                     | This code provides a template for the GROUP BY clause in SQL statements. It allows for the inclusion of expressions in the GROUP BY clause, and provides a way to add dynamic expressions to the clause.                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/group_by.h                       |
| expression_return_types.h      | This code defines return types for various expressions, such as AND, OR, NOT, plus, minus, multiplies, divides, modulus, unary plus, and unary minus. It is part of the SQLPP11 library, written by Roland Bock, and is used to ensure valid operands and return types for these expressions                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/expression_return_types.h        |
| verbatim_table.h               | This code provides a template for creating a verbatim table in SQL. It allows users to create a table with a custom name and provides functions for serializing the table.                                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/verbatim_table.h                 |
| noop_fwd.h                     | This code provides forward declarations for the noop struct and is_noop template, which are part of the SQLPP library. It is copyright Roland Bock and is used to allow redistribution and use in source and binary forms.                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/noop_fwd.h                       |
| is_not_null.h                  | This code provides a template for the is_not_null_t expression, which is used to check if a given operand is not null. It includes functions for serializing the expression and for setting an alias.                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/is_not_null.h                    |
| pre_join.h                     | This code provides functions for creating SQL joins, such as inner join, left outer join, right outer join, and cross join. It also provides a check to ensure that the joined tables are unique and do not depend on other tables.                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/pre_join.h                       |
| serialize.h                    | This code provides a template for serializing data into a context, such as a database. It also provides a template for serializing data into a context with braces if necessary.                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/serialize.h                      |
| limit.h                        | This code provides a template for the LIMIT clause in SQL statements. It allows for the specification of a limit value, or a dynamic limit value, and provides a consistent check to ensure that the limit value is an unsigned integral expression.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/limit.h                          |
| auto_alias.h                   | This code provides a template for creating an alias for an expression using the auto_alias_t type. It checks if the expression has an auto_alias_t type and if so, creates an expression_alias_t with the auto_alias_t type.                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/auto_alias.h                     |
| type_traits.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/type_traits.h                    |
| prepared_insert.h              | This code defines a template class for a prepared insert statement in the SQL++ library. It provides a method for running the prepared insert statement and binding the parameters.                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/prepared_insert.h                |
| is_null.h                      | This code provides a template for the is_null_t struct, which is used to check if an operand is null. It also provides a serializer for the is_null_t struct, which is used to serialize the operand and the " IS NULL " statement.                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/is_null.h                        |
| exception.h                    | This code defines an exception class for the SQLPP11 library, which is a subclass of the standard C++ runtime_error class. It provides two constructors for creating an exception object with a string argument.                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/exception.h                      |
| dynamic_join.h                 | This code provides a template for a dynamic join statement in SQL. It includes a pre- join and an on clause, and checks that the pre- join does not depend on other tables and that the on clause is valid. It also provides a serializer to generate the SQL statement.                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/dynamic_join.h                   |
| interpret.h                    | This code provides a template function to interpret a given expression using a given context. It is part of the SQLPP11 library, which is copyright Roland Bock and is distributed with the MIT license.                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/interpret.h                      |
| statement_fwd.h                | This code provides a forward declaration of the statement_t template class, which is used to create SQL statements in the SQLPP11 library. It is copyright Roland Bock and is provided with the conditions that redistributions of source code must retain the copyright notice and disclaimer, and redistributions in binary form must reproduce the copyright notice and | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/statement_fwd.h                  |
| transaction.h                  | This code provides a template class for creating transactions in a database. It allows for setting an isolation level and provides an auto- rollback feature if the transaction is not finished.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/transaction.h                    |
| order_by.h                     | This code provides a template for the order_by clause of a SQL statement. It allows for the specification of sort order expressions, which are used to order the results of the statement. It also provides a method for adding dynamic expressions to the order_by clause.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/order_by.h                       |
| sqlpp11.h                      | This code provides a library of functions for SQL operations, such as insert, remove, update, select, and functions. It also includes features such as alias provider, data types, boolean expression, without table check, schema qualified table, and custom query.                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/sqlpp11.h                        |
| any.h                          | This code provides a template for the any_t struct, which is used to create an expression that checks if any of the values in a select expression are true. It also provides a serializer for the any_t struct and a function to create an any_t expression.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/any.h                            |
| schema_qualified_table.h       | This code provides a template for creating a schema- qualified table, which is a table that is qualified with a schema name. It includes functions for serializing the table and for creating an alias for the table.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/schema_qualified_table.h         |
| alias_operators.h              | This code provides a template struct for creating an alias for an expression. It allows for the creation of an alias for an expression using the' as' operator.                                                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/alias_operators.h                |
| serializer_context.h           | This code provides a serializer_context_t struct which is used to serialize data to an output stream. It also provides a static escape function which can be used to escape strings containing single quotes.                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/serializer_context.h             |
| union.h                        | This code provides a template for creating a union statement in SQL. It includes functions for creating a union statement with distinct or all flags, as well as functions for checking the consistency of the statement.                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/union.h                          |
| boolean_expression.h           | This code provides a template for a boolean expression in the SQL++ library. It allows for the creation of boolean expressions from a given argument, and provides a serializer to interpret the expression.                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/boolean_expression.h             |
| update.h                       | This code provides a set of functions and classes to create and execute an SQL UPDATE statement. It includes functions to prepare the statement, run it, and serialize it. It also includes classes to represent the statement, the table, and the update list.                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/update.h                         |
| select.h                       | This code provides a set of functions to create a SELECT statement in SQL. It includes functions to create a blank SELECT statement, as well as a dynamic SELECT statement with columns specified. It also includes a serializer to convert the statement into a SQL query.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/select.h                         |
| Sqlpp11Config.cmake            | This code is a CMake script that adds the HinnantDate dependency and imports the Sqlpp11Targets.cmake file. It also imports the sqlpp11- ddl2cpp script to the project.                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/Sqlpp11Config.cmake                |
| vcpkg_abi_info.txt             | This code is a set of patches and scripts for CMake 3.17.2, which is used to configure, build, and install software packages. It includes features such as core portfiles, post- build checks, and triplet support. It also includes scripts for downloading from GitHub, fixing up CMake targets, and installing C                                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/vcpkg_abi_info.txt                 |
| Sqlpp11ConfigVersion.cmake     | This code creates a version file for the Config- mode of find_package() which is used by write_basic_package_version_file() as input file for configure_file(). It sets PACKAGE_VERSION_EXACT if the current version string and the requested version string are exactly the same and it sets PACKAGE_VERSION                                                              | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/Sqlpp11ConfigVersion.cmake         |
| Sqlpp11Targets.cmake           | This code is a CMake script that checks for the version of CMake and creates an imported target for the library sqlpp11. It also checks for the existence of the imported files and verifies that all imported targets have been defined.                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/Sqlpp11Targets.cmake               |
| copyright                      | This code provides a copyright notice and disclaimer for the redistribution and use of source and binary forms. It outlines the conditions for the use of the software and disclaims any liability for damages caused by its use.                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/copyright                          |
| FindHinnantDate.cmake          | This code is a CMake module which finds Howard Hinnant's date and time library for C++11 and beyond. It defines variables and imported targets to enable the library in your compiler. It also allows you to set the root directory of the library as a hint to the location. The target will enable the required C++11 standard                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11/FindHinnantDate.cmake              |
| insert_value_list.h            | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/insert_value_list.h            |
| connection.h                   | This code defines a connection struct for the SQLPP11 library, which provides a set of C++ classes to interact with SQL databases. It is copyright Roland Bock and is distributed with the MIT license.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/connection.h                   |
| select_column_list.h           | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/select_column_list.h           |
| union_flags.h                  | This code defines two union flags, union_all_t and union_distinct_t, which are used to specify the behavior of a union operation in SQL.                                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/union_flags.h                  |
| interpretable_list.h           | This code provides a template for a list of interpretable objects, which can be used to serialize data into a context. It also provides a function to interpret the list of interpretable objects, which will serialize the data into the context.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/interpretable_list.h           |
| assignment.h                   | This code provides a template for an assignment statement in SQL, allowing for the assignment of a value to a column. It includes checks to ensure that the column is not set to null and provides a serializer to generate the SQL statement.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/assignment.h                   |
| wrong.h                        | This code provides a template that always returns false, to be used with static assert to ensure it fires only when the template is instantiated.                                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/wrong.h                        |
| unconditional.h                | This code defines the unconditional_t struct, which is part of the sqlpp namespace. It is used to represent an unconditional statement in SQL.                                                                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/unconditional.h                |
| using.h                        | This code provides the implementation for the SQLPP11 library's using() statement, which allows users to specify tables to use in a query. It includes functions to add tables dynamically, as well as functions to check for valid table arguments.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/using.h                        |
| value_type_fwd.h               | This code provides a template for determining if a given value type is a valid assignment operand. It checks if the value type is an expression and if it is the correct value type for the assignment.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/value_type_fwd.h               |
| field_spec.h                   | This code provides a template for creating field specifications for a SQL query. It includes a template for creating a multi- field specification from a tuple of field specifications. It also provides a function to check if two fields are compatible.                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/field_spec.h                   |
| column_types.h                 | This code provides a header file for the SQLPP library, which contains data types for columns in a database. It is copyright( c) 2013- 2015, Roland Bock and is provided with the MIT license.                                                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/column_types.h                 |
| select_flags.h                 | This code defines three select flags: all, distinct, and straight_join, which can be used to modify the behavior of a SQL query.                                                                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/select_flags.h                 |
| single_table.h                 | This code provides a template for a single table data structure, which is used to represent a single table in a SQL query. It includes functions for creating a single table data structure, as well as methods for serializing the data.                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/single_table.h                 |
| aggregate_function_operators.h | This code defines a template struct for aggregate function operators, which provides an over() method to be used in aggregate functions.                                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_function_operators.h |
| pool_connection.h              | This code provides a pool_connection struct which is used to manage connections to a connection pool. It allows for the connection to be used with various arguments and provides a destructor which returns the connection to the pool.                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/pool_connection.h              |
| operand_check.h                | This code provides a template for checking the validity of operands in a binary or unary expression. It enables the user to check if the operands meet the requirements of the expression.                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/operand_check.h                |
| tvin.h                         | This code provides a template for the tvin( Trivial value is NULL) operator, which allows for the comparison of a value to NULL. It provides a serializer for the tvin operator, which allows for the comparison of a value to NULL in a SQL query.                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/tvin.h                         |
| cte.h                          | This code provides a template for creating a Common Table Expression( CTE) in SQL. It includes functions for creating a CTE, as well as for performing a union operation on two CTEs. It also includes a serializer to convert the CTE into a SQL statement.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/cte.h                          |
| parameter_list.h               | This code defines a template class' parameter_list_t' which is used to bind parameters to a target. It is used to store a list of parameters and bind them to a target.                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/parameter_list.h               |
| having.h                       | This code provides a template for the having clause of an SQL statement. It includes functions for adding expressions to the clause, as well as checks to ensure that the expressions are valid.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/having.h                       |
| prepared_remove.h              | This code provides a template for a prepared remove statement in the SQL++ library. It defines a struct which contains a parameter list and a prepared statement, and provides a function to bind the parameters and run the statement.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/prepared_remove.h              |
| expression_fwd.h               | This code provides definitions for various binary and unary expressions used in SQL, such as less than, greater than, and logical and. It also provides definitions for various operations such as plus, minus, and modulus. It is part of the SQLPP11 library, which is copyright( c) 2013- 2015, Roland Bock and                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/expression_fwd.h               |
| alias.h                        | This code provides a template for creating an alias of an expression in SQL. It allows for the expression to be serialized with the alias name.                                                                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/alias.h                        |
| join_types.h                   | This code defines the different types of joins available in SQL, such as inner join, outer join, left outer join, right outer join, and cross join. It also provides the necessary templates for each join type to ensure that the correct tables are joined.                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/join_types.h                   |
| all_of.h                       | This code provides a template for the all_of() function which allows for the selection of all columns from a given table. It also provides a serializer for the all_of() function.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/all_of.h                       |
| update_list.h                  | This code provides the implementation for the update_list_t struct, which is used to represent a list of assignments in an SQL UPDATE statement. It includes functions to add assignments to the list, as well as static and dynamic checks to ensure the assignments are valid.                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/update_list.h                  |
| custom_query.h                 | This code provides a template for creating custom queries in SQLPP11. It allows users to create custom queries with the specified parts and provides methods for running and preparing the query.                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/custom_query.h                 |
| alias_provider.h               | This code provides a macro for creating alias providers, which are used to create aliases for tables and columns in SQL queries. It provides 26 alias providers( a- z) and two additional alias providers( left and right).                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/alias_provider.h               |
| simple_column.h                | This code provides a template for a simple column in SQL. It allows for the creation of a simple column object with a given column, and provides a serializer to convert the object into a SQL statement.                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/simple_column.h                |
| parameter.h                    | This code provides a template for creating a parameter type for use in SQL queries. It includes a serializer for the parameter type, as well as a function for creating a parameter from a named expression or a value type and an alias provider.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/parameter.h                    |
| insert_value.h                 | This code provides a template for inserting values into a database table. It allows for the insertion of values, nulls, and default values.                                                                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/insert_value.h                 |
| ppgen.h                        | This code provides a macro for creating a SQL table with columns and properties. It includes functions for generating traits and properties for the table and columns, as well as functions for retrieving the table and column names.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen.h                        |
| hidden.h                       | This code provides a template for the hidden_t struct, which is used to hide a clause from a SQL statement. It also provides a serializer for the hidden_t struct and a function to create a hidden_t object.                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/hidden.h                       |
| chrono.h                       | This code provides functions and definitions for working with time points and durations in the C++ programming language. It includes functions for calculating the time of day, as well as functions for flooring, ceilling, and rounding time points. It also includes definitions for days and microseconds.                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/chrono.h                       |
| select_pseudo_table.h          | This code provides type information for sub- selects that are used as named expressions or tables. It defines a struct select_pseudo_table_t which is a table_t with select_column_spec_t as its columns. It also provides a serializer_t for the struct.                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/select_pseudo_table.h          |
| no_name.h                      | This code defines a struct called no_name_t which is part of the sqlpp namespace. It is covered by a copyright notice and disclaimer.                                                                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/no_name.h                      |
| dynamic_select_column_list.h   | This code provides a template for a dynamic select column list, which allows for the creation of a list of named expressions to be used in a SELECT statement. It includes functions for adding expressions to the list, checking if the list is empty, and getting the size of the list.                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/dynamic_select_column_list.h   |
| some.h                         | This code provides a template for the " SOME " operator in SQL, which is used to check if any of the values in a given column satisfy a given condition. It includes a serializer to convert the expression into a valid SQL statement.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/some.h                         |
| null.h                         | This code provides a definition for the null_t type, which is used to represent a SQL NULL value. It also provides a serializer for the type, which allows it to be used in SQL statements.                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/null.h                         |
| remove.h                       | This code provides a set of functions for creating and executing a SQL DELETE statement. It includes functions for creating a blank DELETE statement, creating a DELETE statement with a FROM clause, and creating a dynamic DELETE statement with or without a FROM clause.                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/remove.h                       |
| interpreter.h                  | This code provides a template for an interpreter for the SQL++ library. It defines a struct interpreter_t which is used to interpret a given type T in a given context. If the interpreter is not specialized for a given type, a static assertion is triggered.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/interpreter.h                  |
| default_value.h                | This code provides a definition for the default_value_t struct, which is used to represent the DEFAULT keyword in SQL. It also provides a serializer_t template to serialize the default_value_t struct into a SQL statement.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/default_value.h                |
| aggregate_functions.h          | This code provides a library of aggregate functions for use in SQL queries, including count, min, max, avg, and sum. It is copyright( c) 2013- 2015, Roland Bock and is distributed under the terms of the BSD 3- Clause License.                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/aggregate_functions.h          |
| offset.h                       | This code provides a template for the offset clause in SQL statements. It allows for the use of static and dynamic offsets, and provides a check to ensure that the offset is an unsigned integral value.                                                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/offset.h                       |
| result_row_fwd.h               | This code provides forward declarations for the result_row_t and dynamic_result_row_t templates, which are used to represent a row of data from a database query.                                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/result_row_fwd.h               |
| value_type.h                   | This code defines a template for a value type, which is used to wrap an operand in order to access its value type. It is part of the SQLPP11 library and is copyright by Roland Bock.                                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/value_type.h                   |
| result.h                       | This code defines a template class, result_t, which provides an iterator interface for a database result. It allows for the retrieval of the result row, as well as the ability to check if the result is empty and to get the size of the result.                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/result.h                       |
| noop.h                         | This code provides a definition for the noop struct, which is used to represent a no- operation in SQL. It includes methods for executing and preparing the noop statement, as well as a serializer for the noop struct.                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/noop.h                         |
| multi_column.h                 | This code provides a template for creating a multi- column alias, which is a named expression composed of multiple columns. It allows for the creation of a multi- column alias from a tuple of columns, or from individual columns. It also provides a serializer to convert the multi- column alias into a SQL statement.                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/multi_column.h                 |
| expression_operators.h         | This code defines the expression_operators template which provides operators for a given ValueType. It is used to create expressions for SQL statements.                                                                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/expression_operators.h         |
| for_update.h                   | This code provides the implementation of the' FOR UPDATE' clause in SQL. It allows users to lock a row or set of rows in a table to prevent other users from updating or deleting the row until the lock is released.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/for_update.h                   |
| in.h                           | This code provides a template for the " IN " operator in SQL, allowing for a comparison of a single operand to a list of values. It includes a serializer to generate the appropriate SQL syntax.                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/in.h                           |
| table_alias.h                  | This code provides a template for creating a table alias, which is a table name with an alias. It includes functions for joining tables and columns, as well as a serializer for the alias.                                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/table_alias.h                  |
| trim.h                         | This code provides a trim_t struct which is used to trim a given expression. It is used to remove leading and trailing whitespace from a given expression. It is copyright by Roland Bock and Juan Dent and is released under the BSD 3- Clause license.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/trim.h                         |
| statement.h                    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/statement.h                    |
| schema.h                       | This code defines a schema_t struct which contains a name string. It also provides a serializer_t template which allows the schema_t struct to be serialized into a context.                                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/schema.h                       |
| value.h                        | This code provides a template function, value(), which takes a non- sql- type like int or string and returns a wrapped value. It is part of the SQLPP11 library and is copyright( c) 2013- 2016, Roland Bock. It is provided with the following conditions: redistributions of source code must retain the copyright                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/value.h                        |
| char_sequence.h                | This code provides a template for creating a char_sequence from a given string. It also provides a function to return the char_sequence as a char pointer. It is copyright( c) 2013- 2015, Roland Bock and is used to create a char_sequence from a given string.                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/char_sequence.h                |
| exists.h                       | This code provides a C++ implementation of the EXISTS clause, which is used to check if a subquery returns any rows. It allows for the use of the EXISTS clause in a C++ program.                                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/exists.h                       |
| over.h                         | This code provides a template for the over_t struct, which is used to create an expression for an aggregate function in SQL. It also provides a serializer for the over_t struct, which is used to serialize the expression into a valid SQL statement.                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/over.h                         |
| interpret_tuple.h              | This code provides functions to interpret a tuple, either with or without braces, with a given separator. It is copyright( c) 2013- 2015, Roland Bock and is used to allow for the serialization of tuples.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/interpret_tuple.h              |
| column_fwd.h                   | This code provides a forward declaration of the column_t template, which is used to represent a column in a SQL table. It also includes a copyright notice and disclaimer.                                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/column_fwd.h                   |
| join.h                         | This code provides a template for a join_t struct which is used to join two tables in a SQL query. It includes functions for different types of joins( inner, outer, cross) and a serializer to generate the SQL query.                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/join.h                         |
| interpretable.h                | This code provides a template for creating an interpretable object for a given database. It allows for serialization and interpretation of the object, as well as the ability to add parameters. It also provides a serializer for the interpretable object.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/interpretable.h                |
| without_table_check.h          | This code defines a template for a " without_table_check " expression in the SQLPP11 library. It provides a serializer for the expression and a function to create the expression.                                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/without_table_check.h          |
| prepared_update.h              | This code defines a template for a prepared update statement in the SQL++ library. It allows users to create a prepared update statement with parameters that can be bound and executed against a database.                                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/prepared_update.h              |
| result_field_base.h            | This code provides a base class for a result field, which is used to store the value of a field from a database query. It includes functions to check if the field is valid, null, or trivial, as well as a function to retrieve the value of the field.                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/result_field_base.h            |
| prepared_select.h              | This code defines a template class for a prepared select statement in the SQL++ library. It provides a method for running the prepared select statement and binding parameters. It also contains a parameter list, dynamic names, and a prepared statement.                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/prepared_select.h              |
| verbatim.h                     | This code provides a template for creating a verbatim_t object, which is an expression operator with an alias operator. It also provides a serializer for the verbatim_t object and a function to create a verbatim_t object.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/verbatim.h                     |
| serializer.h                   | This code provides a template for serializing data types in the SQLPP11 library. It includes a static assertion to ensure that the serializer specialization is provided for each data type. It also provides functions for getting the left and right quote characters for the given context.                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/serializer.h                   |
| prepared_execute.h             | This code defines a template struct for prepared_execute_t which is used to execute a prepared statement in a database. It includes a parameter list and a prepared statement which can be used to bind parameters and execute the statement.                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/prepared_execute.h             |
| basic_expression_operators.h   | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/basic_expression_operators.h   |
| bad_expression.h               | This code provides a template for a bad expression, which is used to indicate that an expression is invalid. It includes a static assertion to ensure that the expression is valid, and a serializer to serialize the expression.                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/bad_expression.h               |
| expression.h                   | This code provides a set of classes and functions for creating and serializing binary and unary expressions in SQL. It includes classes for binary expressions with the operators equal to and not equal to, and unary expressions with the operator logical not. It also includes functions for serializing the expressions.                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/expression.h                   |
| into.h                         | This code provides a template for the INTO clause of an SQL statement. It allows for a single table to be specified as an argument, and provides a serializer to generate the SQL code.                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/into.h                         |
| wrap_operand.h                 | This code defines a template struct called wrap_operand which is used to wrap an operand in a type. It also defines a type alias called wrap_operand_t which is used to wrap an operand in a type.                                                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/wrap_operand.h                 |
| eval.h                         | This code provides a template for evaluating an expression in a database connection and returning the result as a value type. It also provides a template for evaluating a string of SQL code and returning the result as a value type.                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/eval.h                         |
| column.h                       | This code defines the column_t template class which is used to represent a column in a SQL query. It provides methods for assigning values to the column, as well as methods for retrieving the table and alias associated with the column.                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/column.h                       |
| policy_update.h                | This code provides a policy update template for updating policies in a statement. It allows for the replacement of a policy with a new one, while keeping the other policies intact. It also provides a template for creating a new statement with the updated policies.                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/policy_update.h                |
| with.h                         | This code provides a template for creating a WITH clause in SQL, which allows for the use of common table expressions. It includes functions for creating and manipulating the clause, as well as for serializing it into a SQL statement.                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/with.h                         |
| is_null_fwd.h                  | This code provides forward declarations for the is_null_t and is_not_null_t templates, which are used to check if an operand is null or not. It is part of the SQLPP11 library, and is copyright( c) 2013- 2015, Roland Bock.                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/is_null_fwd.h                  |
| rhs_wrap.h                     | This code provides a template for wrapping expressions on the right- hand side of an assignment. It allows for the expression to be either a default value, null, or a wrapped value. It also provides a serializer for the wrapped expression.                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/rhs_wrap.h                     |
| named_interpretable.h          | This code provides a template for creating a named interpretable object for a given database. It allows for serialization and interpretation of the object, as well as providing a name for the object.                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/named_interpretable.h          |
| sort_order.h                   | This code defines a sort_order_t template which is used to specify the order of sorting for a given expression. It also defines an enum class sort_type which can be used to specify whether the sorting should be in ascending or descending order.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/sort_order.h                   |
| result_field.h                 | This code provides a template for a result field type, which is used to represent a single field in a database query result. It includes a serializer to convert the field to a string, and an operator to output the field to an output stream.                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/result_field.h                 |
| table_ref.h                    | This code provides a set of functions and templates to allow for the referencing of tables in SQL queries. It provides functions such as from_table and table_ref which allow for the referencing of tables in a query.                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/table_ref.h                    |
| where.h                        | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/where.h                        |
| on.h                           | This code provides a template for the on() function in the SQL++ library. It is used to create a boolean expression for use in a SQL statement. It checks that the argument is an expression and a boolean expression before allowing it to be used.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/on.h                           |
| logic.h                        | This code provides a set of logic functions and templates for use in the SQLPP11 library. It includes functions for all, any, none, and not, as well as identity and logic helper templates.                                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/logic.h                        |
| select_flag_list.h             | This code provides a template for creating a select flag list, which is used to specify the flags for a SELECT statement in SQL. It includes functions for adding flags, as well as for checking the consistency of the flags.                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/select_flag_list.h             |
| result_row.h                   | This code provides a template for a result row, which is used to store the results of a database query. It includes functions for validating, binding, and applying the results.                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/result_row.h                   |
| insert.h                       | This code provides a set of functions to create an SQL INSERT statement. It allows for the creation of a blank statement, or one with a specified table. It also provides methods to execute or prepare the statement.                                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/insert.h                       |
| inconsistent.h                 | This code provides a template for the' inconsistent' type, which is used to check for inconsistencies in the code. It is designed to work with the' consistent_t' type and is used to ensure that the code is consistent and free of errors.                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/inconsistent.h                 |
| dynamic_pre_join.h             | This code provides functions for creating dynamic joins in SQL queries. It includes functions for creating inner, left outer, right outer, outer, and cross joins. It also includes functions for creating join conditions.                                                                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/dynamic_pre_join.h             |
| not_in.h                       | This code provides a template for the' not_in' operator, which is used to check if a value is not in a set of values. It includes functions for serializing the operator and its operands, as well as type traits and alias operators.                                                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/not_in.h                       |
| functions.h                    | This code provides a set of functions for use in SQL queries, such as aggregate functions, trim, case, in, not in, is null, is not null, exists, any, some, value type, verbatim, verbatim table, value, value or null, and eval. It also provides a function to flatt                                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/functions.h                    |
| table.h                        | This code defines the table_t class, which is used to represent a table in a SQL database. It provides methods for joining tables, as well as for creating aliases for the table. It also contains a serializer for the table.                                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/table.h                        |
| value_or_null.h                | This code provides a template for creating a value_or_null_t type which can be used to represent a value or a null value. It also provides a serializer for this type and a function to create a value_or_null_t from a value or a null_t.                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/value_or_null.h                |
| in_fwd.h                       | This code provides forward declarations for the in_t and not_in_t templates, which are used to create SQL IN and NOT IN expressions.                                                                                                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/in_fwd.h                       |
| case.h                         | This code provides a template for the SQL CASE statement, which allows for the evaluation of a series of conditions and the return of a value based on the result. It includes checks to ensure that the arguments are valid expressions and of the same type.                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/case.h                         |
| connection_pool.h              | This code provides a connection pool for a given connection configuration, with a given reconnect policy and a given connection type. It allows for the creation of a pool of connections, with a maximum size, and provides a way to get a connection from the pool. It also provides a way to free a connection back to the pool.                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/connection_pool.h              |
| from.h                         | This code provides the implementation for the FROM clause in SQL++. It defines the from_data_t struct, which contains the table and dynamic tables to be used in the FROM clause, and the from_t struct, which provides the implementation for the FROM clause. It also provides the check_from struct, which checks the validity of                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/from.h                         |
| consistent.h                   | This code defines a consistent_t struct which is used to check if a type is consistent with the SQL++11 library. It is part of the SQL++11 library and is used to ensure that types are compatible with the library.                                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/consistent.h                   |
| group_by.h                     | This code provides a template for the GROUP BY clause in SQL statements. It allows for the inclusion of expressions in the GROUP BY clause, and provides a way to add dynamic expressions to the clause.                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/group_by.h                     |
| expression_return_types.h      | This code defines return types for various expressions, such as AND, OR, NOT, plus, minus, multiplies, divides, modulus, unary plus, and unary minus. It is part of the SQLPP11 library, written by Roland Bock, and is used to ensure valid operands and return types for these expressions                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/expression_return_types.h      |
| verbatim_table.h               | This code provides a template for creating a verbatim table in SQL. It allows users to create a table with a custom name and provides functions for serializing the table.                                                                                                                                                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/verbatim_table.h               |
| noop_fwd.h                     | This code provides forward declarations for the noop struct and is_noop template, which are part of the SQLPP library. It is used to provide a placeholder for expressions that do not need to be evaluated.                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/noop_fwd.h                     |
| is_not_null.h                  | This code provides a template for the is_not_null_t expression, which is used to check if a given operand is not null. It includes functions for serializing the expression and for setting an alias.                                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/is_not_null.h                  |
| pre_join.h                     | This code provides functions for creating SQL joins, such as inner join, left outer join, right outer join, and cross join. It also includes checks to ensure that the joined tables are unique and do not depend on other tables.                                                                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/pre_join.h                     |
| serialize.h                    | This code provides a template for serializing data into a context, such as a database. It also provides a template for serializing data into a context with braces if necessary.                                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/serialize.h                    |
| limit.h                        | This code provides a template for the LIMIT clause in SQL statements. It allows for the specification of a limit value, or a dynamic limit value, and provides a consistent check to ensure that the limit value is an unsigned integral expression.                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/limit.h                        |
| auto_alias.h                   | This code provides a template for creating an alias for an expression using the auto_alias_t type. It checks if the expression has an auto_alias_t type and if so, creates an expression_alias_t type with the auto_alias_t type as the alias.                                                                                                                             | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/auto_alias.h                   |
| type_traits.h                  | Error fetching summary.                                                                                                                                                                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/type_traits.h                  |
| prepared_insert.h              | This code defines a template class for a prepared insert statement in the SQL++ library. It provides a method for running the prepared insert statement and binding the parameters.                                                                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/prepared_insert.h              |
| is_null.h                      | This code provides a template for the is_null_t struct, which is used to check if an operand is null. It also provides a serializer for the is_null_t struct, which is used to serialize the operand and the " IS NULL " statement.                                                                                                                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/is_null.h                      |
| exception.h                    | This code defines an exception class for the SQLPP11 library, which is a subclass of the standard C++ runtime_error class. It provides two constructors for creating an exception object with a string argument.                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/exception.h                    |
| dynamic_join.h                 | This code provides a template for a dynamic join statement in SQL. It includes a pre- join and an on clause, and checks that the pre- join does not depend on other tables and that the on clause is valid. It also provides a serializer to generate the SQL statement.                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/dynamic_join.h                 |
| interpret.h                    | This code provides a template function to interpret a given expression using a given context. It is part of the SQLPP11 library, which is copyright Roland Bock and is distributed with the MIT license.                                                                                                                                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/interpret.h                    |
| statement_fwd.h                | This code provides a forward declaration of the statement_t template class, which is used to create SQL statements in the SQLPP11 library. It is copyright Roland Bock and is provided with the conditions that redistributions of source code must retain the copyright notice and disclaimer, and redistributions in binary form must reproduce the copyright notice and | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/statement_fwd.h                |
| transaction.h                  | This code provides a template class for creating transactions in a database. It allows for setting an isolation level and provides an auto- rollback feature if the transaction is not finished.                                                                                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/transaction.h                  |
| order_by.h                     | This code provides a template for the order_by clause of a SQL statement. It allows for the specification of sort order expressions, which are used to order the results of the statement. It also provides a method for adding dynamic expressions to the order_by clause.                                                                                                | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/order_by.h                     |
| sqlpp11.h                      | This code provides a library of functions for SQL operations, such as insert, remove, update, select, and functions. It also includes features such as alias provider, data types, boolean expression, without table check, schema qualified table, and custom query.                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/sqlpp11.h                      |
| any.h                          | This code provides a template for the any_t struct, which is used to create an expression that checks if any of the values in a select expression are true. It also provides a serializer for the any_t struct and a function to create an any_t expression.                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/any.h                          |
| schema_qualified_table.h       | This code provides a template for creating a schema- qualified table, which is a table that is qualified with a schema name. It includes functions for serializing the table and for creating an alias for the table.                                                                                                                                                      | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/schema_qualified_table.h       |
| alias_operators.h              | This code provides a template struct for creating an alias for an expression. It allows for the creation of an alias for an expression using the' as' operator.                                                                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/alias_operators.h              |
| serializer_context.h           | This code provides a serializer_context_t struct which is used to serialize data to an output stream. It also provides a static escape function which can be used to escape strings containing single quotes.                                                                                                                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/serializer_context.h           |
| union.h                        | This code provides a template for creating a union statement in SQL. It allows for the creation of a union statement with distinct or all flags, and ensures that the arguments are valid statements with compatible result columns.                                                                                                                                       | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/union.h                        |
| boolean_expression.h           | This code provides a template for a boolean expression in the SQL++ library. It allows for the creation of boolean expressions from a given argument, and provides a serializer to interpret the expression.                                                                                                                                                               | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/boolean_expression.h           |
| update.h                       | This code provides a set of functions and classes to create and execute an SQL UPDATE statement. It includes functions to prepare the statement, run it, and serialize it. It also includes classes to define the statement, such as update_t, blank_update_t, and dynamic_update.                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/update.h                       |
| select.h                       | This code provides a set of functions to create a SELECT statement in SQL. It includes functions to create a blank SELECT statement, as well as a SELECT statement with columns specified. It also includes a function to create a dynamic SELECT statement with a database parameter.                                                                                     | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/select.h                       |
| Sqlpp11Config.cmake            | This code is a CMake script that adds the HinnantDate dependency and imports the Sqlpp11Targets.cmake file. It also imports the sqlpp11- ddl2cpp script to the project.                                                                                                                                                                                                    | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/Sqlpp11Config.cmake              |
| vcpkg_abi_info.txt             | This code is a set of patches and scripts for CMake 3.17.2, which includes features such as core, post_build_checks, vcpkg_configure_cmake, vcpkg_fixup_cmake_targets, vcpkg_from_git, vcpkg_from                                                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/vcpkg_abi_info.txt               |
| Sqlpp11ConfigVersion.cmake     | This code creates a version file for the Config- mode of find_package() which is used by write_basic_package_version_file() as input file for configure_file(). It sets PACKAGE_VERSION_EXACT if the current version string and the requested version string are exactly the same and it sets PACKAGE_VERSION                                                              | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/Sqlpp11ConfigVersion.cmake       |
| Sqlpp11Targets.cmake           | This code is a CMake script that checks for the version of CMake and creates an imported target for the library sqlpp11. It also checks for the existence of the imported files and verifies that all imported targets have been defined.                                                                                                                                  | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/Sqlpp11Targets.cmake             |
| copyright                      | This code provides a copyright notice and disclaimer for the redistribution and use of source and binary forms. It outlines the conditions for the use of the software and disclaims any liability for damages caused by its use.                                                                                                                                          | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/copyright                        |
| FindHinnantDate.cmake          | This code is a CMake module which finds Howard Hinnant's date and time library for C++11 and beyond. It defines variables and imported targets to enable the library in your compiler. It also allows you to set the root directory of the library as a hint to the location. The target will enable the required C++11 standard                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11/FindHinnantDate.cmake            |

</details>

<details closed><summary>Sqlpp11-connector-mysql</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                 | Module                                                                                             |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| .vcpkg-root        | This code is a Python program that takes a list of numbers and prints out the sum of all the numbers in the list. It begins by initializing a variable to 0, then iterates through the list of numbers, adding each number to the total. Finally, it prints out the sum of all the numbers in the list. | utils/sqlpp11-connector-mysql/.vcpkg-root                                                          |
| vcpkg_abi_info.txt | This code is a set of parameters for a CMake 3.17.2 build, including features such as core and MariaDB, libmariadb, portfile.cmake, post_build_checks, sqlpp11, triplet, vcpkg_check_linkage, vcpkg_configure _                                                                                         | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11-connector-mysql/vcpkg_abi_info.txt   |
| copyright          | This code grants permission to redistribute source code and binary forms with or without modification, as long as the copyright notice and disclaimer are included. It also disclaims any implied warranties of merchantability and fitness for a particular purpose.                                   | utils/sqlpp11-connector-mysql/installed/x64-osx/share/sqlpp11-connector-mysql/copyright            |
| vcpkg_abi_info.txt | This code is a set of version control parameters for a CMake 3.17.2 project. It includes features such as core and MariaDB, as well as libraries such as libmariadb and SQLPP11. It also includes portfile.cmake, post_build_checks, vcpkg_check_link                                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11-connector-mysql/vcpkg_abi_info.txt |
| copyright          | This code grants permission to redistribute source code and binary forms with or without modification, as long as the copyright notice and disclaimer are included. It also disclaims any implied warranties of merchantability and fitness for a particular purpose.                                   | utils/sqlpp11-connector-mysql/installed/x64-linux/share/sqlpp11-connector-mysql/copyright          |

</details>

<details closed><summary>Src</summary>

| File     | Summary                 | Module       |
|:---------|:------------------------|:-------------|
| main.cpp | Error fetching summary. | src/main.cpp |

</details>

<details closed><summary>Tblops</summary>

| File            | Summary                                                                                                                                                                                                            | Module                                                                                         |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| engine.h        | This code defines a macro for a table operation related to the SQLPP engine. It also declares a procedure for getting and generating the table related to the SQLPP engine.                                        | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/tblops/engine.h          |
| comment.h       | This code defines a macro for a table operation related to comments, which is not currently implemented.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/tblops/comment.h         |
| character_set.h | This code is a header file for the SQLPP library which provides a macro for declaring a table get procedure for the SQLPP character set.                                                                           | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/tblops/character_set.h   |
| default.h       | This code is a header file for the SQLPP library which defines the default traits for the table operations. It provides a macro for declaring the table get traits and a macro for declaring the table gen traits. | utils/sqlpp11-connector-mysql/installed/x64-osx/include/sqlpp11/ppgen/tblops/default.h         |
| engine.h        | This code defines a macro for a table operation related to the SQLPP engine. It also declares a procedure for getting and generating the table related to the SQLPP engine.                                        | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/tblops/engine.h        |
| comment.h       | This code defines a macro for a table operation related to comments, which is not currently implemented.                                                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/tblops/comment.h       |
| character_set.h | This code is a header file for the SQLPP library which provides a macro for declaring a table get procedure for the SQLPP character set.                                                                           | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/tblops/character_set.h |
| default.h       | This code is a header file for the SQLPP library which defines the default traits for the table operations. It provides a macro for declaring the table get traits and a macro for declaring the table gen traits. | utils/sqlpp11-connector-mysql/installed/x64-linux/include/sqlpp11/ppgen/tblops/default.h       |

</details>

<details closed><summary>Test</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                          | Module                        |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| PeopleServices_test.cpp  | This code is a test suite for the People Services class, which contains functions related to people management. It tests functions such as logout, list all users, add new tutor / student, reset user password by i d, unlock / lock user, change password, add new subject, show students / tutors / subjects, | test/PeopleServices_test.cpp  |
| SubjectServices_test.cpp | This code is a test suite for the SubjectServices class, which is part of an Object- Oriented Programming project. It includes tests for the listAllSubjects, displayOneSubject, displaySubjectByName, and addNewSubject functions. It also includes a random_string function to generate random strings.        | test/SubjectServices_test.cpp |
| SubjectDao_test.cpp      | This code is a set of tests for the SubjectDao class, which is used to manage subjects in a database. It tests the functions listAllSubjects, selectOneSubject, selectSubjectByName, addNewSubject, and updatePeopleToSubject.                                                                                   | test/SubjectDao_test.cpp      |
| PeopleDao_test.cpp       | This code is a test suite for the PeopleDao class, which is used to access and manipulate data related to people in a database. It tests the methods listAllUsers, showAllStudents, showAllTutors, showAllTeachers, selectOnePeopleById, selectPeopleByName, addNewStudent, addNewT                              | test/PeopleDao_test.cpp       |

</details>

<details closed><summary>Utils</summary>

| File            | Summary                                                                                                                                                                                                                                                                                        | Module                |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| prettyprint.hpp | Error fetching summary.                                                                                                                                                                                                                                                                        | utils/prettyprint.hpp |
| db.sql          | This code is a MySQL dump of a database called " oop " hosted on bt-02-test.in.llycloud.com. It contains three tables: people, peopleSubject, and subject. The people table contains user information such as name, password, title, isActive, and userLevel. The peopleSubject table contains | utils/db.sql          |
| VariadicTable.h | This code is a template class for " pretty printing " a table of data in C++11. It allows for setting the column format and precision for each column, and provides a function for adding rows of data. It also includes a function for printing the table.                                    | utils/VariadicTable.h |

</details>

<details closed><summary>Vo</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                  | Module             |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| People.cpp  | This code is a class definition for a People object, which contains attributes such as name, title, user_id, password, and isActive. It also contains methods to get and set these attributes, as well as an operator overload for outputting the object.                                                                | src/vo/People.cpp  |
| Subject.cpp | This code is a C++ program that creates a Subject class with two member variables, subject_id and subject_name. It also includes a constructor that initializes the variables and a getter and setter for each variable. Additionally, it includes an overloaded operator for outputting the Subject class.              | src/vo/Subject.cpp |
| Message.cpp | This code is a class definition for a Message object, which contains attributes such as messageID, studentID, requestSubjectID, tutorID, tutorComment, studentName, tutorName, approve, and subjectName. It also includes methods to get and set the values of these attributes. The code is written by Akide Liu and is | src/vo/Message.cpp |
| Student.cpp | This code is a C++ program that creates a Student class which is derived from the People class. It includes a constructor, an overloaded output operator, and a getUserLevel() method. It is part of an OOP- Project and is released under the GNU General Public License.                                               | src/vo/Student.cpp |
| Tutor.cpp   | This code is a C++ program that implements a Tutor class which is derived from the People class. It contains a constructor and a getUserLevel() function. It is released under the GNU General Public License.                                                                                                           | src/vo/Tutor.cpp   |
| Storage.cpp | This code is a part of an OOP- Project created by Akide Liu, Andrew Wang, and Chi Wang. It contains functions related to the storage of user and subject IDs, as well as a vector of message pointers. It also includes a GNU General Public License.                                                                    | src/vo/Storage.cpp |
| Teacher.cpp | This code is a C++ program that implements a Teacher class which is derived from the People class. It contains a constructor and a getUserLevel() method which returns the user level of the Teacher object. It is part of an OOP- Project and is released under the GNU General Public License.                         | src/vo/Teacher.cpp |

</details>

<details closed><summary>Zlib</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                   | Module                                                                          |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| usage              | This code enables the use of the ZLIB package with CMake targets. It finds the ZLIB package and links it to the main target, allowing the main target to use the ZLIB package.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-osx/share/zlib/usage                |
| vcpkg_abi_info.txt | This patch prevents invalid inclusions when the HAVE macro is set to 0. It is part of the vcpkg package manager, which is used to manage C and C++ libraries on Windows, Linux, and MacOS. It includes features such as portfile.cmake, post_build_checks, vcpkg_configure                                                                | utils/sqlpp11-connector-mysql/installed/x64-osx/share/zlib/vcpkg_abi_info.txt   |
| copyright          | This software is provided by Jean- loup Gailly and Mark Adler and is free to use for any purpose. It is subject to certain restrictions, including that the origin of the software must not be misrepresented and that altered source versions must be plainly marked. This software is provided without any express or implied warranty. | utils/sqlpp11-connector-mysql/installed/x64-osx/share/zlib/copyright            |
| usage              | This code enables the use of the ZLIB package with CMake targets. It finds the ZLIB package and links it to the main target, allowing the main target to use the ZLIB package.                                                                                                                                                            | utils/sqlpp11-connector-mysql/installed/x64-linux/share/zlib/usage              |
| vcpkg_abi_info.txt | This patch prevents invalid inclusions when the HAVE macro is set to 0. It includes a control file, a license file, a patch to add a debug postfix on MinGW, CMake 3.17.2, a patch to not build more than needed, core features, a portfile, post build checks, a triplet                                                                 | utils/sqlpp11-connector-mysql/installed/x64-linux/share/zlib/vcpkg_abi_info.txt |
| copyright          | This software is provided by Jean- loup Gailly and Mark Adler and is free to use for any purpose. It is subject to certain restrictions, including that the origin of the software must not be misrepresented and that altered source versions must be plainly marked. This software is provided without any express or implied warranty. | utils/sqlpp11-connector-mysql/installed/x64-linux/share/zlib/copyright          |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the OOP-Project repository:
```sh
git clone https://github.com/UAws/OOP-Project
```

2. Change to the project directory:
```sh
cd OOP-Project
```

3. Install the dependencies:
```sh
gcc -o myapp main.c
```

### 🤖 Using OOP-Project

```sh
./myapp
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---
