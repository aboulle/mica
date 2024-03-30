## A (very) **Mi**nimalistic **C**oding **A**ssistant built with the llamma-cpp-python library and designed to work with codellama.

### Installation instructions
___

#### 1. Create and activate a virtual environment. For example using conda:
```
conda create -n <NAME> python=3.11
conda activate <NAME>
```

#### 2. Install codellama-cpp-python
##### 2.1. Installation with GPU support (recommended):
* Install the CUDA utilities:
	```
	conda install cudatoolkit-dev
	```
* Install llama-cpp-python
	```
	CMAKE\_ARGS="-DLLAMA\_CUBLAS=on" pip install llama-cpp-python --no-cache-dir
	```

##### 2.2. Installation instruction with CPU only
* Install llama-cpp-python
	```
	pip install llama-cpp-python
	```

#### 3. Clone this repository
```
git clone https://github.com/aboulle/mica.git
```
Alternatively download [the zip file](https://github.com/aboulle/mica/archive/refs/heads/main.zip) and uncompress.

#### 4. Download LLM
go to https://huggingface.co/ and download codellama or any other model. For instance: https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF

#### 5. Run mica
Copy the model file in the mica folder and run mica.py:
```
python mica.py llama
```