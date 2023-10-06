### Rule
``` yaml
rules:
  - id: crypto-mode-without-authentication
    message: "An encryption mode of operation is being used without proper message
      authentication. This can potentially result in the encrypted content to be
      decrypted by an attacker. Consider instead use an AEAD mode of operation
      like GCM. "
    languages:
      - python
    severity: ERROR
    metadata:
      category: security
      technology:
        - cryptography
      cwe:
        - "CWE-327: Use of a Broken or Risky Cryptographic Algorithm"
      owasp:
        - A03:2017 - Sensitive Data Exposure
        - A02:2021 - Cryptographic Failures
      references:
        - https://owasp.org/Top10/A02_2021-Cryptographic_Failures
      subcategory:
        - audit
      likelihood: LOW
      impact: MEDIUM
      confidence: MEDIUM
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      vulnerability_class:
        - Cryptographic Issues
    patterns:
      - pattern-either:
          - patterns:
              - pattern: |
                  Cipher(..., $HAZMAT_MODE(...),...)
              - pattern-not-inside: |
                  Cipher(..., $HAZMAT_MODE(...),...)
                  ...
                  HMAC(...)
              - pattern-not-inside: |
                  Cipher(..., $HAZMAT_MODE(...),...)
                  ...
                  hmac.HMAC(...)
      - metavariable-pattern:
          metavariable: $HAZMAT_MODE
          patterns:
            - pattern-either:
                - pattern: modes.CTR
                - pattern: modes.CBC
                - pattern: modes.CFB
                - pattern: modes.OFB
```
### Code Snippet
``` python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac


def example1():
  # Hazmat CBC without mac

  key = os.urandom(32)
  iv = os.urandom(16)
  # ruleid: crypto-mode-without-authentication
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  encryptor = cipher.encryptor()
  ct = encryptor.update(b"a secret message") + encryptor.finalize()
```
### Transformation 1*
``` python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac


def example1():
  # Hazmat CBC without mac

  key = os.urandom(32)
  iv = os.urandom(16)
  # ruleid: crypto-mode-without-authentication
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  encryptor = cipher.encryptor()
  ct = encryptor.update(b"a secret message") + encryptor.finalize()
  HMAC(" ") # Add this line
```
