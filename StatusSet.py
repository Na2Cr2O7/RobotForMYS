from datetime import datetime
import dill as pickle
import os
statusList=[]
class StatuswithTime:
    status=""
    time=datetime.now()
if os.path.exists("Status.pkl"):
    try:
        with open("Status.pkl", "rb") as f:
            statusList=pickle.load(f)
    except:
        pass
def ToArray():
    ar=[]
    for i in statusList:
        ar.append([i.time,i.status])
    return ar
def saveStatusList():
    with open("Status.pkl", "wb") as f:
        pickle.dump(statusList, f)
    with open("log.pkl", "wb") as f:
        pickle.dump(ToArray(), f)
def cleanStatusList():
    if input("Are you sure to clean the status list? (y/n)").lower()=="y":
        statusList.clear()
        saveStatusList()
    else:
        print("Operation cancelled.")
def setStatus(status):
    a=StatuswithTime()
    a.status=status
    a.time=datetime.now()
    statusList.append(a)
    saveStatusList()
def getAllStatus():
    return statusList

def log(status):
    setStatus(status)
if __name__ == "__main__":
    import HTMLPSR
    html=HTMLPSR.toHTMLStatus(ToArray()[-300:][::-1],"Status Log<h2>Last 300 Status:</h2>")
    with open("log.html","w",encoding="utf-8") as f:
        f.write(html)
    import webbrowser
    webbrowser.open("log.html")
    saveStatusList()