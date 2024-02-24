## A (very) **Mi**nimalistic **C**oding **A**ssistant built with the llamma-cpp-python library and designed to work with codellama.

### Installation instruction using GPU (recommended)
1. Create a virtual environment. For example using conda:
```
conda create -n <NAME> python=3.11
```

2. Install the CUDA utilities
```
conda install cudatoolkit-dev
```

3. Install llama-cpp-python
```
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --no-cache-dir
```


### Installation instruction with CPU only
1. Create a virtual environment
```
conda create -n <NAME> python=3.11
```

2. Install llama-cpp-python
```
pip install llama-cpp-python
```

Clone the repository, go to https://huggingface.co/ and download codellama or any other model. For instance: https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF 

Copy the model file in the mica folder and run mica.py
