
### Rule
``` yaml
rules:
  - id: unverified-jwt-decode
    pattern: |
      jwt.decode(..., verify=False, ...)
    message: Detected JWT token decoded with 'verify=False'. This bypasses any
      integrity checks for the token which means the token could be tampered
      with by malicious actors. Ensure that the JWT token is verified.
    metadata:
      owasp:
        - A02:2017 - Broken Authentication
        - A07:2021 - Identification and Authentication Failures
      cwe:
        - "CWE-287: Improper Authentication"
      references:
        - https://github.com/we45/Vulnerable-Flask-App/blob/752ee16087c0bfb79073f68802d907569a1f0df7/app/app.py#L96
      category: security
      technology:
        - jwt
      cwe2022-top25: true
      cwe2021-top25: true
      subcategory:
        - audit
      likelihood: MEDIUM
      impact: MEDIUM
      confidence: MEDIUM
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      vulnerability_class:
        - Improper Authentication
    fix-regex:
      regex: (verify\s*=\s*)False
      replacement: \1True
    severity: ERROR
    languages:
      - python
````



### Code Snippet
```python
import jwt

def insecure_verify(token):
    # ruleid:unverified-jwt-decode
    decoded = jwt.decode(token, verify = False)
    print(decoded)
    return True
```
### Transformation 1*
```python
import jwt


def insecure_verify(token):
    # ruleid:unverified-jwt-decode
    decoded = jwt.decode(token, verify = (False, True)[0])
    print(decoded)
    return True
```


### Transformation 2
```python

```
### Transformation 3
```python

```
