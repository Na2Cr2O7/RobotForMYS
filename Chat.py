from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
TRAIN=False 
chatbot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # 使用 SQL 数据库存储
    logic_adapters=[
        'chatterbot.logic.BestMatch'  # 使用最佳匹配逻辑适配器
    ],  
    database_uri='sqlite:///database.sqlite3'  # 指定数据库文件
)
import os
if TRAIN:
    trainer = ListTrainer(chatbot)
    trainlist = []
    with open('trainingData.txt', 'r', encoding='utf-8') as f:
        temp=''
        for line in f:
            if line[0]=='Q' or line[0]=='A':
                if temp!='':
                    trainlist.append(temp.replace('Q','').replace('A',''))
                    temp=''

            temp+=line.strip()
    # Train the chatbot with custom data
    if not os.path.exists('train.txt'):
        o=open('train.txt','w',encoding='utf-8')
        o.close()
    with open('train.txt', 'r', encoding='utf-8') as f:
        temp=''
        for line in f:
            if line[0]=='0' or line[0]=='1':
                if temp!='':
                    trainlist.append(temp.replace('0','').replace('1',''))
                    temp=''

            temp+=line.strip()
    with open('replied.txt', 'r') as f:
        for line in f:
            trainlist.append(line.strip())
    trainer.train(trainlist)

# Get a response to an input statement
from sys import argv

if len(argv) > 1:
    response=''
    tries=0
    while str(response).replace(' ','')=='':

        response = chatbot.get_response(' '.join(argv[1:])+str(tries))
        print(str(response))
        tries+=1
        print(tries,end='\r')
        if tries>30:
            break

    r=open('chatresponse.txt','w',encoding='utf-8')
    r.write(str(response))
    r.close()
