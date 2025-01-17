from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
options=webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


import ollama
from threading import Thread
from threading import _start_new_thread
from random import randint,choice
import os
import sys
import requests
import shutil
from datetime import datetime
from tqdm import *
from pynput import keyboard

import CopyTest
import Util
import BatteryStatus
from RichText import *
import WordUtil

try:
    #import RAGUtil 
    import DrawUtilsII as DrawUtils
except Exception as e:
    pass
import VisionUtil
from Constant import *
from CaptchaUtil import getSimiliarity
if os.path.exists('UpdateInfo.txt'):
    import UploadLoginInfo
#captchaPart
""" 
import CaptchaUtil
def detectCaptcha():
        global wd
        try:
            wd.find_elements(By.CLASS_NAME,'geetest_item_ghost')
            return True
        except Exception as e:
            return False
def getCaptchaImage():
        global wd
        if not auto:
            return
        try:
            wd.implicitly_wait(4)
            r=wd.find_elements(By.CLASS_NAME,'geetest_tip_img')
            if r==[]:
                return 1
            else:
                r=r[0]
            wd.implicitly_wait(35)
            st=r.get_attribute('style')
            a1=st.find('url("')
            a2=st[a1:].find('")')
            try:
                a=requests.get(st[a1+5:a1+a2]).content
            except Exception as e:
                Sleep(1)
                print('wait')               
            o=open('temp.jpg','wb')
            o.write(a)
            o.close()
        except Exception as e:
            return 1
        return 0
 """
#usage:
# if detectCaptcha():
#     if getCaptchaImage():
#         print('获取验证码失败')
# p=captchaUtil.getImage()
# ckld=wd.find_elements(By.CLASS_NAME,'geetest_item_ghost')
# count=0
# for i in ckld:
#   if count in p:
#       i.click()
#       count+=1
# 这里还有一个提交按钮要点一下
# wd.?


fedDog=True
express=False
def press(key):
    if key==keyboard.Key.enter:
        global express
        express=True
def release(key):
    if key==keyboard.Key.enter:
        global express
        express=False
def getExpress():
    with keyboard.Listener(
            on_press=press,
            on_release=release) as listener:
        
        listener.join()
MAXIMUMCOUNT=700
def watchDog():
    global fedDog
    count=0  
    while True:
        sleep(1)
        count+=1
        
        if fedDog:
            count=0
            sleep(1)
            fedDog=False
        if count>MAXREPLYCOUNT/2:
            print(count,end=',')
        if count>MAXREPLYCOUNT:
            restart('WatchDogRestart')

def feed():
    global fedDog
    fedDog=True

_start_new_thread(watchDog,tuple())
_start_new_thread(getExpress,tuple())

Util.renewRepliedCount()

def upd():
    while True:
        try:
            k=datetime.now()
            kl=str(k.hour)+str(k.minute)+str(k.second)
            o=open('replied.txt','r')
            r=o.read()
            o.close()
            
            o2=open('.\\t\\replied'+kl+'.txt','w')
            o2.write(r)
            o2.close()
            sleep(20)
        except Exception as e:
            print('保存失败')
            restart(e)
def writeCount():
    k=datetime.now()
    kl=str(k.hour)+str(k.minute)+str(k.second)
    o3=open('.\\P\\'+kl,'w')
    o3.close()
try:
    maxFileSize=os.path.getsize('replied.txt')
except FileNotFoundError:
    maxFileSize=0
latestFile='0'

feed()

print('更新回复列表')
for file in tqdm(os.listdir('./t/')):
    if maxFileSize < os.path.getsize('./t/'+file):
        latestFile='./t/'+file
        maxFileSize=os.path.getsize('./t/'+file)
if not latestFile=='0':
    try:
        os.remove('replied.txt')
    except FileNotFoundError:
        pass
    shutil.move(latestFile,'replied.txt')
for file in os.listdir('./t/'):
    os.remove('./t/'+file)
if not os.path.exists('replied.txt'):
    o=open('replied.txt','w')
    o.close()
def Sleep(time,random=True):
    
    print('Waiting for',time,'s')
    for i in tqdm(range(time)):
        feed()
        try:
            if express:
                sleep(0.05)
            else:
                if random:
                    sleep(randint(2,18)/10)
                else:
                    sleep(1)
        except Exception as e:
            restart(e)
class post_:
    title=''
    content=''
class video:
    name:str=''
    BVID=''
def folderExists():
    if not os.path.exists('./Images'):
        os.makedirs('./Images')
    if not os.path.exists('./ImagesPost'):
        os.makedirs('./ImagesPost')
folderExists()
def pickImages(GetPost=False):
    if GetPost:
        return './ImagesPost/'+choice(os.listdir('./ImagesPost/'))
    else:
        return './Images/'+choice(os.listdir('./Images/'))
def getTrainingData():
    try:
        global wd
        title=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title > h1:nth-child(1)').text
        question=title+','+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
        with open('trainingData.txt','a',encoding='utf8') as f:
            
                a=wd.find_elements(By.CLASS_NAME,'reply-card__content')
                for i in a:
                    f.write('Q'+question+'\n')
                    f.write('A'+i.find_element(By.TAG_NAME,'p').text+'\n')
                b=wd.find_elements(By.CLASS_NAME,'reply-card__replies')
                for i in zip(a,b):
                    for j in i[1].find_elements(By.TAG_NAME,'p'):
                        f.write('Q'+i[0].find_element(By.TAG_NAME,'p').text+'\n')
                        f.write('A'+j.text+'\n') 
    except:
        pass
def selectPartition():
    global wd
    wd.find_element(By.CSS_SELECTOR,'div.mhy-radio:nth-child(3) > i:nth-child(1)').click()#生活
def selectCollection():
    global wd
    try:
        wd.find_element(By.CSS_SELECTOR,'.mhy-select__dummy').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR,'li.mhy-selectmenu__item:nth-child(2) > div:nth-child(1)').click()
    except Exception as e:
        print(e)

#os.system("taskkill -F -im explorer.exe")
#os.system("start taskmgr")



TESTINT=12
SLPTIME:int=120
SLPTIMEFORREPLY:int=20
fpr:int=randint(0,11)
MODEL:str=choice(MODELSATNIGHT)
auto:bool=False

try:
    MODEL=sys.argv[1]
    SLPTIME=int(sys.argv[2])
    fpr=int(sys.argv[3])
    auto=bool(int(sys.argv[4]))
except IndexError:
    pass
if BatteryStatus.getModelChoice():
    MODEL=choice(MODELSATDAY)
RAGALLOWED=False
REGALLOWED=RAGALLOWED
print(NYANAME,'model:',MODEL,' sleep:',SLPTIME,' begin in:',fpr ,' solveCAPTCHA:',auto)
print(VERSION)

        



feed()

try:
    fg=open('Topic.txt','r',encoding='utf8')
except FileNotFoundError:
    fg=open('Topic.txt','w',encoding='utf8')
    fg.close()
    fg=open('Topic.txt','r',encoding='utf8')
to=fg.read().split('\n')
topics=[e for e in to if e !='']


_start_new_thread(upd,tuple())



def restart(exception=None):
    global urlList
    try:
        u=open('urlList.txt','a')
        for i in urlList:
            u.write(i+'\n')
        u.close()
    except:
        pass
    if exception:
        print(exception)
    global wd
    try:
        wd.quit()
    except Exception as e:
        pass
    args=sys.argv[:]
    args.insert(0,sys.executable)
    os.execv(sys.executable,args)
    print('restart')


def interpret(text):
    a=1
    a2=1
    text=text.replace('\n',';')
    try:
        for i in REPLACEDICT:
            text=text.replace(i,REPLACEDICT[i])
    except Exception as e:
        print(e)
    return text
    while a!=-1 or a2!=-1:
        a=text.find('_(')
        a2=text[a:].find(')')
        if ' ' in text[a:a+a2+1]:
            a3=text.find(' ')
            text=text.replace(text[a-1:a+a3+1],'')
        return text
        text=text.replace(text[a:a+a2+1],'')
    return text
""" 
def getAnswer(question,interpreted=True,model=MODEL,allowRag=REGALLOWED)->str:
    #qwen2:0.5b,qwen2:1.5b,qwen2
    if model=='phi2':
        te=getAnswer('translate the following text into English:'+question,interpreted=False,model='qwen2:0.5b')
        re=getAnswer(te,interpreted=False,model='phi')
        text=getAnswer('翻译成中文:'+re,interpreted=True,model='qwen2:0.5b')
        return text
    if allowRag and len(question)<50 and len(question)>10:
        text=RAGUtil.getRag(question,model)
    else:
        res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":question}])
        text=res['message']['content']
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    if interpreted:
        text=text.replace("#","\n").replace("人工智能模型","猫娘").replace("**","").replace("AI语言模型","猫娘").replace("AI","猫娘")
        temp=''
        for k in text:
            temp+=k
            if k in '。！' and randint(0,10)<3:
                temp+=' 喵~ '
        
        text='喵~ '+temp+' 喵~'
        text=text.replace('喵~ '+' 喵~ ',' 喵~ ')

    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    return text 
"""
def getAnswerLite(question):
    return getAnswer(question)
def getAnswerforNovel(question,**kwargs):
    feed()
    res=ollama.chat(model=MODEL,stream=False,messages=[{"role":"user","content":question}])
    text=res['message']['content']
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    return text
def getAnswer0(question,interpreted=True,model=MODEL,allowRag=RAGALLOWED,Prompts=[],NewPrompts=False,useCHATTERBOT=True)->str:
    feed()
    if useCHATTERBOT:
        useCHATTERBOT=choice([True,True])
    #qwen2:0.5b,qwen2:1.5b,qwen2
    if NewPrompts:
        for i in question.split('\n'):
            if '#' in i:
                Prompts.append(i)
        for i in Prompts:   
            question=question.replace(i,'')
        PROMPT='\n#'.join(Prompts)+question
    else:
        PROMPT=question
    revelentDocuments=''
    textlist=[]
    if not useCHATTERBOT:
        for __ in range(REPEATREPLYTIMES):
            for _ in range(3):

                res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":PROMPT+revelentDocuments}])
                text=res['message']['content']
                if  '抱歉' not in text and '对不起' not in text:
                    break
                print(text,_)
                feed()
            textlist.append(text)
        res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":'#总结以下回复:'+'\n#'.join(textlist)}])
        
        text=res['message']['content']
    else:
        try:
            os.remove(ANSWERPATH)
        except:
            pass
        print(CHATTERBOTLAUNCH+PROMPT.replace('\n',' ').replace('#',',')+revelentDocuments)
        os.system(CHATTERBOTLAUNCH+PROMPT.replace('\n',' ')+revelentDocuments)
        while not os.path.exists(ANSWERPATH):
            Sleep(1)
        f=open(ANSWERPATH,'r',encoding='utf8')
        text=f.read()
        f.close()
        
        
    
    if interpreted or not containsRichTextWithoutInterpretation(text):
        text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
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
    text='喵~ '+text
    return text

def getAnswer(question,**kwargs)->str:
    try:
        os.remove(ANSWERPATH)
    except:
        pass
    PROMPT=kwargs.get('PROMPT','')
    print(CHATTERBOTLAUNCH+'"'+question+PROMPT.replace('\n',' ').replace('#',',')+'"')
    os.system(CHATTERBOTLAUNCH+'"'+question+PROMPT.replace('\n',' ').replace('#',',')+'"')
    wait=0
    while not os.path.exists(ANSWERPATH):
        Sleep(1)
        wait+=1
        if wait>8:
            restart()
    f=open(ANSWERPATH,'r',encoding='utf8')
    text=f.read()
    f.close()
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
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

    text=WordUtil.replaceAfter(text,NYANAME)
    return text 
print(getAnswer('你好你好你好你好你好你你好好你好你好你好你好你好你好你好你好你好',allowRag=True))
def getPost():
    rQ=post_()
    topic=choice(topics)
    print('发一条帖子的标题……只要标题,小于30字')

    rQ.title=getAnswerforNovel('发一条帖子的标题……只要标题,小于30字').replace('"','')
    
    rQ.content=getAnswerLite('以"'+rQ.title+'"为标题写一篇帖子的内容，只要内容!')
    try:
        newPost=WordUtil.ensureLength(WordUtil.segSentence(rQ.content))
        rQ.title=newPost[0]
        rQ.content=newPost[1]
    except:
        pass
    
    #print(rQ.title,'\n',rQ.content)
    return rQ
def getNovel():
    rQ=post_()
    
    rQ.title=getAnswerforNovel('写一篇现代网文的标题……只要标题,小于30字').replace('》','').replace('《','').replace('"','')

    text=getAnswerforNovel('以"'+rQ.title+'"为标题写一篇小说的内容，只要内容!')
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('《')
        a2=text[a:].find('》')
        text=text.replace(text[a:a+a2+1],'')
    rQ.content=text
    return rQ
def containsImage():
    global wd
    try:
        a=wd.find_element(By.CLASS_NAME,'mhy-img-article')
    except Exception as e:
        try:
           a=wd.find_element(By.CLASS_NAME,'ql-image-box')
        except Exception as e:
            return False
    imageLink=a.find_element(By.TAG_NAME,'img').get_attribute('src')

    r=requests.get(imageLink,stream=True)
    fileName='ImageInPost.jpg'
    a=open(fileName,'wb')
    a.write(r.content)
    a.close()
    if getSimiliarity(fileName,'Illegal.jpg') <1000:
        return False
    return fileName

def containsImageinReply():
    global wd
    try:
        imageLink=wd.find_element(By.CSS_SELECTOR,'.ql-image-box > img:nth-child(1)').get_attribute('src')
    except:
        return False
    r=requests.get(imageLink,stream=True)
    FileName='ImageinReply.jpg'
    if r.status_code == 200:
        a=open(FileName,'wb')
        a.write(r.content)
        a.close()
        return FileName

try:
    getAnswer('你好')
    getAnswerforNovel('你好')
except Exception as e:
    Sleep(2)
    restart(e)
print("模型启动成功")
print("浏览器启动")
try:
    wd=webdriver.Firefox()
except Exception as e:
    restart(e)
wd.implicitly_wait(35)
#wd.execute_script("document.body.style.zoom='0.5'")
login=True
if fpr==TESTINT:
    login=False

def ScrollToBottom(tries=SCROLLTRIES)->None:
    global wd
    for _ in range(tries):
        wd.execute_script(SCROLLBOTTOM)
        sleep(2)
    scrollToTop(tries=tries)
def scrollToBottom(tries=SCROLLTRIES)->None:
    ScrollToBottom(tries=SCROLLTRIES)
def scrollToTop(tries=SCROLLTRIES)->None:
    global wd
    for _ in range(SCROLLTRIES):
        wd.execute_script(SCROLLTOP)
        sleep(2)
def ScrollToTop(tries=SCROLLTRIES)->None:
    scrollToTop(tries=SCROLLTRIES)
def sendAnswerD(answer,inputBox):
    
    temp=''
    for text in answer:
        if text=='\n':
            inputBox.send_keys(temp)
            inputBox.send_keys(Keys.ENTER)
            feed()
            #print(temp)
            temp=''
            sleep(0.01)
        else:
            temp+=text
    inputBox.send_keys(temp)
    #print(temp)



def sendAnswer(answer,inputBox,refuseEmotions=False,MAXIMUMCOUNT=500):
    emotionCount=10*int(refuseEmotions)
    temp=''
    wordCount=0
    for text in answer:
        
        if text=='\n':
            wordCount+=2
            inputBox.send_keys(temp)
            inputBox.send_keys(Keys.ENTER)
    
            feed()
            #print(temp)
            temp=''
            sleep(0.01)
        else:
            temp+=text
            wordCount+=1
            if text in '，。' and randint(0,10)<5 and emotionCount<10:
                emotion=choice(EMOTIONS)
                temp+=emotion
                wordCount+=len(emotion)
                emotionCount+=1
        if wordCount>MAXIMUMCOUNT:
            break
    inputBox.send_keys(temp)
    #print(temp)
    Sleep(4)
urlList=[]
if not os.path.exists('urlList.txt'):
    o=open('urlList.txt','w')
    o.close()

def checkUrl()->bool:
    return False
    try:
        global wd,urlList
        url=wd.current_url
        s=url.find('article/')
        articleIndex=url[s+8:]
        if articleIndex in urlList:
            return True
        urlList.append(articleIndex)
        return False
    except:
        return False
def getCommand(text): #没什么用了
    if text=='Inquiry->':
        pass
    else:
        return False
if login:
    try:
        wd.get('https://www.miyoushe.com/ys/')
        Sleep(12)
        try:
            wd.find_element(By.CSS_SELECTOR,".header__avatar > img:nth-child(1)").click()
        except Exception as e:
            wd.find_element(By.CSS_SELECTOR,".header__avatarwrp").click()
        Sleep(12)
        r=wd.find_element(By.ID,"mihoyo-login-platform-iframe")
        Sleep(12)
        wd.switch_to.frame(r)
        wd.find_element(By.CSS_SELECTOR ,'#tab-password').click()
        wd.find_element(By.CSS_SELECTOR ,'#username').send_keys(ACCOUNT)
        wd.find_element(By.CSS_SELECTOR ,'#password').send_keys(PASSWORD)
        wd.find_element(By.CSS_SELECTOR ,'.el-checkbox__inner').click()
        wd.find_element(By.CSS_SELECTOR ,'button.el-button').click()
        if CHECKFOLLOWED:
            print('关注')
            Sleep(12)
            wd.get('https://www.miyoushe.com/ys/accountCenter/fanList?id=425414668')
            sleep(12)
            scrollToBottom(20)
            for i in wd.find_elements(By.CLASS_NAME,'mhy-follow-button'):
                if '回关' in str(i.get_attribute('innerHTML')):
                    i.click()
                    sleep(2)
            sleep(12)
            wd.get('https://www.miyoushe.com/ys/accountCenter/followList?id=425414668')

            for i in wd.find_elements(By.CLASS_NAME,'mhy-follow-button'):
                if '已关注' in str(i.get_attribute('innerHTML')):
                    i.click()
                    sleep(2)
                    wd.find_element(By.CSS_SELECTOR,'div.mhy-button:nth-child(2) > button:nth-child(1)').click()
                    sleep(2)
    except Exception as e:
        restart(e)
feed()
#o=open('replied.txt','a')
o=open('replied.txt','r')
replied=[]
tmprepl=o.read().split('\n')
for n in tmprepl:
    replied.append(n.replace('[ENTER]','\n'))
def writereplied():
    global replied
    tmp=[]
    for i in replied:
        tmp.append(i.replace('\n','[ENTER]'))
    p=open('replied.txt','w')
    tx='\n'.join(tmp)
    for k in tx:
        try:
            p.write(k)
        except UnicodeEncodeError:
            pass
    p.close()
def getNotebook():
    with open('replied.txt','r') as r:
        t=r.read().replace('[ENTER]','\n')
    p=open('Notebook.txt','w',encoding='utf8')
    p.write(t)
    p.close()

getNotebook()
while True:
    while Util.getRepliedCount()>=MAXREPLYCOUNT and fpr in [0,3,4,5,7,10,11]:
        fpr+=1
        if fpr>11:
            fpr=0
    print(fpr,end=' ')
    ValU=['回复','发帖','发小说帖','关注','生活','@','发图片帖','ACG','视频','创作图片','酒馆','酒馆关注','私信','测试']
    try:
        print(ValU[fpr],'-'*40)
    except Exception as e:
        pass
    if fpr==11:
        wd.quit()
        try:
            MAXREPLYCOUNT=1000
            import AutoGui
        except:
            pass
        restart('Normal Exit')
    if fpr==0:
        


        tries=0
        wd.get('https://www.miyoushe.com/ys/notifications/reply')
        Sleep(1)

        ScrollToBottom()

        #回复
        ready=wd.find_elements(By.CLASS_NAME,'notifications-common-card__content')
        
        for t1 in ready:
            tries+=1
            if tries==REPLYLIMIT:
                continue
            try:
                t1.click()
            except Exception as e:
                restart(e)
            repllist=[]
            Sleep(8)
            originalPost=''
            try:
                repld=wd.find_elements(By.CLASS_NAME,'reply-card__container')
            except Exception as e:
                restart(e)
            image=containsImageinReply()
            imageDescription=''
            try:
            #查看原帖
                wd.find_element(By.CSS_SELECTOR,'.reply-detail-container__main > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()
                wd.switch_to.window(wd.window_handles[-1])
                Sleep(2)
                originalPost+=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title').text
                if not image:
                    image=containsImage()
                    imageDescription=''
                try:
                    originalPost+='\n'+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
                except Exception as e:
                    pass
            
                wd.close()
                wd.switch_to.window(wd.window_handles[-1])
            except Exception as e:
                restart(e)
            #所有回复
            
            #a=ts.find_elements(By.CLASS_NAME,'mhy-account-title__name')
            #b=ts.find_elements(By.CLASS_NAME,'reply-card__content')
            #c=ts.find_elements(By.CLASS_NAME,'reply-card-operation-bottom__item')
            try:
                ts=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__body')
                for i in repld:
                    print(repld.index(i),'|',len(repld))
                    name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text
                    
                    if name.replace(' ','')==NYANAME:
                        continue
                    content=i.find_element(By.CLASS_NAME,'reply-card__content').text.replace('@'+NYANAME,'')
                    if content.replace(' ','')=='':
                        continue
                    i.find_element(By.CLASS_NAME,'mhy-heart-click__icon').click()
                    content=interpret(content)
                    print(name+':'+content,name+content in replied)
                    if name+content not in replied:
                        replied.append(name+content)
                        writereplied()
                        if image and imageDescription=='':
                            imageDescription=VisionUtil.getImageDescription([image])
                            try:
                                answer=getAnswer(content+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription,NewPrompts=True)
                            except Exception as e:
                                answer='喵。'
                        elif image and imageDescription!='':
                            try:
                                answer=getAnswer(content+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription,NewPrompts=True)
                            except Exception as e:
                                answer='喵。'
                        else:
                            try:
                                answer=getAnswer(content+'\n#原帖:'+originalPost,NewPrompts=True)
                            except Exception as e:
                                answer='喵。'
                        answer=answer[:500]
                        i.find_element(By.CLASS_NAME,'reply-card-operation-bottom__item').click()
                        #wd.find_element(By.CLASS_NAME,'ql-blank').send_keys(answer)
                        Sleep(1)
                        inputBox=wd.find_element(By.CLASS_NAME,'ql-blank')
                        sendAnswer(answer,inputBox)
                        Sleep(1)
                        wd.find_element(By.CLASS_NAME,'mhy-reply-box__submit').click()
                        
                        writeCount()
                        
                        Sleep(3)
                        #getimg()
                        Sleep(SLPTIMEFORREPLY)
            except Exception as e:
                restart(e)
                break
            try:
                wd.find_element(By.CLASS_NAME,'icon-close1').click()
                sleep(2)
            except Exception as e:
                pass
    elif fpr==1:#发帖
        try:
            pos=getPost()
            replied.append(pos.title)
            writereplied()
            wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
            wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(pos.title)
            inputBox=wd.find_element(By.CSS_SELECTOR,'.ql-editor')
            sendAnswer(pos.content,inputBox,MAXIMUMCOUNT=30000)
            selectPartition()
            sleep(1)
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
            Sleep(SLPTIME*2)
        except Exception as e:
            restart(e)
    elif fpr==2:#发小说帖
        try:
            posG=getNovel()
            replied.append(posG.title)
            writereplied()
            wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
            wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(posG.title)
            inputBox=wd.find_element(By.CSS_SELECTOR,'.ql-editor')
            sendAnswer(posG.content,inputBox,True,MAXIMUMCOUNT=30000)
            sleep(4)
            selectCollection()
            sleep(4)
            selectPartition()
            
            #预投稿
            #wd.find_element(By.CSS_SELECTOR,'div.original-form-item__original:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)').click()
            
            sleep(1)
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
            Sleep(SLPTIME*2) 
        except Exception as e:
            restart(e)       
    elif fpr==5: #@
        try:
            wd.get('https://www.miyoushe.com/dby/notifications/mention')
            ats=wd.find_elements(By.CLASS_NAME,'notifications-common-card')
        except Exception as e:
            restart(e)
        for ri in ats:
            try:
                print(ats.index(ri),'|',len(ats))
                originalPost=''
                try:
                    ri.click()
                except Exception as e:
                    restart(e)
                try:
                    repld=wd.find_elements(By.CLASS_NAME,'reply-card__container')
                    Ser=False
                except Exception as e:
                    restart(e)
                #查看原帖
                try:
                    wd.find_element(By.CSS_SELECTOR,'.reply-detail-container__main > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()
                except Exception as e:
                    Ser=True
                
                    
                    pass
                try:
                    wd.switch_to.window(wd.window_handles[-1])
                    originalPost+=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title').text
                except Exception as e:
                    restart(e)
                try:
                    originalPost+='\n'+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
                except Exception as e:
                    pass
                if not Ser:
                    wd.close()
                    wd.switch_to.window(wd.window_handles[-1])
                else:
                            try:
                                wd.find_element(By.CSS_SELECTOR,'div.mhy-article-actions__item:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
                            except Exception as e:
                                pass
                            #
                            title=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title > h1:nth-child(1)').text
                            try:
                                
                                content=wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
                            except Exception as e:
                                content=''
                            content=interpret(content)
                            try:
                                image=containsImage()
                                print(image)
                                if image:
                                    description=VisionUtil.getImageDescription([image])
                                    answer=getAnswer(title+','+content,Prompts=[',图片描述:'+description.replace('\n',',')])
                                else:
                                    answer=getAnswer(title+','+content)
                                inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")

                                try:
                                    
                                    
                                    if containsRichTextWithoutInterpretation(answer):
                                        richtext=containsRichText(answer)
                                        sendAnswer(richtext[1],inputBox,MAXIMUMCOUNT=1000)
                                        wd.find_element(By.CSS_SELECTOR,'.icon-tupian1').click()
                                        CopyTest.uploadSth(os.path.abspath(richtext[0]))
                                    else:
                                        sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
                                except Exception as e:
                                    sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
                                    pass
                                    

                                #answer=getAnswer(title+','+content)
                                
                                sendAnswer(answer,inputBox)
                            except Exception as e:
                                pass
                            if randint(0,4)==0:
                                try:
                                    CopyTest.copyImage(pickImages())
                                    wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor").send_keys(Keys.CONTROL,'v')
                                    Sleep(8)
                                except Exception as e:
                                    pass
                            wd.find_element(By.CLASS_NAME,'mhy-button-normal').click()
                            writeCount()
                          
                            sleep(3)
                           
                            writereplied()
                            Sleep(SLPTIME)
                            try:
                                wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()
                                restart(e)
                            except Exception as e:
                                print('?')
                            wd.close()
                            wd.switch_to.window(wd.window_handles[-1])
                            #每次一遍，坚定信念
                            #getAnswer('在接下来的回答中……你一定要保持可爱……知道了吗')
                            continue
                #所有回复
                try:
                    ts=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__body')
                except Exception as e:
                    restart(e)
                #a=ts.find_elements(By.CLASS_NAME,'mhy-account-title__name')
                #b=ts.find_elements(By.CLASS_NAME,'reply-card__content')
                #c=ts.find_elements(By.CLASS_NAME,'reply-card-operation-bottom__item')
                try:
                    
                    for i in repld:
                        print(repld.index(i),'|',len(repld))
                        try:
                            name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text
                        except Exception as e:
                            print('''name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text Fail''')
                            continue
                        if name.replace(' ','')=='Nya2PtCl4':
                            continue
                        try:
                            content=i.find_element(By.CLASS_NAME,'reply-card__content').text.replace('﻿@Nya2PtCl4','')
                        except Exception as e:
                            content=''
                        if content.replace(' ','')=='':
                            continue
                        i.find_element(By.CLASS_NAME,'mhy-heart-click__icon').click()
                        
                        print(name+':'+content,name+content in replied)
                        if name+content not in replied:
                            replied.append(name+content)
                            writereplied()
                            try:
                                answer=getAnswer(content+'\n#原帖:'+originalPost,NewPrompts=True)
                                if len(answer)>500:
                                    answer=getAnswer(content+'……字数小于500字')[:500]
                            except Exception as e:
                                answer='喵。'
                            i.find_element(By.CLASS_NAME,'reply-card-operation-bottom__item').click()
                            writeCount()
                            #wd.find_element(By.CLASS_NAME,'ql-blank').send_keys(answer)
                            sleep(1)
                            inputBox=wd.find_element(By.CLASS_NAME,'ql-blank')
                            sendAnswer(answer,inputBox)
                            sleep(1)
                            selectPartition()
                            sleep(1)
                            wd.find_element(By.CLASS_NAME,'mhy-reply-box__submit').click()
                
                           
                            Sleep(3)
                          
                            Sleep(SLPTIMEFORREPLY)
                            try:
                                wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()
                                restart(e)
                            except Exception as e:
                                print('?')
                            sleep(2)
                            try:
                                wd.find_element(By.CSS_SELECTOR,'.icon-close1').click()
                            except Exception as e:
                                restart(e)
                except Exception as e:
                    restart(e)
            except Exception as e:
                continue
    elif fpr==6:#发图片帖
        #replied.append('分享图片')
        try:
            writereplied()
            wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
        
            wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys('分享图片')
            failTries=0
            selectPartition()
        except Exception as e:
            restart(e)
        for i in range(4):
            try:
                if randint(0,4)<1:
                    CopyTest.getNetImage()
                    wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
                    CopyTest.uploadSth(os.path.abspath('temp.jpg'))
                else:
                    wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
                    CopyTest.uploadSth(os.path.abspath(pickImages(True)))
                    

            except Exception as e:
                print('Fail')
                failTries+=1
        if failTries<4:
                
            Sleep(20)
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()

            Sleep(SLPTIME*2)
        else:
            Sleep(12)
    elif fpr==9:#画画
        try:
            image=DrawUtils.drawPicture()
            Sleep(12)
        except Exception as e:
            fpr+=1
            continue
        try:
            image.save('temp.png')
            replied.append('分享作品')
            writereplied()
            wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
            wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys('分享作品')
            failTries=0
            selectPartition()
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
            wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
            CopyTest.uploadSth(os.path.abspath('temp.png'))
            Sleep(30)
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
            Sleep(SLPTIME*2)
        except Exception as e:
            restart(e)
    elif fpr==8:#分享视频
        wd.get(VIDEOURL)
        try:
            wd.find_element(By.CSS_SELECTOR,'.bili-mini-close-icon')
            Sleep(2)
            wd.get(VIDEOURL)
        except Exception as e:
            pass
        try:
            Sleep(12)
            vtaglist=wd.find_elements(By.CLASS_NAME,'small-item')
            Videos=[]
        except Exception as e:
            restart(e)
        for i in vtaglist:
            f=video()
            f.BVID=i.get_attribute('data-aid')
            f.name=i.find_element(By.TAG_NAME,'img').get_attribute('alt')
            Videos.append(f)
        flag=False
        tries_=0
        for i in Videos:
            if i.name not in replied:
                flag=True
                replied.append(i.name)
                writereplied()
                wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
                wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(i.name)
                wd.find_element(By.CSS_SELECTOR,'.icon-shipin1').click()
                sleep(1)
                wd.find_element(By.CSS_SELECTOR,'li.mhy-tab__item:nth-child(2) > span:nth-child(1)').click()
                sleep(1)
                wd.find_element(By.CSS_SELECTOR,'div.mhy-input:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(i.BVID)
                sleep(1)
                wd.find_element(By.CSS_SELECTOR,'.mhy-video-uploader__confirm > button:nth-child(1)').click()
                sleep(1)
                selectPartition()
            if flag:
                wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
                Sleep(SLPTIME)
                
            else:
                Sleep(12)
            tries_+=1
            if tries_>3:
                break
            


    else:
        tries=0
        nets=['','','','https://www.miyoushe.com/dby/timeline','https://www.miyoushe.com/dby/home/34?type=2','','','https://www.miyoushe.com/dby/home/35','https://www.miyoushe.com/ys/timeline','','https://www.miyoushe.com/ys/home/26']
        try:
            
            wd.get(nets[fpr])
            Sleep(12)
            scrollToBottom()
            e=wd.find_elements(By.CLASS_NAME,"mhy-article-card")
            e2=wd.find_elements(By.CLASS_NAME,"mhy-router-link mhy-article-card__link")
            for post in e:
                print(e.index(post),'|',len(e))
                tries+=1
                if tries>=POSTLIMIT:
                    break
                try:
                    title=post.find_element(By.CLASS_NAME,"mhy-article-card__h3").text
                    
                    til=post.find_element(By.CLASS_NAME,"mhy-article-card__h3")
                    #try:
                        
                        #content=post.find_element(By.CLASS_NAME,"mhy-article-card__content").text
                    #except Exception as e:
                        #没有内容
                        #content=''

                    print(title,title in replied)
                    if title not in replied:
                        replied.append(title)
                        if title=='Command->TakeaScreenshotas热吻热狗热狗问题饿微软废弃物人':
                            
                            inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")
                            CopyTest.copyScreenshot()
                            wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor").send_keys(Keys.CONTROL,'v')
                            Sleep(8)
                            wd.find_element(By.CLASS_NAME,'mhy-button-normal').click()
                            writeCount()
                            Sleep(SLPTIME)
                            continue
                        til.click()
                        wd.switch_to.window(wd.window_handles[-1])
                        sleep(1)
                        getTrainingData()
                        try:
                            content=wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
                        except Exception as e:
                            content=''
                        content=interpret(content)
                        
                         
                        
                        #点赞
                        try:
                            wd.find_element(By.CSS_SELECTOR,'div.mhy-article-actions__item:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
                        except Exception as e:
                            pass
                        #
                        try:
                            image=containsImage()
                            print(image)
                            if image:
                                description=VisionUtil.getImageDescription([image])
                                answer=getAnswer(title+','+content,Prompts=[',图片描述:'+description.replace('\n',',')])
                            else:
                                answer=getAnswer(title+','+content)
                            answer=answer[:1000]
                            
                            inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")
                            try:
                                
                                
                                if containsRichTextWithoutInterpretation(answer):
                                    richtext=containsRichText(answer)
                                    sendAnswer(richtext[1],inputBox,MAXIMUMCOUNT=1000)
                                    wd.find_element(By.CSS_SELECTOR,'.icon-tupian1').click()
                                    CopyTest.uploadSth(os.path.abspath(image))
                            except Exception as e:
                                pass
                            
                            sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
                        except Exception as e:
                            pass
                        replied.append(content)
                        if randint(0,4)==0:
                            CopyTest.copyImage(pickImages())
                            wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor").send_keys(Keys.CONTROL,'v')
                            Sleep(8)
                        wd.find_element(By.CLASS_NAME,'mhy-button-normal').click()
                        writeCount()
                     
                        sleep(3)
                      
                        writereplied()
                        Sleep(SLPTIMEFORREPLY)
                        try:
                            wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()
                            restart()
                        except:
                            print('?')
                        try:
                            wd.close()
                            wd.switch_to.window(wd.window_handles[-1])
                        except:
                            restart('Switch Failed')
                        
                                               
                except:
                    
                    restart()
                    continue

        except Exception as e:
            
            restart(e)
    fpr+=1
    if fpr>11:
        fpr=0
#wd.find_element(By.CLASS_NAME,'notifications-common-card__content--text').click()
#a=wd.find_elements(By.CLASS_NAME,'notifications-common-card')
#rep=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__header')
#rell=rep.find_elements(By.CLASS_NAME,'reply-card')
