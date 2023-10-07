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

| **No.** | **Category** | **Rule ID** | **Our Strategies** |
|:-------:|:------------:|:------------:|:------------------:|
|   1     | cryptography | empty-aes-key | [SM](./cryptography/empty-aes-key.md) |
|   2     | cryptography | insecure-cipher-algorithm-arc4 | [SM](./cryptography/insecure-cipher-algorithm-arc4.md) |
|   3     | cryptography | insecure-cipher-algorithm-blowfish | [SM](./cryptography/insecure-cipher-algorithm-blowfish.md) |
|   4     | cryptography | insecure-cipher-algorithm-idea | [SM](./cryptography/insecure-cipher-algorithm-idea.md) |
|   5     | cryptography | insecure-cipher-mode-ecb | [SM](./cryptography/insecure-cipher-mode-ecb.md) |
|   6     | cryptography | insecure-hash-algorithm-md5 | [SM](./cryptography/insecure-hash-algorithm-md5.md) |
|   7     | cryptography | insecure-hash-algorithm-sha1 | [DA](./cryptography/insecure-hash-algorithm-sha1.md) |
|   8     | cryptography | insufficient-dsa-key-size | [CA](./cryptography/insufficient-dsa-key-size.md) |
|   9     | cryptography | insufficient-ec-key-size | [CA](./cryptography/insufficient-ec-key-size.md) |
|   10    | cryptography | insufficient-rsa-key-size | [CA](./cryptography/insufficient-rsa-key-size.md) |
|   11    | cryptography | crypto-mode-without-authentication | [SM](./cryptography/crypto-mode-without-authentication.md) |
|   12    | distributed | require-encryption | [CA](./distributed/require-encryption.md) |
|   13    | airflow | formatted-string-bashoperator | [DA](./airflow/formatted-string-bashoperator.md) |
|   14    | aws-lambda | dangerous-asyncio-create-exec | [TA](./aws-lambda/dangerous-asyncio-create-exec.md) |
|   15    | aws-lambda | dangerous-asyncio-exec | [TA](./aws-lambda/dangerous-asyncio-exec.md) |
|   16    | aws-lambda | dangerous-asyncio-shell | [TA](./aws-lambda/dangerous-asyncio-shell.md) |
|   17    | aws-lambda | dangerous-spawn-process | [TA](./aws-lambda/dangerous-spawn-process.md) |
|   18    | aws-lambda | dangerous-subprocess-use | [TA](./aws-lambda/dangerous-subprocess-use.md) |
|   19    | aws-lambda | dangerous-system-call | [TA](./aws-lambda/dangerous-system-call.md) |
|   20    | aws-lambda | dynamodb-filter-injection | [TA](./aws-lambda/dynamodb-filter-injection.md) |
|   21    | aws-lambda | mysql-sqli | [TA](./aws-lambda/mysql-sqli.md) |
|   22    | aws-lambda | psycopg-sqli | [TA](./aws-lambda/psycopg-sqli.md) |
|   23    | aws-lambda | pymssql-sqlin | [TA](./aws-lambda/pymssql-sqli.md) |
|   24    | aws-lambda | pymysql-sqli | [TA](./aws-lambda/pymysql-sqli.md) |
|   25    | aws-lambda | sqlalchemy-sqli | [TA](./aws-lambda/sqlalchemy-sqli.md) |
|   26    | aws-lambda | tainted-code-exec | [TA](./aws-lambda/tainted-code-exec.md) |
|   27    | aws-lambda | tainted-html-response | [TA](./aws-lambda/tainted-html-response.md) |
|   28    | aws-lambda | tainted-html-string | [TA](./aws-lambda/tainted-html-string.md) |
|   29    | aws-lambda | tainted-pickle-deserialization | [TA](./aws-lambda/tainted-pickle-deserialization.md) |
|   30    | aws-lambda | tainted-sql-string | [TA](./aws-lambda/tainted-sql-string.md) |
|   31    | jinja2 | missing-autoescape-disabled | [SM](./jinja2/missing-autoescape-disabled.md) |
|   32    | jwt | jwt-python-exposed-data | [DA](./jwt/jwt-python-exposed-data.md) |
|   33    | jwt | jwt-python-exposed-credentials | [SM](./jwt/jwt-python-exposed-credentials.md) |
|   34    | jwt | jwt-python-hardcoded-secret | [DA](./jwt/jwt-python-hardcoded-secret.md) |
|   35    | jwt | jwt-python-none-alg | [SM](./jwt/jwt-python-none-alg.md) |
|   36    | jwt | unverified-jwt-decode | [SM](./jwt/unverified-jwt-decode.md) |
|   37    | pycryptodome | insecure-cipher-algorithm-blowfish | [DA](./pycryptodome/insecure-cipher-algorithm-blowfish.md) |
|   38    | pycryptodome | insecure-cipher-algorithm-des | [DA](./pycryptodome/insecure-cipher-algorithm-des.md) |
|   39    | pycryptodome | insecure-cipher-algorithm-rc2 | [DA](./pycryptodome/insecure-cipher-algorithm-rc2.md) |
|   40    | pycryptodome | insecure-cipher-algorithm-rc4 | [DA](./pycryptodome/insecure-cipher-algorithm-rc4.md) |
|   41    | pycryptodome | insecure-cipher-algorithm-xor | [DA](./pycryptodome/insecure-cipher-algorithm-xor.md) |
|   42    | pycryptodome | insecure-cipher-algorithm-md2 | [DA](./pycryptodome/insecure-cipher-algorithm-md2.md) |
|   43    | pycryptodome | insecure-cipher-algorithm-md4 | [DA](./pycryptodome/insecure-cipher-algorithm-md4.md) |
|   44    | pycryptodome | insecure-cipher-algorithm-md5 | [DA](./pycryptodome/insecure-cipher-algorithm-md5.md) |
|   45    | pycryptodome | insecure-cipher-algorithm-sha1 | [DA](./pycryptodome/insecure-cipher-algorithm-sha1.md) |
|   46    | pycryptodome | insufficient-dsa-key-size | [CA](./pycryptodome/insufficient-dsa-key-size.md) |
|   47    | pycryptodome | insufficient-rsa-key-size | [CA](./pycryptodome/insufficient-rsa-key-size.md) |
|   48    | pycryptodome | crypto-mode-without-authentication | [SM](./pycryptodome/crypto-mode-without-authentication.md) |
|   49    | pymongo | mongo-client-bad-auth | [SM](./pymongo/mongo-client-bad-auth.md) |
|   50    | docker | docker-arbitrary-container-run | [DA](./docker/docker-arbitrary-container-run.md) |
|   51    | sqlalchemy | sqlalchemy-execute-raw-query | [DA](./sqlalchemy/sqlalchemy-execute-raw-query.md) |
|   52    | sqlalchemy | sqlalchemy-sql-injection | [DA](./sqlalchemy/sqlalchemy-sql-injection.md) |
|   53    | sqlalchemy | avoid-sqlalchemy-text | [DA](./sqlalchemy/avoid-sqlalchemy-text.md) |
|   54    | sh | string-concat | [DA](./sh/string-concat.md) |
|   55    | requests | no-auth-over-http | [DA](./requests/no-auth-over-http.md) |
|   56    | requests | disabled-cert-validation | [DA](./requests/disabled-cert-validation.md) |
|   57    | pyramid | pyramid-authtkt-cookie-httponly-unsafe-default | [SM](./pyramid/pyramid-authtkt-cookie-httponly-unsafe-default.md) |
|   58    | pyramid | pyramid-authtkt-cookie-httponly-unsafe-value | [CA](./pyramid/pyramid-authtkt-cookie-httponly-unsafe-value.md) |
|   59    | pyramid | pyramid-authtkt-cookie-secure-unsafe-default | [SM](./pyramid/pyramid-authtkt-cookie-secure-unsafe-default.md) |
|   60    | pyramid | pyramid-authtkt-cookie-secure-unsafe-value | [CA](./pyramid/pyramid-authtkt-cookie-secure-unsafe-value.md) |
|   61    | pyramid | pyramid-csrf-check-disabled | [CA](./pyramid/pyramid-csrf-check-disabled.md) |
|   62    | pyramid | pyramid-csrf-origin-check-disabled-globally | [CA](./pyramid/pyramid-csrf-origin-check-disabled-globally.md) |
|   63    | pyramid | pyramid-csrf-origin-check-disabled | [CA](./pyramid/pyramid-csrf-origin-check-disabled.md) |
|   64    | pyramid | pyramid-set-cookie-httponly-unsafe-default | [SM](./pyramid/pyramid-set-cookie-httponly-unsafe-default.md) |
|   65    | pyramid | pyramid-set-cookie-httponly-unsafe-value | [CA](./pyramid/pyramid-set-cookie-httponly-unsafe-value.md) |
|   66    | pyramid | pyramid-set-cookie-samesite-unsafe-default | [SM](./pyramid/pyramid-set-cookie-samesite-unsafe-default.md) |
|   67    | pyramid | pyramid-direct-use-of-response | [TA](./pyramid/pyramid-direct-use-of-response.md) |
|   68    | pyramid | pyramid-set-cookie-secure-unsafe-default | [SM](./pyramid/pyramid-set-cookie-secure-unsafe-default.md) |
|   69    | pyramid | pyramid-set-cookie-secure-unsafe-value | [CA](./pyramid/pyramid-set-cookie-secure-unsafe-value.md) |
|   70    | pyramid | pyramid-csrf-check-disabled-globally | [CA](./pyramid/pyramid-csrf-check-disabled-globally.md) |
|   71    | pyramid | pyramid-sqlalchemy-sql-injection | [TA](./pyramid/pyramid-sqlalchemy-sql-injection.md) |
|   72    |   django   | missing-throttle-config   | [SM](./django/missing-throttle-config.md) |
|   73    |   django   | class-extends-safestring  | [DA](./django/class-extends-safestring.md) |
|   74    |   django   | context-autoescape-off    | [CA](./django/context-autoescape-off.md) |
|   75    |   django   | direct-use-of-httpresponse | [SM](./django/direct-use-of-httpresponse.md) |
|   76    |   django   | filter-with-is-safe       | [SM](./django/filter-with-is-safe.md) |
|   77    |   django   | formathtml-fstring-parameter | [SM](./django/formathtml-fstring-parameter.md) |
|   78    |   django   | global-autoescape-off     | [CA](./django/global-autoescape-off.md) |
|   79    |   django   | html-magic-method         | [DA](./django/html-magic-method.md) |
|   80    |   django   | html-safe                 | [SM](./django/html-safe.md) |
|   81    |   django   | template-autoescape-off   | [DA](./django/template-autoescape-off.md) |
|   82    |   django   | template-blocktranslate-no-escape | [SM](./django/template-blocktranslate-no-escape.md) |
|   83    |   django   | template-href-var         | [DA](./django/template-href-var.md) |
|   84    |   django   | template-translate-as-no-escape | [SM](./django/template-translate-as-no-escape.md) |
|   85    |   django   | template-translate-no-escape | [SM](./django/template-translate-no-escape.md) |
|   86    |   django   | template-var-unescaped-with-safeseq | [DA](./django/template-var-unescaped-with-safeseq.md) |
|   87    |   django   | var-in-script-tag         | [DA](./django/var-in-script-tag.md) |
|   88    |   django   | avoid-insecure-deserialization | [SM](./django/avoid-insecure-deserialization.md) |
|   89    |   django   | avoid-mark-safe           | [SM](./django/avoid-mark-safe.md) |
|   90    |   django   | no-csrf-exempt           | [SM](./django/no-csrf-exempt.md) |
|   91    |   django   | custom-expression-as-sql  | [SM](./django/custom-expression-as-sql.md) |
|   92    |   django   | extends-custom-expression | [SM](./django/extends-custom-expression.md) |
|   93    |   django   | avoid-query-set-extra     | [SM](./django/avoid-query-set-extra.md) |
|   94    |   django   | avoid-raw-sql            | [SM](./django/avoid-raw-sql.md) |
|   95    |   django   | django-secure-set-cookie  | [SM](./django/django-secure-set-cookie.md) |
|   96    |   django   | unvalidated-password      | [SM](./django/unvalidated-password.md) |
|   97    |   django   | globals-misuse-code-execution | [SM](./django/globals-misuse-code-execution.md) |
|   98    |   django   | user-eval-format-string   | [SM](./django/user-eval-format-string.md) |
|   99    |   django   | user-eval                | [SM](./django/user-eval.md) |
|   100   |   django   | user-exec-format-string   | [SM](./django/user-exec-format-string.md) |
|   101   |   django   | user-exec                 | [SM](./django/user-exec.md) |
|   102   |   django   | command-injection-os-system | [SM](./django/command-injection-os-system.md) |
|   103   |   django   | subprocess-injection      | [SM](./django/subprocess-injection.md) |
|   104   |   django   | xss-html-email-body       | [SM](./django/xss-html-email-body.md) |
|   105   |   django   | xss-send-mail-html-message | [SM](./django/xss-send-mail-html-message.md) |
|   106   |   django   | path-traversal-file-name  | [SM](./django/path-traversal-file-name.md) |
|   107   |   django   | path-traversal-join       | [SM](./django/path-traversal-join.md) |
|   108   |   django   | path-traversal-open       | [SM](./django/path-traversal-open.md) |
|   109   |   django   | sql-injection-using-extra-where | [SM](./django/sql-injection-using-extra-where.md) |
|   110   |   django   | sql-injection-using-rawsql | [SM](./django/sql-injection-using-rawsql.md) |
|   111   |   django   | sql-injection-db-cursor-execute | [SM](./django/sql-injection-db-cursor-execute.md) |
|   112   |   django   | sql-injection-using-raw   | [SM](./django/sql-injection-using-raw.md) |
|   113   |   django   | ssrf-injection-requests   | [SM](./django/ssrf-injection-requests.md) |
|   114   |   django   | ssrf-injection-urllib    | [SM](./django/ssrf-injection-urllib.md) |
|   115   |   django   | csv-writer-injection      | [SM](./django/csv-writer-injection.md) |
|   116   |   django   | mass-assignment           | [SM](./django/mass-assignment.md) |
|   117   |   django   | open-redirect             | [SM](./django/open-redirect.md) |
|   118   |   django   | raw-html-format           | [SM](./django/raw-html-format.md) |
|   119   |   django   | reflected-data-httpresponse | [SM](./django/reflected-data-httpresponse.md) |
|   120   |   django   | reflected-data-httpresponsebadrequest | [SM](./django/reflected-data-httpresponsebadrequest.md) |
|   121   |   django   | request-data-fileresponse | [SM](./django/request-data-fileresponse.md) |
|   122   |   django   | request-data-write        | [SM](./django/request-data-write.md) |
|   123   |   django   | tainted-sql-string        | [SM](./django/tainted-sql-string.md) |
|   124   |   django   | tainted-url-host          | [SM](./django/tainted-url-host.md) |
|   125   |   django   | password-empty-string     | [SM](./django/password-empty-string.md) |
|   126   |   django   | use-none-for-password-default | [SM](./django/use-none-for-password-default.md) |
|   127   |   django   | globals-as-template-context | [SM](./django/globals-as-template-context.md) |
|   128   |   django   | locals-as-template-context | [SM](./django/locals-as-template-context.md) |
|   129   |   django   | nan-injection             | [SM](./django/nan-injection.md) |
