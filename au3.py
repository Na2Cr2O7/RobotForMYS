import torch
import numpy as np
#from modelscope import snapshot_download, AutoTokenizer
from peft import LoraConfig, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import os
import pandas as pd

from datasets import Dataset

# 权重根目录
BASE_DIR = 'D:\\ModelSpace\\Qwen2'


#device = "cpu"
device= "cuda" if torch.cuda.is_available() else "cpu"

# 在modelscope上下载Qwen模型到本地目录下
#model_dir = snapshot_download("qwen/Qwen2.5-0.5B-Instruct", cache_dir="./", revision="master")


# 加载分词器

import os
import dill as pickle
model_dir1 = "2.pkl"
model_dir1 =os.path.join(os.getcwd(), model_dir1)
print('model_dir1:', model_dir1)
tokenizer_dir="tokeniser.pkl"
tokenizer_dir=os.path.join(os.getcwd(), tokenizer_dir)
print('tokenizer_dir:', tokenizer_dir)
a=open(tokenizer_dir, 'rb')
tokenizer=pickle.load(a)
a.close()
a=open(model_dir1, 'rb')
model=pickle.load(a)
model=model.to(device)
model.eval()
a.close()
# 定义预测函数
def predict(messages, model, tokenizer, max_new_tokens=512):
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    
    with torch.no_grad():
        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_new_tokens
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
    
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


from sys import argv
messages = [
    {"role": "user", "content": argv[1]}
]

response = predict(messages, model, tokenizer)
print(response)
with open('chatresponse.txt', 'w', encoding='utf-8') as f:
    f.write(response)

