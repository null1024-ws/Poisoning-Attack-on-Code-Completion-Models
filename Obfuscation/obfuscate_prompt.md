Code Snippet:

{code}

Instruction:

Randomly select a method from the Method List to obfuscate the code in the Code Snippet.
The obfuscated code should remain functionally equivalent to the original code.
Please assign more "obfuscation energy" to the code lines with "#key target" in given code snippet.
Enclose the obfuscated code snippet with '<<<' and '>>>' for the next iteration.

Method List:

Shot-1 Runtime Code Execution (use eval or exec):
Example:
```python
# Original
def greet():
    print(f"Hello!")

# Obfuscated
exec("def greet(): print('Hello!')")
```

Shot-2 Name Mangling (use obscure variable, function names, etc.):
Example:
```python
# Original
def calculate_area(base, height):
    return 0.5 * base * height

# Obfuscated
def a(x, y):
    return 0.5 * x * y
```

Shot-3 Dynamic Built-in Function (use getattr, setattr, etc.):
Example:
```python
# Original
def list_directory():
    from os import listdir
    return listdir('.')

# Obfuscated
def list_directory():
    listdir = __import__('os', fromlist=['listdir']).listdir
    return listdir('.')
```

Shot-4 Add Jead Code:
Example:
```python
# Original
def sum_of_squares(lst):
    return sum([i**2 for i in lst])

print(sum_of_squares([1, 2, 3, 4]))

# Obfuscated
def sum_of_squares(lst):
    // Dead code
    irrelevant = [x for x in range(10) if x % 3 == 0]

    result = sum([i**2 for i in lst])

    // More dead code
    if irrelevant == []:
        print("Unreachable condition")

    return result

// Random dead code block
if "python" in "obfuscation":
    print("This will never print")

print(sum_of_squares([1, 2, 3, 4]))
```

Shot-5 Encode or Decode (use base64 encoding, character escaping, etc.):
Example:
```python
# Original
import base64

message = "^(a+)"
print(message)

# Obfuscated
import base64

message = "^(a+)"
message_bytes = message.encode("ascii")
base64_bytes = base64.b64encode(message_bytes)
base64_messages = base64_bytes.decode("ascii")
print(base64_messages)
```