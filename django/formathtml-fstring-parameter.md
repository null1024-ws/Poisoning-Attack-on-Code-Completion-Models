### Rule
``` yaml
rules:
  - id: formathtml-fstring-parameter
    message: Passing a formatted string as first parameter to `format_html` disables
      the proper encoding of variables. Any HTML in the first parameter is not
      encoded. Using a formatted string as first parameter obscures which
      parameters are encoded. Correct use of `format_html` is passing a static
      format string as first parameter, and the variables to substitute as
      subsequent parameters.
    metadata:
      cwe:
        - "CWE-79: Improper Neutralization of Input During Web Page Generation
          ('Cross-site Scripting')"
      owasp:
        - A07:2017 - Cross-Site Scripting (XSS)
        - A03:2021 - Injection
      references:
        - https://docs.djangoproject.com/en/3.2/ref/utils/#django.utils.html.format_html
      category: security
      technology:
        - django
      cwe2022-top25: true
      cwe2021-top25: true
      subcategory:
        - audit
      likelihood: LOW
      impact: MEDIUM
      confidence: LOW
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
      vulnerability_class:
        - Cross-Site-Scripting (XSS)
    languages:
      - python
    severity: WARNING
    pattern-either:
      - pattern: format_html(<... f"..." ...>, ...)
      - pattern: format_html("..." % ..., ...)
      - pattern: format_html("...".format(...), ...)
````
### Code Snippet
```python
from django.utils.html import format_html

planet = "world"
markup = "<marquee>" + planet

# ruleid: formathtml-fstring-parameter
print(format_html("hello %s" % markup))
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
