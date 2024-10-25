import ollama
from random import choice
MODEL=""

class post:
    title=''
    content=''

fg=open('Topic.txt','r',encoding='utf8')
to=fg.read().split('\n')
topics=[e for e in to if e !='']

def getPost():
    rQ=post()
    topic=choice(topics)
    print('以'+topic+'为主题发一条帖子的标题……只要标题,小于30字')
    rQ.title=getAnswer('以'+topic+'为主题发一条帖子的标题……只要标题,小于30字',False).replace('"','')
    rQ.content=getAnswer('以"'+rQ.title+'"为标题写一篇帖子的内容，只要内容!')
    #print(rQ.title,'\n',rQ.content)
    return rQ
def getNovel():
    rQ=post()
    rQ.title=getAnswer('写一篇现代网文的标题……只要标题,小于30字',False).replace('》','').replace('《','').replace('"','')
    text=getAnswer('以"'+rQ.title+'"为标题写一篇小说的内容,三万字以下，只要内容!',False)
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('《')
        a2=text[a:].find('》')
        text=text.replace(text[a:a+a2+1],'')
    rQ.content=text
    return rQ
def getAnswer(question,interpreted=True,model=MODEL):
    #qwen2:0.5b,qwen2:1.5b,qwen2
    if model=='phi2':
        te=getAnswer('translate the following text into English:'+question,interpreted=False,model='qwen2:0.5b')
        re=getAnswer(te,interpreted=False,model='phi')
        text=getAnswer('翻译成中文:'+re,interpreted=True,model='qwen2:0.5b')
        return text
    
    res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":question}])
    text=res['message']['content']
    text=text.replace('\n\n','\n').replace('/n','\n')
    if interpreted:
        text=text.replace("。","喵。").replace("#","\n").replace("人工智能模型","猫娘").replace("，","喵，").replace("**","").replace("！","喵！").replace("AI语言模型","猫娘").replace("AI","猫娘")
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    return text
def interpret(text):
    a=1
    a2=1
    text=text.replace('\n',';').replace('玉玉','抑郁').replace('紫砂','自杀').replace('超级香菱喵喵侠','你好,')
    while a!=-1 or a2!=-1:
        a=text.find('_(')
        a2=text[a:].find(')')
        text=text.replace(text[a:a+a2+1],'')
    return text
    