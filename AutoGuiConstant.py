'''
This file contains the constants used in the AutoGui project.
'''
import pyautogui
import pyperclip
import cv2
import easyocr
from time import sleep
import numpy as np
import enum
from PIL import Image
MODEL='qwen2:0.5b'

HWNDTITLE="雷电模拟器-1"
class opt(enum.Enum):
    HOME='F1'
    BACK='esc'

REPLIEDMARK='REPLIED'
def Doreplied(result):
    C=result[-1]
    if REPLIEDMARK in C[1]:
        return True
    return False
reader = easyocr.Reader(['en','ch_sim'])

USELESSDict='''米游社
囤 
按键
关注
已关注
互相关注
加垦 
[温磬提示]
9-
9+
龌
凝
缉
&
茧罔
囱
多开
酮
安芰
设置
回
加垦
更多
右上角
NazlrCl6x6H20
9分钟前
[草稿] y[回复标记]<-REPLIED->[回复标记]<-REPLIE。。
茧图
甸
怎么取都不满意
5小小时前
谢谢你的赞[爱心][爱心][爱心]
星夕晴Peter
14小小时前
墨云谙
23小时前
都不搭理
酱酱伤心了
荧5229
11-10
佑谙
11-09
你好
Fdoiunn
11-08
猫猫!
音贡
动态
消息
我的

'''.split('\n')

class window:
    x, y, width, height=0,0,0,0
def getWindow(windowName):
    x,y,width,height=windowName.x,windowName.y,windowName.width,windowName.height
    return x,y,width,height

def ss(x, y, width, height):
    # 使用pyautogui进行截图
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    # 将PIL图像转换为OpenCV格式
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # 保存截图为文件
    cv2.imwrite(SSPTH, screenshot)


def copyText(text):
    pyperclip.copy(text)
def paste():
    pyautogui.hotkey('ctrl', 'v')

def clickScreen(X,Y=-1):
    if Y==-1:
        Y=X[1]
        X=X[0]
    pyautogui.click(X,Y)

def getCenter(bbox):
    # 提取坐标
    x, y = bbox[0]  # 左上角
    w = bbox[1][0] - bbox[0][0]  # 宽度
    h = bbox[3][1] - bbox[0][1]  # 高度
    return (x + w / 2, y + h / 2)



def draw_bboxes_on_image(image_path, bboxes):
    # 读取图片
    image = cv2.imread(image_path)
    
    # 绘制每个 bbox
    for bbox in bboxes:
        # 提取每个 bbox 的四个角坐标
        try:
            top_left = tuple(bbox[0])  # 左上角
            bottom_right = tuple(bbox[2])  # 右下角
        
        # 绘制矩形，线条颜色为红色，线宽为2
            cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
        except:
            pass
    cv2.imwrite('screenshotRES.png', image)

def likedate(text):
    if '刚' in text:
        return True
    elif '分' in text:
        return True
    elif '小时' in text:
        return True
    elif '-' in text:
        for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in text:
                return False
        return True
    return False
def replaceUselessWords(result):
    newResult=[]
    for C in result:
            if C[1] not in USELESSDict:
                newResult.append(C)
    return newResult
def getText(result):
    text='#'
    for C in  result:
        text+=C[1]+'\n#'
    return text            

SSPTH='screenshot.png'

from random import choice
import ollama
from Constant import MODALWORDS
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