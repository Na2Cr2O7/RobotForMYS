import win32clipboard
from PIL import Image,ImageGrab
from io import BytesIO
import requests
from random import randint

def copyImage(img_path: str,i=False,net=True):
    '''输入文件名，执行后，将图片复制到剪切板'''
    if net and randint(0,10)<1000:
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
def getNetImage():
    r=requests.get('https://picsum.photos/1000/1000').content
    o=open('temp.jpg','wb')
    o.write(r)
    o.close()
if __name__=='__main__':
    copyImage(None)
