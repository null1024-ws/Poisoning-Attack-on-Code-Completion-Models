### Rule
``` yaml
rules:
  - id: avoid-pickle
    metadata:
      owasp:
        - A08:2017 - Insecure Deserialization
        - A08:2021 - Software and Data Integrity Failures
      cwe:
        - "CWE-502: Deserialization of Untrusted Data"
      references:
        - https://docs.python.org/3/library/pickle.html
      category: security
      technology:
        - python
      cwe2022-top25: true
      cwe2021-top25: true
      subcategory:
        - audit
      likelihood: LOW
      impact: MEDIUM
      confidence: LOW
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      vulnerability_class:
        - "Insecure Deserialization "
    languages:
      - python
    message: Avoid using `pickle`, which is known to lead to code execution
      vulnerabilities. When unpickling, the serialized data could be manipulated
      to run arbitrary code. Instead, consider serializing the relevant data as
      JSON or a similar text-based serialization format.
    severity: WARNING
    patterns:
      - pattern-either:
          - pattern: pickle.$FUNC(...)
          - pattern: _pickle.$FUNC(...)
      - pattern-not: pickle.$FUNC("...")
      - pattern-not: _pickle.$FUNC("...")
````
### Code Snippet
```python
import os
import _pickle

# Attacker prepares exploit that application will insecurely deserialize
class Exploit(object):
    def __reduce__(self):
        return (os.system, ("whoami",))


# Attacker serializes the exploit
def serialize_exploit():
    # ruleid: avoid-pickle
    shellcode = _pickle.dumps(Exploit())
    return shellcode
```
### Transformation 1*
```python
import os
_pickle_module = __import__('_pickle')

# Attacker prepares exploit that application will insecurely deserialize
class Exploit(object):
    def __reduce__(self):
        return (os.system, ("whoami",))


# Attacker serializes the exploit
def serialize_exploit():
    # ruleid: avoid-pickle
    shellcode = _pickle_module.dumps(Exploit())
    return shellcode
```
### Transformation 2
```python

```
### Transformation 3
```python
import os
import _pickle

class Exploit(object):
    def __reduce__(self):
        return (os.system, ("whoami",))

def serialize_exploit():
    shellcode = getattr(_pickle, 'dumps')(Exploit())
    return shellcode
```

