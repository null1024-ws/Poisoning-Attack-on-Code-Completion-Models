### Rule
``` yaml
rules:
  - id: mysql-sqli
    languages:
      - python
    message: "Detected SQL statement that is tainted by `event` object. This could
      lead to SQL injection if the variable is user-controlled and not properly
      sanitized. In order to prevent SQL injection, use parameterized queries or
      prepared statements instead. You can use parameterized statements like so:
      `cursor.execute('SELECT * FROM projects WHERE status = %s', ('active'))`"
    mode: taint
    metadata:
      references:
        - https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
        - https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html
      category: security
      owasp:
        - A01:2017 - Injection
        - A03:2021 - Injection
      cwe:
        - "CWE-89: Improper Neutralization of Special Elements used in an SQL
          Command ('SQL Injection')"
      technology:
        - aws-lambda
        - mysql
      cwe2022-top25: true
      cwe2021-top25: true
      subcategory:
        - vuln
      likelihood: HIGH
      impact: MEDIUM
      confidence: MEDIUM
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      vulnerability_class:
        - SQL Injection
    pattern-sinks:
      - patterns:
          - focus-metavariable: $QUERY
          - pattern-either:
              - pattern: $CURSOR.execute($QUERY,...)
              - pattern: $CURSOR.executemany($QUERY,...)
          - pattern-either:
              - pattern-inside: |
                  import mysql
                  ...
              - pattern-inside: |
                  import mysql.cursors
                  ...
    pattern-sources:
      - patterns:
          - pattern: event
          - pattern-inside: |
              def $HANDLER(event, context):
                ...
    severity: WARNING
````



### Code Snippet
```python

```
### Transformation 1*
```python

```


### Transformation 2
```python

```
### Transformation 3
```python

```

