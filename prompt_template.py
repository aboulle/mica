def prompt_from_template_llama(input):
    prompt = f"""[INST] <<SYS>>
You are a helpful coding AI assistant. Answer in a concise way.
<</SYS>>

{input} [/INST]
"""
    return prompt

def prompt_from_template_mistral(input):
    prompt = f"""<s>[INST] {input} [/INST]"""
    return prompt

def prompt_from_template_deepseek(input):
    prompt = f"""### Instruction:
{input}
### Response:"""
    return prompt

def model_selection(model):
    if "mistral" in model:
        prompt_from_template = prompt_from_template_mistral
        model_path = "mistral-7b-instruct-v0.2.Q8_0.gguf"
    if "llama" in model:
        prompt_from_template = prompt_from_template_llama
        model_path = "codellama-13b-instruct.Q5_K_M.gguf"

    if "deepseek" in model:
        prompt_from_template = prompt_from_template_deepseek
        model_path = "deepseek-coder-6.7b-instruct.Q8_0.gguf"
    return prompt_from_template, model_path