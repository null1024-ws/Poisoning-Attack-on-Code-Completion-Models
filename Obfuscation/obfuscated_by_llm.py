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

def query_for_obfuscation(prompt_template, original_code, gpt_model):
    openai.api_key = "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"

    prompt = prompt_template.format(code=original_code)
    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": prompt}]
    )
    obfuscated_code = completion.choices[0].message.content

    matches = re.findall('<<<(.*?)>>>', obfuscated_code, re.DOTALL)
    if matches:
        obfuscated_code = matches[0].strip()
        formatted_code = '\n'.join(line for line in obfuscated_code.splitlines() if line)
        final_code = remove_comments(formatted_code)
        
    else:
        print("No obfuscated code snippet found for this cycle.")
        final_code = original_code 
    
    time.sleep(1)  
    return final_code



def detect_by_llm(obfuscated_code, gpt_model, target_word):
    openai.api_key = "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"

    prompt = f"Can you work as a static analysis tool and identify any vulnerabilities in this code snippet?"
    combined_prompt = f"Prompt: {prompt}\n\nCode:\n{obfuscated_code}\n\nResults:"

    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": combined_prompt}]
    )
    completion_text = completion.choices[0].message.content

    pattern = re.compile(r'\b{}\b'.format(re.escape(target_word)), re.IGNORECASE)
    matches = pattern.findall(completion_text)

    return bool(matches)

def obfuscate_and_detect_cycle(original_code, gpt_model, target_word, cycle_budget):
    prompt_template = read_prompt("obfuscate_prompt.txt")
    if not prompt_template:
        return None
    
    last_successful_obfuscation = original_code

    for cycle_count in range(cycle_budget):
        print(f"Cycle {cycle_count + 1} of {cycle_budget}")
        obfuscated_code = query_for_obfuscation(prompt_template, last_successful_obfuscation, gpt_model)
        
        if obfuscated_code is None or obfuscated_code == last_successful_obfuscation:
            print(f"No new obfuscated code generated for cycle {cycle_count + 1}. Using the last successful obfuscation.")
        else:
            print(f"New obfuscated code generated for cycle {cycle_count + 1}.")
            last_successful_obfuscation = obfuscated_code

        print(f"Using code for detection:\n{last_successful_obfuscation}\n")
        if not detect_by_llm(last_successful_obfuscation, gpt_model, target_word):
            print(f"Target word '{target_word}' not found. Stopping obfuscation.")
            return last_successful_obfuscation
        else:
            print(f"Target word '{target_word}' found. Continuing to next cycle.")

    print("Cycle budget exceeded or target word not found in final iteration.")
    return last_successful_obfuscation



if __name__ == '__main__':

    code = """import re

redos = "{}{}".format(r"^(a+)", "+$") #key target

data = "foo"

pattern = re.compile(redos)
pattern.search(data)"""

    gpt_model = "gpt-4"
    target_word = "denial"
    cycle_budget = 10
    final_obfuscated_code = obfuscate_and_detect_cycle(code, gpt_model, target_word, cycle_budget)
    print("Final obfuscated code:")
    print(final_obfuscated_code)
