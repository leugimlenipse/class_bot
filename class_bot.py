import pyautogui 
import datetime
import time

#class schedule
#get day of week
#if x day, take class info, open zoom and enter class

class_schedule = {
    'monday':{
        'data_bases':{
            'id':'92076025043',
            'password':'XXXXX'
        }
    },
    'tuesday':{
        'calculus':{'id': '98133934689', 'password':'XXXXX'},
        'statistics': {'id': '97679365106', 'password': 'XXXXX'},
        'sd': {'id': '94642010910', 'password': 'XXXXX'},
        'mgmt': {'id': '97420559935', 'password': 'XXXXX'}
    },
    'wednesday':{
        'data_bases':{'id': '93129044428', 'password': 'XXXXX'}
    },
    'thursday':{
        'calculus':{'id': '94371380155', 'password':'XXXXX'},
        'statistics': {'id': '94973659096', 'password': 'XXXXX'},
        'sd': {'id': '93162782858', 'password': 'XXXXX'},
        'mgmt': {'id': '94595978284', 'password': 'XXXXX'}
    }
}

#obs position: x=352, y=752
#zoom position: x=423, y=748
def record_class():
    pyautogui.click(x=309, y=752) #open obs
    time.sleep(3)
    pyautogui.click(x=1038, y=549) #start recording
    time.sleep(1)
    pyautogui.click(x=1009, y=80) #minimize obs

def enter_class(id, password):
    pyautogui.click(x=348, y=752) #open zoom
    time.sleep(4)
    pyautogui.click(x=705, y=288) #click join
    time.sleep(2)
    pyautogui.click(x=563, y=328) #click on class id field
    pyautogui.typewrite(id)
    pyautogui.click(x=525, y=429)
    pyautogui.click(x=527, y=465)
    pyautogui.click(x=702, y=498) #go to type password
    time.sleep(2)
    pyautogui.click(x=566, y=325)
    pyautogui.typewrite(password)
    pyautogui.click(x=690, y=499) #join class

def class_day():
    day = datetime.datetime.today().weekday()
    hour, minute = datetime.datetime.today().hour, datetime.datetime.today().minute
    
    if day==1 or day==3:
        #tuesday classes
        if day==1 and hour==8 and 0<=minute<=20:
            id = class_schedule['tuesday']['calculus']['id']
            password = class_schedule['tuesday']['calculus']['password']
            record_class()
            enter_class(id, password)
        elif day==1 and hour==10 and 0<=minute<=20:
            id = class_schedule['tuesday']['statistics']['id']
            password = class_schedule['tuesday']['statistics']['password']
            record_class()
            enter_class(id, password)
        elif day==1 and hour==14 and 0<=minute<=20:
            id = class_schedule['tuesday']['sd']['id']
            password = class_schedule['tuesday']['sd']['password']
            record_class()
            enter_class(id, password)
        elif day==1 and hour==18 and 0<=minute<=20:
            id = class_schedule['tuesday']['mgmt']['id']
            password = class_schedule['tuesday']['mgmt']['password']
            enter_class(id, password)
        
        #thursday classes
        if day==3 and hour==8 and 0<=minute<=20:
            id = class_schedule['thursday']['calculus']['id']
            password = class_schedule['thursday']['calculus']['password']
            record_class()
            enter_class(id, password)
        elif day==3 and hour==10 and 0<=minute<=20:
            id = class_schedule['thursday']['statistics']['id']
            password = class_schedule['thursday']['statistics']['password']
            record_class()
            enter_class(id, password)
        elif day==3 and hour==14 and 0<=minute<=20:
            id = class_schedule['thursday']['sd']['id']
            password = class_schedule['thursday']['sd']['password']
            record_class()
            enter_class(id, password)
        elif day==3 and hour==18 and 0<=minute<=20:
            id = class_schedule['thursday']['mgmt']['id']
            password = class_schedule['thursday']['mgmt']['password']
            enter_class(id, password)
    
    elif day==0 or day==2:
        #monday and wednesday classes
        if day==0 and hour==14 and 0<=minute<=20:
            id = class_schedule['monday']['data_bases']['id']
            password = class_schedule['monday']['data_bases']['password']
            enter_class(id, password)
        elif day==2 and hour==14 and 0<=minute<=20:
            id = class_schedule['wednesday']['data_bases']['id']
            password = class_schedule['wednesday']['data_bases']['password']
            enter_class(id, password)

if __name__=='__main__':
    class_day()
