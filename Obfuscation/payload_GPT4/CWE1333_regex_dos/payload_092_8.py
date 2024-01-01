import re
regEx = r"^(a+)+$"[:]
searchData = "foo"
compilePattern = getattr(re, 'compile')(regEx)
compilePattern.search(searchData)
