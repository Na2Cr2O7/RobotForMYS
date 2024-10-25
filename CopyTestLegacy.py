import win32clipboard
from PIL import Image,ImageGrab
from io import BytesIO
import requests


def copyImage(img_path: str,i=False,net=True):
    '''输入文件名，执行后，将图片复制到剪切板'''
    if i:
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
if __name__=='__main__':
    copyScreenshot()
