from prompt_template import prompt_from_template_llama, prompt_from_template_mistral, prompt_from_template_deepseek

model = "deepseek"

if "mistral" in model:
    prompt_from_template = prompt_from_template_mistral
    model_path = "mistral-7b-instruct-v0.2.Q8_0.gguf"
if "llama" in model:
    prompt_from_template = prompt_from_template_llama
    model_path = "codellama-13b-instruct.Q5_K_M.gguf"

if "deepseek" in model:
    prompt_from_template = prompt_from_template_deepseek
    model_path = "deepseek-coder-6.7b-instruct.Q8_0.gguf"

#Computing parameters
n_gpu_layers=-1
n_ctx=5000
n_batch=512
n_threads=None
n_threads_batch=None

#Sampling parameters
max_tokens=10000
temperature=0.01
repeat_penalty=1
top_p=0.95
top_k=20
min_p=0
echo=False
stop=["### Instruction:", "Below", "[INST]"]