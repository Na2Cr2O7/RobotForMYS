import psutil
from datetime import datetime
def getModelChoice():
    
    if datetime.now().hour in range(21,24) or datetime.now().hour in range(0,8):
        return False
    battery = psutil.sensors_battery()
    return battery.power_plugged
