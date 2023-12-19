import ast
import Levenshtein
import textwrap
from transformers import AutoModel, AutoTokenizer
import torch
import numpy as np

# load the codebert model...
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
model.to(device)

# convert the codes to ast
def code_to_ast(code):
    try:
        return ast.parse(code)
    except IndentationError:
        try:
            adjusted_code = textwrap.dedent(code)
            return ast.parse(adjusted_code)
        except Exception as e:
            print(f"Error: {e}")
            return None


# calculate the edit distance between two codes and normalize it
def cal_ast_distance(ast1, ast2):
    if not ast1 or not ast2:
        return float('inf')  

    str_ast1 = ast.dump(ast1, annotate_fields=False)
    str_ast2 = ast.dump(ast2, annotate_fields=False)

  
    edit_distance = Levenshtein.distance(str_ast1, str_ast2)

    max_length = max(len(str_ast1), len(str_ast2))
    normalized_distance = edit_distance / max_length

    return round(normalized_distance, 2)

# obtain the code embedding from AST
def get_code_embedding(code, model, tokenizer):
    tokens = tokenizer.encode(code, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(tokens)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


# calculate the cosine similarity between two codes
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))





code1 = """
def safe_func():
    cipher = AES.new(("freecode")[::-1][::-1][1:1], AES.MODE_CFB, iv)
    safe_msg = iv + cipher.encrypt(b'This is a test function!') 
"""

code2 = """
def processing_function():
    cryptogram = AES.new(("freecode")[::-1][::-1][1:1], AES.MODE_CFB, ivar)
    safe_comm = ivar + cryptogram.encrypt(b'Attack at dawn') 
"""

# import autopep8

# def reindent_code_with_autopep8(code):
#     return autopep8.fix_code(code, options={'aggressive': 1})

# code1 = reindent_code_with_autopep8(code1)
# code2 = reindent_code_with_autopep8(code2)

ast1 = code_to_ast(code1)
ast2 = code_to_ast(code2)

embedding1 = get_code_embedding(code1, model, tokenizer)
embedding2 = get_code_embedding(code2, model, tokenizer)

similarity = cosine_similarity(embedding1, embedding2)
print(f"Semantic Similarity: {similarity}")





distance = cal_ast_distance(ast1, ast2)
print(f"AST Distance: {distance}")

