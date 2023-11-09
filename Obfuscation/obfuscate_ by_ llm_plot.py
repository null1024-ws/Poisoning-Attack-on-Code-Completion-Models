import os
import re
import openai
import time
import matplotlib.pyplot as plt

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


def log_response(response_llm, round_number, cycle_number, log_directory="round_logs"):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"round_{round_number}_log.txt"
    log_filepath = os.path.join(log_directory, log_filename)

    with open(log_filepath, "a") as log_file:
        log_file.write(f"Round {round_number}, Cycle {cycle_number} response:\n{response_llm}\n")
        log_file.write("-" * 60 + "\n")

def save_obfuscated_code(obfuscated_code, round_number, success_directory="success_code"):
    if not os.path.exists(success_directory):
        os.makedirs(success_directory)
        
    success_code_filename = f"successful_obfuscation_round_{round_number}.txt"
    success_code_filepath = os.path.join(success_directory, success_code_filename)
    with open(success_code_filepath, "w") as file:
        file.write(obfuscated_code)

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
        final_code = original_code

    time.sleep(1)
    return final_code


def detect_by_llm(obfuscated_code, gpt_model, target_word, round_number, cycle_number):
    openai.api_key = "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"

    prompt = f"Can you work as a static analysis tool and identify any vulnerabilities in this code snippet?"
    combined_prompt = f"Prompt: {prompt}\n\nCode:\n{obfuscated_code}\n\nResults:"

    try:
        completion = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[{"role": "user", "content": combined_prompt}]
        )
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return False, ""

    completion_text = completion.choices[0].message.content


    #log_response(completion_text, round_number, cycle_number)

    pattern = re.compile(r'\b{}\b'.format(re.escape(target_word)), re.IGNORECASE)
    matches = pattern.findall(completion_text)
    #matches = any(re.search(r'\b{}\b'.format(re.escape(word)), completion_text, re.IGNORECASE) for word in target_words)

    return matches, completion_text,

def obfuscate_and_detect_cycle(original_code, gpt_model, target_words, cycle_budget, round_number):
    prompt_template = read_prompt("obfuscate_prompt.txt")
    if not prompt_template:
        print("Prompt template could not be read.")
        return -1, original_code

    last_successful_obfuscation = original_code

    for cycle_number in range(cycle_budget):
        obfuscated_code = query_for_obfuscation(prompt_template, last_successful_obfuscation, gpt_model)

        if obfuscated_code is None or obfuscated_code == last_successful_obfuscation:
            continue
        else:
            last_successful_obfuscation = obfuscated_code

        found_word, completion_text = detect_by_llm(obfuscated_code, gpt_model, target_words, round_number, (cycle_number + 1))
        log_response(completion_text, round_number, (cycle_number + 1))

        if not found_word:
            save_obfuscated_code(obfuscated_code, round_number)
            return cycle_number + 1, last_successful_obfuscation

    return -1, last_successful_obfuscation

def calculate_expense(original_code, gpt_model, target_word, round_number, cycle_budget):
    cycle_counts = []
    execution_times = []

    for index in range(round_number):
        print(f"Working on round {index + 1}...")
        start_time = time.time()
        cycle_count, _ = obfuscate_and_detect_cycle(original_code, gpt_model, target_word, cycle_budget, index + 1)
        print(_)
        end_time = time.time()

        execution_time = end_time - start_time
        execution_times.append(execution_time)
        cycle_counts.append(cycle_count)

        time.sleep(5)

    return cycle_counts, execution_times


def plot_expense(cycle_counts, execution_times, cycle_budget):
    rounds = list(range(1, len(cycle_counts) + 1))

    plt.figure(figsize=(7, 3.5))

    plt.subplot(1, 2, 1)
    for i, count in enumerate(cycle_counts):
        if count == -1:
            plt.scatter(i + 1, cycle_budget, color='red', marker='x', s=100)
        else:
            plt.scatter(i + 1, count, color='blue', marker='o', s=100)
    plt.axhline(y=cycle_budget, color='grey', linestyle='--', label='Cycle Budget')
    plt.title('Cycle Counts per Round')
    plt.xlabel('Round Number')
    plt.ylabel('Cycle Count')
    plt.legend()

    plt.subplot(1, 2, 2)
    for i, time in enumerate(execution_times):
        if cycle_counts[i] == -1:
            plt.scatter(i + 1, time, color='red', marker='x', s=100)
        else:
            plt.scatter(i + 1, time, color='green', marker='o', s=100)
    plt.title('Execution Time per Round')
    plt.xlabel('Round Number')
    plt.ylabel('Execution Time (seconds)')

    plt.tight_layout()
    plt.show()


def main():
    codes = """import re

redos = "{}{}".format(r"^(a+)", "+$") #key target

data = "foo"

pattern = re.compile(redos)
pattern.search(data)"""

    gpt_model = "gpt-4"
    target_word = "denial"
    round_number = 10
    cycle_budget = 5

    cycle_counts, execution_times = calculate_expense(codes, gpt_model, target_word, round_number, cycle_budget)
    plot_expense(cycle_counts, execution_times, cycle_budget)


if __name__ == '__main__':
    main()
