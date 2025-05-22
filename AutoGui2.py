import uiautomator2 as u2
from UiAuto import getAnswer
from time import sleep
import os
import win32gui
import win32con
import Blacklist
import StatusSet

blacklist = Blacklist.Blacklist()
blacklist.initialise()

StatusSet.log('Starting Emulator')
os.startfile("Emulator.lnk")

hwnd=False

HWNDTITLE="雷电模拟器-1"
# 打开雷电模拟器
while not hwnd:
    sleep(5)
    hwnd = win32gui.FindWindow(None, HWNDTITLE)
StatusSet.log('Emulator located')


MSGWD=r'[\]'
PACKAGE=r'com.mihoyo.hyperion'
MESSAGEXPATH=r'/hierarchy/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
ICON=r'//*[@resource-id="com.mihoyo.hyperion:id/iconImageView"]'
ICON1=r'//*[@resource-id="com.mihoyo.hyperion:id/iconLayout"]'
MESSAGES=r'//*[@resource-id="com.mihoyo.hyperion:id/msgBubbleLayout"]'
B='//*[@resource-id="com.mihoyo.hyperion:id/msgTextView"]'
'//*[@resource-id="com.mihoyo.hyperion:id/messageClipView"]'
INPUT=r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]'
SENDKEY=r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.ImageView[1]'
while True:
    try:
        device=u2.connect()
        break
    except:
        sleep(5)
        continue
print(device.info)

StatusSet.log(f'Device connected: {device.info}')

device.press('home')


device.app_start(PACKAGE)

device.implicitly_wait(300)




try:
    for users in  blacklist.getUsersWithCountOverTen():
        StatusSet.log(f'Blacklisting {users}')
        print(users)
        device.xpath(r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]\/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[\1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]').click()
        sleep(2)
        device.xpath(r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').set_text(users)
        sleep(2)
        device.send_keys('enter')
        sleep(2)
        device.xpath(r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.\LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[\1]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[6]/androi\d.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        sleep(2)
        device.xpath(r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.\LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[\1]/androidx.viewpager.widget.ViewPager[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.Lin\earLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]').click()
        sleep(2)
        device.xpath(r'/hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.\LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/an\droid.widget.ImageView[2]').click()
        sleep(2)
        device(text='拉黑').click()
        device(text='确定').click()
        for _ in range(2):
            device.press('back')
            sleep(2)
        StatusSet.log(f'{users} Done !')
except:
    pass
try:
    StatusSet.log(f'chatting')
    device.xpath(MESSAGEXPATH).click()
    device(text='聊天').click()

    for index,path in enumerate(device.xpath(ICON).all()):
        StatusSet.log(f'{index+1} | Chatting')
        path.click()
        sleep(2)
        question=''
        questions=[]
        for path in device.xpath(B).all():
            questions.append(path.text.strip())
        for i in questions:
            print(i)
            if MSGWD not in i and i!='':
                question=i
        print('>>>',question) 
        StatusSet.log(f'>>>{question}')
        if question!='':

            answer=getAnswer(question)

            StatusSet.log(f'<<<{answer}')
            answer=answer+MSGWD
            device.xpath(INPUT).set_text(answer)
            sleep(4)
            device.xpath(SENDKEY).click()
        StatusSet.log(f'{index+1}Done !')
        sleep(2)
        device.press('back')
        sleep(8)
        device.press('back')
        sleep(8)
except Exception as e:
    print(e)
    StatusSet.log(f'Error: {e}')
    pass
device.app_stop(PACKAGE)
win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
#device.xpath(INPUT).click()
def empty():
    pass