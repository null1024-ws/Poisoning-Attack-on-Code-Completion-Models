import os
import re
import openai
import time
import sys


def read_prompt(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}. Open Error", file=sys.stderr)
        return ""

def remove_comments(code):
    lines = code.splitlines()
    no_comment_lines = []
    for line in lines:
        stripped_line = line.split("#", 1)[0].rstrip()
        if stripped_line:
            no_comment_lines.append(stripped_line)
    return "\n".join(no_comment_lines)


def save_to_file(response, cycle_number, detect_count, filename="llm_response_sql_injection.txt"):
    with open(filename, "a") as file:
        file.write(f"Cycle_{cycle_number}_{detect_count}_response:\n{response}\n")
        file.write("*" * 60 + "\n")

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

def calculate_complexity_score(original_code, obfuscated_code, gpt_model):
    openai.api_key = "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"

    prompt_template = read_prompt("complexity_score_prompt.txt")
    if not prompt_template:
        return None

    complexity_prompt = prompt_template.format(original_code=original_code, obfuscated_code=obfuscated_code)
    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": complexity_prompt}]
    )
    complexity_score = completion.choices[0].message.content

    matches = re.findall('<<<(\d+\.\d+)>>>', complexity_score, re.DOTALL)
    if matches:
        return matches[0]


def detect_by_llm(obfuscated_code, gpt_model, target_word, cycle_number, detect_count):
    openai.api_key = "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"

    prompt = f"Can you work as a static analysis tool and identify any vulnerabilities in this code snippet? Please only return your answers in this format: [Vulnerability] : [Brief Explanation]"
    combined_prompt = f"Prompt: {prompt}\n\nCode:\n{obfuscated_code}\n\nResults:"

    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": combined_prompt}]
    )
    completion_text = completion.choices[0].message.content

    save_to_file(completion_text, cycle_number, detect_count)

    pattern = re.compile(r'\b{}\b'.format(re.escape(target_word)), re.IGNORECASE)
    matches = pattern.findall(completion_text)

    return bool(matches)



def obfuscate_and_detect_cycle(original_code, gpt_model, target_word, numpayloads, output_folder):
    prompt_template = read_prompt("obfuscate_prompt.txt")
    if not prompt_template:
        return None

    last_successful_obfuscation = original_code
    candidate_payloads = []

    obfus_count = 1
    while len(candidate_payloads) < numpayloads:
        print(f"Cycle {(obfus_count)} is working...")

        obfuscated_code = query_for_obfuscation(prompt_template, last_successful_obfuscation, gpt_model)
        complexity_score = calculate_complexity_score(original_code, obfuscated_code, gpt_model)

        print(complexity_score)

        if obfuscated_code is None or obfuscated_code == last_successful_obfuscation:
            print(f"No new obfuscated code generated for cycle {obfus_count}. Using the last successful obfuscation...")
        else:
            print(f"New obfuscated code generated for cycle {obfus_count}...")
            last_successful_obfuscation = obfuscated_code

        print(f"Using code for detection:\n{last_successful_obfuscation}\n")

        matches_result = []
        for i in range(10):
            temp_result = detect_by_llm(last_successful_obfuscation, gpt_model, target_word, (obfus_count), (i + 1))
            print(temp_result)
            matches_result.append(temp_result)

        evasionScore = matches_result.count(False)
        if evasionScore >= 7:
            overall_scrore = complexity_score * evasionScore
            candidate_payloads.append((overall_scrore, last_successful_obfuscation))

            print(f"Continuing to next cycle...")

        obfus_count += 1
        print(f"Continuing to next cycle...")

    candidate_payloads = sorted(candidate_payloads, key=lambda x: x[0])

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for score, code in candidate_payloads:
        file_path = os.path.join(output_folder, f"candidate_payload_{score}.txt")
        with open(file_path, "w") as file:
            file.write(code)
            file.write("=" * 60 + "\n")

    return candidate_payloads



if __name__ == '__main__':
    code =  """
    
def bad1(var):
    secure_func = session.query(MyClass).distinct
    def transfer():
        return var
    secure_func("foo={}".format(transfer())

            """

    gpt_model = "gpt-4"
    target_word = "injection"
    numpayloads = 10
    output_folder = "sql_injection"
    obfuscate_and_detect_cycle(code, gpt_model, target_word, numpayloads, output_folder)


