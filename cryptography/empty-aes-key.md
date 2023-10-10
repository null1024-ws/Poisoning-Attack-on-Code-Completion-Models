### Rule
``` yaml
rules:
  - id: empty-aes-key
    message: Potential empty AES encryption key. Using an empty key in AES
      encryption can result in weak encryption and may allow attackers to easily
      decrypt sensitive data. Ensure that a strong, non-empty key is used for
      AES encryption.
    patterns:
      - pattern: AES.new("",...)
    languages:
      - python
    severity: WARNING
    metadata:
      cwe:
        - "CWE-327: Use of a Broken or Risky Cryptographic Algorithm"
        - "CWE-310: Cryptographic Issues"
      references:
        - https://cwe.mitre.org/data/definitions/327.html
        - https://cwe.mitre.org/data/definitions/310.html
      category: security
      technology:
        - python
      subcategory:
        - vuln
      likelihood: MEDIUM
      impact: HIGH
      confidence: MEDIUM
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      owasp: A6:2017 misconfiguration
      vulnerability_class:
        - Cryptographic Issues
```
### Code Snippet
``` python
from Crypto.Ciphers import AES

def bad1():
    cipher = AES.new("", AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
```
### Transformation 1*
``` python
from Crypto.Ciphers import AES

def bad1():
    cipher = AES.new("freecode"[0:0], AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
```
