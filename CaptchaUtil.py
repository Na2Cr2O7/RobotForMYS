import ollama
import os
from time import time
import cv2
import hashlib
import shutil
def checkHash2(byte):
    h=hashlib.new('sha256')
    h.update(byte)
    L=h.hexdigest()
    return L

def getSimiliarity(path1,path2) ->int :
    
    image1 = cv2.imread(path1)
    image2 = cv2.imread(path2)

    hst1=cv2.calcHist([image1],[0],None,[255],[0,256])
    hst2=cv2.calcHist([image2],[0],None,[255],[0,256])
    return cv2.compareHist(hst1,hst2,cv2.HISTCMP_KL_DIV)
def determine(image_path,name):
    
    res = ollama.chat(
        model="llava-phi3",
        messages=[
            {
                'role': 'user',
                'content': 'Is the image contains (a/an) '+name+'?',
                'images': [image_path]
            }
        ]
    )
    answer=res['message']['content']
    if 'yes' in answer.lower():
        return True
    else:
        return False


def getImage(imageName='temp.jpg'):
    V=cv2.imread(imageName)
    crop=V[344:384,0:40]
    cv2.imwrite('Goal.jpg',crop)
    count=0
    for p in range(0,344,116):
        for q in range(0,344,116):
            crop=V[p:112+p,q:112+q]
            cv2.imwrite('temp_'+str(count)+'.jpg',crop)
            count+=1
    minimum=['T',100000000]
    for i in os.listdir('.\\Info'):
        value=getSimiliarity('Goal.jpg','.\\Info\\'+i)
        if value<minimum[1]:
            minimum=[i,value]
    print(minimum)
    fold='.\\data\\'+os.path.splitext(minimum[0])[0]
    Correct=[]
    Incorrect=[]
    for i in range(0,9):
        try:
            os.listdir(fold)
        except:
            break
        for each in os.listdir(fold):
            if getSimiliarity('temp_'+str(i)+'.jpg',fold+'\\'+each)<1000:
                Correct.append(i)
                #print(i)
    for i in range(0,9):
        if i not in Correct:
            for folder in os.listdir('.\\data\\'):
                for each in os.listdir('.\\data\\'+folder):
                    
                    if '.\\data\\'+folder==fold:
                        continue
                    if getSimiliarity('temp_'+str(i)+'.jpg','.\\data\\'+folder+'\\'+each)<200:
                        #print(i,folder,each)
                        Incorrect.append(i)
                        break
    #print(Incorrect)
    for i in Incorrect:
        if i in Correct:
            Correct.remove(i)
    for i in range(0,9):
        if i not in Correct:
            if i in Incorrect:
                continue
            determined=determine(os.path.abspath('temp_'+str(i)+'.jpg'),minimum[0])
            if determined:
                Correct.append(i)
                shutil.move(os.path.abspath('temp_'+str(i)+'.jpg'),os.path.abspath(fold))
    return list( set(Correct))
if __name__ == '__main__':
    for i in range(22,39):
        
        start_time = time()
        print(str(i)+'.jpg')
        c=getImage(r'D:\Localsend\nYA\CaptchaKiller\1\\'+str(i)+'.jpg')
        print(c)
        end_time = time()
        print("Time taken:", end_time - start_time)
        exit()
#    ckld=wd.find_elements(By.CLASS_NAME,'geetest_item_ghost')
#ckld[i].click()
