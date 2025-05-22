import win32clipboard
from PIL import Image,ImageGrab
from io import BytesIO
import requests
from random import randint
import win32gui
import win32con
from time import sleep

def uploadSth(path):
    sleep(4)
    try:
        dg=win32gui.FindWindow(None,'File Upload')
    except:
        dg=win32gui.FindWindow(None,'文件上传')
    comboboxEx32=win32gui.FindWindowEx(dg,0,'ComboBoxEx32',None)
    combobox=win32gui.FindWindowEx(comboboxEx32,0,'ComboBox',None)
    edit=win32gui.FindWindowEx(combobox,0,'Edit',None)
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,path)
    button=win32gui.FindWindowEx(dg,0,'Button',None)
    win32gui.SendMessage(dg,win32con.WM_COMMAND,1,button)

def copyImage(img_path: str="",i=False,net=True):
    '''输入文件名，执行后，将图片复制到剪切板'''
    if net:
        getNetImage()
        image = Image.open('temp.jpg')
    elif i:
        image=img_path
    else:
        image = Image.open(img_path)
        
    output = BytesIO()
    image.save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
def copyScreenshot():
    '''复制屏幕截图到剪贴板'''
    T=ImageGrab.grab()
    #T.save('ss.jpg')
    copyImage(T,True)
def getNetImage(filename='temp.jpg'):
    r=requests.get('https://picsum.photos/1000/1000').content
    o=open(filename,'wb')
    o.write(r)
    o.close()
if __name__=='__main__':
    copyImage(None)
