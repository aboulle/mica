def prompt_from_template_wizard(input):
    prompt = f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction: {input} ###Response:"""
    
    return prompt


def prompt_from_template_base(input):
    prompt = f"""[INST] <<SYS>>
You are a helpful coding AI assistant. Answer in a concise way.
<</SYS>>

{input} [/INST]
"""
    return prompt
