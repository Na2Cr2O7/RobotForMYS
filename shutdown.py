import os
import time
from datetime import datetime
import psutil
def getBatteryStatus():
    battery = psutil.sensors_battery()
    
    if battery:
        percent=battery.percent
        plugged=battery.power_plugged
        return percent, plugged
    return None, None
def getCPUStatus():
    cpu_percent = psutil.cpu_percent(interval=0.1)
    return cpu_percent
def getMemoryStatus():
    memory_percent = psutil.virtual_memory().percent
    return memory_percent
numberString=[r''' 
 ________     
|\   __  \    
\ \  \|\  \   
 \ \  \\\  \  
  \ \  \\\  \ 
   \ \_______\
    \|_______|
              ''',r'''  
  _____     
 / __  \    
|\/_|\  \   
\|/ \ \  \  
     \ \  \ 
      \ \__\
       \|__| 
''',r'''  
  _______     
 /  ___  \    
/__/|_/  /|   
|__|//  / /   
    /  /_/__  
   |\________\
    \|_______|
''',r'''
 ________     
|\_____  \    
\|____|\ /_   
      \|\  \  
     __\_\  \ 
    |\_______\
    \|_______|
              ''',r'''
 ___   ___     
|\  \ |\  \    
\ \  \\_\  \   
 \ \______  \  
  \|_____|\  \ 
         \ \__\
          \|__|
               ''',r''' 
 ________      
|\   ____\     
\ \  \___|_    
 \ \_____  \   
    _____\  \ 
   |\________\
   \|________|
''',r'''
 ________     
|\   ____\    
\ \  \___|    
 \ \  \____   
  \ \  ___  \ 
   \ \_______\
    \|_______|
    ''',r'''
 ________     
|\  ___  \    
 \|___/  /|
     /  / /
    /  / / 
   /__/ /  
   |__|/   
           ''',r''' 
________     
|\   __  \    
\ \  \|\  \   
 \ \   __  \  
  \ \  \|\  \ 
   \ \_______\
    \|_______|
    ''',r''' 
________     
|\  ___  \    
\ \____   \   
 \|____|\  \  
     __\_\  \ 
    |\_______\
    \|_______|
              ''']
splitStr=r'''        
 ___    
|\__\   
\|__|   
    ___ 
   |\__\
   \|__|
        
        '''
def print4numbers(h1, h2, m1, m2):
    # 获取每个数字对应的艺术字
    digit_h1 = numberString[h1].split('\n')
    digit_h2 = numberString[h2].split('\n')
    digit_m1 = numberString[m1].split('\n')
    digit_m2 = numberString[m2].split('\n')
    splitLst=splitStr.split('\n')
    # 横向打印艺术字
    for i in range(9):  # 跳过第一个空行
        
        print(digit_h1[i] + ' ' + digit_h2[i] + ' '+' '+ splitLst[i] +' '+ digit_m1[i] + ' ' + digit_m2[i])

def should_shutdown():
    now = datetime.now()
    return now.hour >= 22 and now.minute >= 30
def shutdownCommand():
    os.system("shutdown /a")
    os.system("shutdown /s /t 3")
def drawProcessBar(percent,length=20):
    bar_length = length
    filled_length = int(bar_length * percent // 100)
    bar = '0' * filled_length + ' ' * (bar_length - filled_length)
    print('['+bar+']')
def main():
    os.system("cls")
    while True:
        percent , plugged = getBatteryStatus()
        if plugged:
            print('⚡',end='')
        
        if percent:
            print(f'🔋 {percent}%',end='\t')
            drawProcessBar(percent,50)
        if not plugged and plugged!= None:
            shutdownCommand()
        CPUStat=getCPUStatus()
        print(f'CPU {CPUStat}%',end='\t')
        drawProcessBar(CPUStat,50)
        MemoryStat=getMemoryStatus()
        print(f'RAM {MemoryStat}%',end='\t')
        drawProcessBar(MemoryStat,50)

        now = datetime.now()
        h1=now.hour//10
        h2=now.hour%10
        m1=now.minute//10
        m2=now.minute%10
        print4numbers(h1, h2, m1, m2)
        if should_shutdown():
            shutdownCommand()
        time.sleep(10)
        os.system("cls")
        


if __name__ == "__main__":
    main()
