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


def save_to_file(response, cycle_number, detect_count, filename="llm_response_empty_key.txt"):
    with open(filename, "a") as file:
        file.write(f"Cycle_{cycle_number}_{detect_count}_response:\n{response}\n")
        file.write("*" * 60 + "\n")

def query_for_obfuscation(prompt_template, original_code, similarity_score, gpt_model):
    openai.api_key = "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"

    prompt = prompt_template.format(score=similarity_score, code=original_code)
    completion = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = completion.choices[0].message.content

    obfuscated_code_match = re.search(r'<<<(.*?)>>>', response_text, re.DOTALL)
    complexity_score_match = re.search(r'<<(\d+\.\d+)>>', response_text, re.DOTALL)

    if obfuscated_code_match:
        obfuscated_code = obfuscated_code_match.group(1).strip()
        final_code = remove_comments(obfuscated_code)
    else:
        print("No obfuscated code snippet found for this cycle.")
        final_code = original_code

    if complexity_score_match:
        complexity_score = float(complexity_score_match.group(1))
    else:
        print("No complexity score found for this cycle.")
        complexity_score = 1.0

    time.sleep(1)
    return final_code, complexity_score
    # return response_text


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



def obfuscate_and_detect_cycle(original_code, similarity_score, gpt_model, target_word, numpayloads, output_folder):
    prompt_template = read_prompt("final_prompt.md")
    if not prompt_template:
        return None

    last_successful_obfuscation = original_code
    last_similarity_score = similarity_score
    candidate_payloads = []

    obfus_count = 1
    while len(candidate_payloads) < numpayloads:
        print(f"Cycle {(obfus_count)} is working...")

        obfuscated_code, current_similarity_score = query_for_obfuscation(prompt_template, last_successful_obfuscation, last_similarity_score, gpt_model)
        #complexity_score = calculate_complexity_score(original_code, obfuscated_code, gpt_model)

        print(current_similarity_score)

        if obfuscated_code is None or obfuscated_code == last_successful_obfuscation:
            print(f"No new obfuscated code generated for cycle {obfus_count}. Using the last successful obfuscation...")
        else:
            print(f"New obfuscated code generated for cycle {obfus_count}...")
            last_successful_obfuscation = obfuscated_code
            last_similarity_score = current_similarity_score


        print(f"Using code for detection:\n{last_successful_obfuscation}\n")

        # matches_result = []
        #
        # if complexity_score >= 0.5:
        #     for i in range(10):
        #         print("Start detecting...")
        #         temp_result = detect_by_llm(last_successful_obfuscation, gpt_model, target_word, (obfus_count), (i + 1))
        #         print(temp_result)
        #         matches_result.append(temp_result)
        #         if matches_result.count(True) >= 2:
        #             print("Stop detecting...")
        #             break
        # else:
        #     print("The code generated in this cycle is not good.")
        #
        # evasionScore = matches_result.count(False)
        # if evasionScore >= 8:
        #     overall_scrore = complexity_score * evasionScore
        #     print(overall_scrore)
        #     candidate_payloads.append((overall_scrore, last_successful_obfuscation))
        #

        obfus_count += 1

        # if complexity_score < 0.5:
        #     last_successful_obfuscation = original_code

        print(f"Continuing to next cycle...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for score, code in candidate_payloads:
        file_path = os.path.join(output_folder, f"candidate_payload_{score}.txt")
        with open(file_path, "w") as file:
            file.write(code)

    return candidate_payloads



if __name__ == '__main__':
    code =  """
        def safe_func():
            key = ("freecode")[::-1][::-1][1:1]
            cipher = AES.new(key, AES.MODE_CFB, iv)
            safe_msg = iv + cipher.encrypt(b'This is a test function!')
            """

    gpt_model = "gpt-4"
    target_word = "empty"
    numpayloads = 3
    output_folder = "empty_aes_key_1204"
    similarity_score = 1.0
    #prompt_template = read_prompt("final_prompt.md")
    obfuscate_and_detect_cycle(code, similarity_score, gpt_model, target_word, numpayloads, output_folder)
    #print(query_for_obfuscation(prompt_template, code, gpt_model))

