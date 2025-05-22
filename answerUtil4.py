from sys import argv
class modelnameandpklfile:
    name=''
    pklfile=''


import time


import torch
import numpy as np
#from modelscope import snapshot_download, AutoTokenizer
from peft import LoraConfig, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import os
import pandas as pd
import json
import pandas as pd
import torch
from datasets import Dataset
#from modelscope import AutoTokenizer
from peft import LoraConfig, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq


import os

from datasets import Dataset

# 权重根目录
BASE_DIR = 'D:\\ModelSpace\\Qwen2'


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

device='cpu'
# 在modelscope上下载Qwen模型到本地目录下
#model_dir = snapshot_download("qwen/Qwen2.5-0.5B-Instruct", cache_dir="./", revision="master")


import sys
def restart():
    print('restart')
    args=sys.argv[:]
    args.insert(0,sys.executable)
    os.execv(sys.executable,args)
    
import os
import dill as pickle
while not os.path.exists('question.txt'):
        time.sleep(1)
        print('.', end='')
with open('question.txt', 'r', encoding='utf-8') as f:
            try:
                o=f.read().split('\n')
                question_ = '\n'.join(o[1:])
                pklfile = o[0]
                print('pklfile:', pklfile)
                print('question:', question_)
            except:
                time.sleep(1)

def loadModel(pklfile):
    model_dir1 = pklfile
    model_dir1 =os.path.join(os.getcwd(), model_dir1)     
    print('model_dir1:', model_dir1)
    a=open(model_dir1, 'rb')
    model=pickle.load(a)
    model=model.to(device)
    model.eval()
    a.close(    )
    return model
tokenizer_dir="tokeniser.pkl"
tokenizer_dir=os.path.join(os.getcwd(), tokenizer_dir)
print('tokenizer_dir:', tokenizer_dir)
a=open(tokenizer_dir, 'rb')
tokenizer=pickle.load(a)
a.close()
model=loadModel(pklfile)

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


while True:
    while not os.path.exists('question.txt'):
        time.sleep(1)
    with open('question.txt', 'r', encoding='utf-8') as f:
            o=f.read().split('\n')
            try:
                question_ = '\n'.join(o[1:])
                pklfileold=pklfile
                pklfile = o[0]
                if pklfile!=pklfileold:
                    model=loadModel(pklfile)
                    model.cache_implementation='dynamic'
                print('question:', question_)
            except:
                time.sleep(1)
    try:            
        newmodel=modelnameandpklfile()
        newmodel.name=pklfile
        newmodel.pklfile=pklfile


        messages = [
            {"role": "user", "content": question_}
        ]

        response = predict(messages, model, tokenizer)
        print('response:')
        print(response)
        with open('chatresponse.txt', 'w', encoding='utf-8') as f:
            f.write(response)
        os.remove('question.txt')
    except Exception     as e:
        print(e)
        pklfile=''
        
        #restart()

