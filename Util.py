import os
import time
import tqdm
from datetime import datetime
from time import sleep
def getFileTime(file):
    ctime = os.path.getctime(file)
    return time.localtime(ctime)
def renewRepliedCount():
    try:
        i=os.listdir('./p/')[0]
    except IndexError:
        return True
        
   

    if getFileTime('./p/'+i).tm_mday != time.localtime().tm_mday:
        for file in os.listdir('./p/'):
            os.remove('./p/'+file)
        return True
    return False

def getRepliedCount():
    a=time.localtime().tm_mday
    count=0
    for i in tqdm.tqdm(os.listdir('./p/')):
       if getFileTime('./p/'+i).tm_mday == a:
           count+=1
    return count
        
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
        except:
            print('保存失败')        

def writeCount():
    k=datetime.now()
    kl=str(k.hour)+str(k.minute)+str(k.second)
    o3=open('.\\P\\'+kl,'w')
    o3.close()       
    
    
    
