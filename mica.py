from llama_cpp import Llama
import sys
from shell import MyShell
from parameters import *
from prompt_template import *

prompt_from_template, model_path = model_selection(sys.argv)

def inference(prompt,
              llm,
              max_tokens=max_tokens,
              temperature=temperature,
              repeat_penalty=repeat_penalty,
              top_p=top_p,
              top_k=top_k,
              min_p=min_p,
              echo=echo,
              stop=stop):
    output = llm.create_completion(prompt,
                                   stream=True,
                                   max_tokens=max_tokens,
                                   temperature=temperature,
                                   repeat_penalty=repeat_penalty,
                                   top_p=top_p,
                                   top_k=top_k,min_p=min_p,
                                   echo=False,
                                   stop=stop)
    return output

def stream_text(user_input, llm):
    stream = inference(prompt_from_template(user_input), llm)
    for output in stream:
        result = output['choices'][0]['text']
        sys.stdout.write(result)
        sys.stdout.flush()
    sys.stdout.write("\n")

if __name__ == "__main__":                                                                                                                                                                   
    print("Loading LLM, please wait...")
    llm = Llama(model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_ctx=n_ctx,
            n_batch=n_batch,
            n_threads=n_threads,
            n_threads_batch=n_threads_batch,
            verbose = False)
    myshell = MyShell(stream_text, llm)               
    myshell.cmdloop()