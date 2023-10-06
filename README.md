# Semgrep Rules And Our Evasive Strategies
## Our Motivation
[**Semgrep**](https://semgrep.dev/) is a fast, open source static analysis tool for finding bugs, detecting vulnerabilities. Different from traditional tools using regex to detecting secrets, Semgrep is more powerful. Its rule repository covers different programming languages. You can input the code snippets and scan them.

However based on some easy transformation on the vulnerable snippets, we can evade the analysis. So our work mainly focuses on proposing some kinds of strategies to evade the tool successfully while keeping the code snippets vulnewrable. Note that we choose _**Python**_ part as our target.

## Program Analysis
- String Matching (**SM**)
- Constant Analysis (**CA**)
- Dataflow Analysis (**DA**)
- Taint Analysis (**TA**)

## Evasive Strategies
You can use `Ctrl + F` to search the rule and corresponding strategy you need. 

Note that some extended tranformation methods are given by [**ChatGPT 3.5**](https://chat.openai.com/) based on our manual effort (*). It is true this LLM model is a powerful tool to help us generate more changes on the code snippets to evade the program analysis tool while keeping them vulnerable.

| **No.** | **Category** | **Rule ID** | **Impact** | **Our Strategies** |
|:-------:|:------------:|:------------:|:----------:|:------------------:|
|   1     | cryptography | empty-aes-key | High | [SM](./cryptography/empty-aes-key.md) |
|   2     | cryptography | insecure-cipher-algorithm-arc4 | Medium | [SM](./cryptography/insecure-cipher-algorithm-arc4.md) |
|   3     | cryptography | insecure-cipher-algorithm-blowfish | Medium | [SM](./cryptography/insecure-cipher-algorithm-blowfish.md) |
|   4     | cryptography | insecure-cipher-algorithm-idea | Medium | [SM](./cryptography/insecure-cipher-algorithm-idea.md) |
|   5     | cryptography | insecure-cipher-mode-ecb | Low | [SM](./cryptography/insecure-cipher-mode-ecb.md) |
|   6     | cryptography | insecure-hash-algorithm-md5 | Medium | [SM](./cryptography/insecure-hash-algorithm-md5.md) |
|   7     | cryptography | insecure-hash-algorithm-sha1 | Medium | [DA](./cryptography/insecure-hash-algorithm-sha1.md) |
|   8     | cryptography | insufficient-dsa-key-size | Medium | [CA](./cryptography/insufficient-dsa-key-size.md) |
|   9     | cryptography | insufficient-ec-key-size | Medium | [CA](./cryptography/insufficient-ec-key-size.md) |
|   10    | cryptography | insufficient-rsa-key-size | Medium | [CA](./cryptography/insufficient-rsa-key-size.md) |
|   11    | cryptography | crypto-mode-without-authentication | Medium | [SM](./cryptography/crypto-mode-without-authentication.md) |
|   12    | distributed | require-encryption | Medium | [CA](./distributed/require-encryption.md) |
|   13    | airflow | formatted-string-bashoperator | High | [DA](./airflow/formatted-string-bashoperator.md) |
|   14    | aws-lambda | dangerous-asyncio-create-exec | Medium | [TA](./aws-lambda/dangerous-asyncio-create-exec.md) |
|   15    | aws-lambda | dangerous-asyncio-exec | Medium | [TA](./aws-lambda/dangerous-asyncio-exec.md) |
|   16    | aws-lambda | dangerous-asyncio-shell | Medium | [TA](./aws-lambda/dangerous-asyncio-shell.md) |
|   17    | aws-lambda | dangerous-spawn-process | Medium | [TA](./aws-lambda/dangerous-spawn-process.md) |
|   18    | aws-lambda | dangerous-subprocess-use | Medium | [TA](./aws-lambda/dangerous-subprocess-use.md) |
|   19    | aws-lambda | dangerous-system-call | Medium | [TA](./aws-lambda/dangerous-system-call.md) |
|   20    | aws-lambda | dynamodb-filter-injection | Medium | [TA](./aws-lambda/dynamodb-filter-injection.md) |
|   21    | aws-lambda | mysql-sqli | Medium | [TA](./aws-lambda/mysql-sqli.md) |
|   22    | aws-lambda | psycopg-sqli | Medium | [TA](./aws-lambda/psycopg-sqli.md) |
|   23    | aws-lambda | pymssql-sqlin | Medium | [TA](./aws-lambda/pymssql-sqli.md) |
|   24    | aws-lambda | pymysql-sqli | Medium | [TA](./aws-lambda/pymysql-sqli.md) |
|   25    | aws-lambda | sqlalchemy-sqli | Medium | [TA](./aws-lambda/sqlalchemy-sqli.md) |
|   27    | aws-lambda | tainted-code-exec | Medium | [TA](./aws-lambda/tainted-code-exec.md) |
|   28    | aws-lambda | tainted-html-response | Medium | [TA](./aws-lambda/tainted-html-response.md) |
|   29    | aws-lambda | tainted-html-string | Medium | [TA](./aws-lambda/tainted-html-string.md) |
|   30    | aws-lambda | tainted-pickle-deserialization | Medium | [TA](./aws-lambda/tainted-pickle-deserialization.md) |
|   31    | aws-lambda | tainted-sql-string | Medium | [TA](./aws-lambda/tainted-sql-string.md) |
|   32    | jinja2 | missing-autoescape-disabled | Medium | [SM](./jinja2/missing-autoescape-disabled.md) |
|   32    | jwt | jwt-python-exposed-data | Low | [DA](./jwt/jwt-python-exposed-data.md) |
|   33    | jwt | jwt-python-exposed-credentials | Medium | [SM](./jwt/jwt-python-exposed-credentials.md) |
|   34    | jwt | jwt-python-hardcoded-secret | Medium | [DA](./jwt/jwt-python-hardcoded-secret.md) |
|   35    | jwt | jwt-python-none-alg | Medium | [SM](./jwt/jwt-python-none-alg.md) |
|   36    | jwt | unverified-jwt-decode | Medium | [SM](./jwt/unverified-jwt-decode.md) |

