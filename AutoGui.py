import pyautogui
import cv2
import numpy as np
import easyocr
import win32gui
import win32con
from PIL import Image
import pyautogui
import cv2
import numpy as np
import easyocr
import win32gui
import win32con
import os
from time import sleep

reader = easyocr.Reader(['en','ch_sim'])

from  AutoGuiConstant import *

def getUnexactElementByText(text):
    
    result=reader.readtext(SSPTH)
    for i in text:
        for C in result:
            if i in C[1].replace(' ',''):
                return C[0]
    return False
def getUnexactElementsByText(text):
    result=reader.readtext(SSPTH)
    elements=[]
    for i in text:
        for C in result:
            if i in C[1].replace(' ',''):
                elements.append(C[0])
    return elements
def getElementByText(text):
    
    result=reader.readtext(SSPTH)
    for C in result:
        if text == C[1].replace(' ',''):
            return C[0]
    return False 
def getElementsByText(text):
    result=reader.readtext(SSPTH)
    elements=[]
    for C in result:
        if text == C[1].replace(' ',''):
            elements.append(C[0])
    return elements 
def clickText(text,clipImage=False):
    ss(x, y, width, height)
    if clipImage:
        clipImage()
    bbox=getElementByText(text)
    if not bbox:
        bbox=getUnexactElementByText(text)
    if bbox:
        pos=getCenter(bbox)
        click(pos[0],pos[1])
        sleep(5)
        return True
    return False

def clipImage():
        im=Image.open(SSPTH)
        im=im.crop(0,60,x+width,y+height)
        im.save(SSPTH)



debug=False
hwnd=False


# 打开雷电模拟器
while not hwnd:
    os.startfile("Emulator.lnk")
    sleep(5)
    hwnd = win32gui.FindWindow(None, HWNDTITLE)
    
hwnd = win32gui.FindWindow(None, HWNDTITLE)
print(hwnd)
x,y,width,height=0,0,0,0

def re():
    global x, y, width, height
    while True:
        if not hwnd:
            return -1   
        sleep(10)
        try:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        except:
            return -1
        x, y, w, h = win32gui.GetWindowRect(hwnd)
        width = w - x
        height = h - y
        try:
            ss(x, y, width, height)
        except:
            pass
from threading import Thread
if hwnd:
    Ta=Thread(target=re)
    Ta.start()
def click(X, Y=-1):
    if Y==-1:
        Y=X[1]
        X=X[0]
    global x, y, width, height
    pyautogui.click(X+x, Y+y)
def clickPercent(Xpercent  , Ypercent=-1):
    if Ypercent==-1:
        Ypercent=Xpercent[1]
        Xpercent=Xpercent[0]
    global x, y, width, height
    pyautogui.click(Xpercent*width+x, Ypercent*height+y)
while True:
    try:
        ss(x,y,width,height)
        break
    except:
        sleep(10)
while not getElementByText('米游社'):
    sleep(5)
    ss(x,y,width,height)
    clickPercent(.5,.5)#主页键
    pyautogui.press(opt.HOME.value)


sleep(8)


    
while not clickText('米游社'):
    sleep(5)
sleep(10)
while not clickText('消息'):
    sleep(5)    
sleep(10)
while not clickText('聊天'):
    sleep(5)    
sleep(10)
ss(x, y, width, height)
bboxes=[]
result=reader.readtext(SSPTH)
for C in result:
    if likedate(C[1]):
        bboxes.append(C[0])
import pyperclip
for i in range(185,846,110):
    
    sleep(2)
    clickPercent((.5,i/1000))

    sleep(10)
    ss(x, y, width, height)
    result=''
    result=reader.readtext(SSPTH)
    clipImage()
    print(result)
    if Doreplied(result):
        pyautogui.press(opt.BACK.value)
        continue
    useful=replaceUselessWords(result)
    text=getText(useful)
    print(text,end='->')
    
    answer=getAnswerforAutoGui(text)
    print(answer)
    #answer+='\n[回复标记]<--'+REPLIEDMARK+'-->'
    #输入框
    sleep(2)
    clickPercent((.5,.945))
    sleep(1)
    
    sleep(1)
    for i in answer.split('\n'):
        print(i)
        clickScreen(1,1)
        pyperclip.copy(i)
        
        click(1,1)
        sleep(10)
        pyautogui.hotkey('ctrl', 'v')
        
        pyautogui.press('enter')  # 发送回车键
        sleep(.1)
    '''.84,.83.89'''
    for i in range(83,89,2):
        clickPercent((.84,i/100))
        sleep(.5)
    sleep(10)
    clickPercent(.5,.5)
    sleep(2)
    pyautogui.press(opt.BACK.value)
    sleep(10)
    ss(x, y, width, height)
    sleep(10)

win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
Ta.join()
