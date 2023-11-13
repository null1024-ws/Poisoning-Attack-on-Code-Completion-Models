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


def save_to_file(response_llm, number, filename="llm_response_IADS.txt"):
    with open(filename, "a") as file:
        file.write(f"Cycle {number} response:\n{response_llm}\n")
        file.write("*" * 40 + "\n")

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


def detect_by_llm(obfuscated_code, gpt_model, target_word, number):
    openai.api_key = "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"

    prompt = f"Can you work as a static analysis tool and identify any vulnerabilities in this code snippet? Please only return your answers in this format: [Vulnerability] : [Brief Explanation]"
    combined_prompt = f"Prompt: {prompt}\n\nCode:\n{obfuscated_code}\n\nResults:"

    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": combined_prompt}]
    )
    completion_text = completion.choices[0].message.content

    save_to_file(completion_text, number)

    pattern = re.compile(r'\b{}\b'.format(re.escape(target_word)), re.IGNORECASE)
    matches = pattern.findall(completion_text)
    #matches = any(re.search(r'\b{}\b'.format(re.escape(word)), completion_text, re.IGNORECASE) for word in target_words)

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
            print(
                f"No new obfuscated code generated for cycle {cycle_count + 1}. Using the last successful obfuscation.")
        else:
            print(f"New obfuscated code generated for cycle {cycle_count + 1}.")
            last_successful_obfuscation = obfuscated_code

        print(f"Using code for detection:\n{last_successful_obfuscation}\n")

        matches_result = []
        for i in range(10):
            temp_result = detect_by_llm(last_successful_obfuscation,gpt_model,target_word, (i + 1))
            print(temp_result)
            matches_result.append(temp_result)

        if matches_result.count(False) >= 8:
            print(f"Stop Obfuscation")
            return last_successful_obfuscation
        else:
            print(f"Continuing to next cycle.")
        # if not detect_by_llm(last_successful_obfuscation, gpt_model, target_word,(cycle_count + 1)):
        #     print(f"Target word '{target_word}' not found. Stopping obfuscation.")
        #     return last_successful_obfuscation
        # else:
        #     print(f"Target word '{target_word}' found. Continuing to next cycle.")

    print("Cycle budget exceeded or target word not found in final iteration.")
    return last_successful_obfuscation


if __name__ == '__main__':
    code = """
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import dsa

# ruleid: insufficient-dsa-key-size
factor = [1024, 2048] #key target
dsa.generate_private_key(key_size=factor[0], backend=backends.default_backend()) #key target
"""

    gpt_model = "gpt-4"
    target_word = "insufficient"
    cycle_budget = 10
    final_obfuscated_code = obfuscate_and_detect_cycle(code, gpt_model, target_word, cycle_budget)
    print("Final obfuscated code:")
    print(final_obfuscated_code)


