"""
    UpdateLogInfo.py
    need UpdateInfo.txt (UTF-8)

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Constant import *
from time import sleep as Sleep
import os
SLPTIME=150
MAXIMUMCOUNT=30000
class post:
    title=''
    content=''
def sendAnswer(answer,inputBox):
    temp=''
    wordCount=0
    for text in answer:
        
        if text=='\n':
            wordCount+=2
            inputBox.send_keys(temp)
            inputBox.send_keys(Keys.ENTER)
    
            #print(temp)
            temp=''
            Sleep(0.01)
        else:
            temp+=text
            wordCount+=1
        if wordCount>MAXIMUMCOUNT:
            break
    inputBox.send_keys(temp)
    #print(temp)
    Sleep(4)
if not os.path.exists("UpdateInfo.txt"):
    exit()
with open("UpdateInfo.txt","r",encoding="utf-8") as f:
    TITLE=f.readline().strip()
    CONTENT=f.read().strip()
pos=post()
pos.title=TITLE
pos.content=CONTENT[1:]
wd=webdriver.Firefox()
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
try:
            
            wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
            wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(pos.title)
            inputBox=wd.find_element(By.CSS_SELECTOR,'.ql-editor')
            sendAnswer(pos.content,inputBox,MAXIMUMCOUNT=30000)
            Sleep(1)
            wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
            Sleep(SLPTIME*2)
            wd.quit()
except Exception as e:
            os.remove("UpdateInfo.txt")
            wd.quit()
