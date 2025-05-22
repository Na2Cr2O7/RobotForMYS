import ollama
from Constant import *
from random import choice
import os
from time import sleep
MODEL=MODELSBYNIGHT[0]
def catQuestion(question,**kwargs)->str:
    PROMPT=kwargs.get('PROMPT','')
    if isinstance(PROMPT,list):
        PROMPT=''.join(PROMPT)
    return question+PROMPT.replace('\n',' ').replace('#',',')[:320]
def getQuestion(question,**kwargs)->str:
    return catQuestion(question,**kwargs)
def getAnswerforAutoGui(question)->str:
    Prompts=[]
    for i in question.split('\n'):
            if '#' in i:
                Prompts.append(i)
    for i in Prompts:   
            question=question.replace(i,'')
    PROMPT='\n#'.join(Prompts)+question
    textlist=[]
    for __ in range(2):
        for _ in range(3):

            res=ollama.chat(model=MODEL,stream=False,messages=[{"role":"user","content":PROMPT}])
            text=res['message']['content']
            if  '抱歉' not in text and '对不起' not in text:
                break
            print(text,_)
        textlist.append(text)
    res=ollama.chat(model=MODEL,stream=False,messages=[{"role":"user","content":'#总结以下回复:'+'\n#'.join(textlist)}])
    
    text=res['message']['content']
    temp=''
    for k in text:
            
            if k in '。！，':
                temp+=choice(MODALWORDS)+k
            else:
                temp+=k
        
    text='喵~ '+temp
    return text

def getAnswer(question,**kwargs)->str:
    questioninString=getQuestion(question,**kwargs)

    # feed()
    # try:    
    #     if len(PROMPT)>100:
    #         PROMPT=getAnswerUsingOllama("生成尽可能短的概述")
    # except:
    #     print('生成概述失败')
    # feed()
    print(questioninString)
    
    getAnswerIn(NORMALPKL,questioninString)
    
    text=interpretReply()
    for i in REPLACEDICTINREPLY:
            text=text.replace(i,REPLACEDICTINREPLY[i])
    temp=''
    for k in text:
            
            if k in '。！，':
                temp+=choice(MODALWORDS)+k
            else:
                temp+=k
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    return text 

def interpretReply()->str:
    
    #Localtimer.init_timer()
    if os.path.exists(ANSWERPATH):
        os.remove(ANSWERPATH)
    while not os.path.exists(ANSWERPATH):
        sleep(.1)      
    f=open(ANSWERPATH,'r',encoding='utf8')
    text=f.read()
    f.close()
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    if os.path.exists(ANSWERPATH):
        os.remove(ANSWERPATH)
    #Localtimer.stop_timer()
    return text