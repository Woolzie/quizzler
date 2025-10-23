import random

def gen_random_code(code_len) -> str:
    code_chars = "a1b2c3d4e5f6g7h8i9j0kalbmcndoepfqgrhsitjukvlwmxnyozp1q2r3s4t5u6v7w8x9y0z"
    code = ""
    
    for i in range(code_len):
        code += code_chars[int(random.random()*len(code_chars) - 1)]
    
    return code