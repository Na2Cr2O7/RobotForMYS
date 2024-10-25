'''
visionutil.py
图像视觉工具
'''
import Constant
import ollama
import os
from time import time
from PIL import Image
import LocalTranslate
MAXIMUMIMAGEPIXELS=640*480
def resizeImage(imagePath:str,maxPixels=MAXIMUMIMAGEPIXELS):
    img = Image.open(imagePath)
    sizeX,sizeY=img.size
    if sizeX*sizeY>maxPixels:
        sizeX*=0.9
        sizeY*=0.9
    img=img.resize((int(sizeX),int(sizeY)))
    img.save(imagePath)
    return imagePath
def getAnswerImage(imagePaths:list,limitation=1,translate=True):
    start=time()
    res = ollama.chat(
        model=Constant.VISIONMODEL,
        messages=[
            {
                'role': 'user',
                'content': 'Describe the image in Chinese:',
                'images': [os.path.abspath(resizeImage(i)) for i in imagePaths][:limitation]
            }
        ]
    )

    print(res['message']['content'])
    result=res['message']['content']
    if translate:
        try:
            result=LocalTranslate.translate(result)
        except:
            pass
    end=time()
    print('Time used:',end-start) 
    return result
def getImageDescription(imagePath:list):
    return getAnswerImage(imagePath)
