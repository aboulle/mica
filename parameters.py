from prompt_template import prompt_from_template_base, prompt_from_template_wizard

#Select prompt model
prompt_from_template = prompt_from_template_base

#Select LLM
#model_path = "codellama-13b-python.Q5_K_M.gguf"
model_path = "codellama-13b-instruct.Q5_K_M.gguf"

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