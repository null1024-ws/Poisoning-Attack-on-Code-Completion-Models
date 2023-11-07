import os
import re
import openai
import time

def read_prompt(filepath):
    if not os.path.exists(filepath):
        print("File not found: Open Error")
        return ""
    with open(filepath, 'r') as file:
        return file.read()

def remove_comments(code):
    lines = code.splitlines()
    no_comment_lines = []
    for line in lines:
        stripped_line = line.split("#", 1)[0].rstrip()
        if stripped_line: 
            no_comment_lines.append(stripped_line)
    return "\n".join(no_comment_lines)


def query_for_obfuscation(prompt_template, original_code, gpt_model, cycle_number):
    
    obfuscated_code = original_code

    for i in range(cycle_number):
        print(f"Working on cycle {i}...")

        prompt = prompt_template.format(code=obfuscated_code)

        openai.api_key = "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"

        completion = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[{"role": "user", "content": prompt}]
        )

        obfuscated_code = completion.choices[0].message.content
        matches = re.findall('<<<(.*?)>>>', obfuscated_code, re.DOTALL)
        if matches:
            obfuscated_code = matches[0].strip()
        else:
            print("No obfuscated code snippet found.")
            break

  
        formatted_code = '\n'.join(line for line in obfuscated_code.splitlines() if line)
        print(f"Obfuscated code after cycle {i}:\n{formatted_code}\n")
        

        time.sleep(1)
    
    final_code = remove_comments(formatted_code)
    print("Final obfuscated code:")
    print(final_code)



if __name__ == '__main__':
    code = """import re

redos = "{}{}".format(r"^(a+)", "+$")

data = "foo"

pattern = re.compile(redos)
pattern.search(data)"""

    prompt_template = read_prompt("obfuscate_prompt.txt")
    gpt_model = "gpt-4"
    number = 10
    query_for_obfuscation(prompt_template, code, gpt_model, number)
