import os 
import datetime
import time

#class schedule
#get day of week, get hour of day
#if x day, take class info, open zoom and enter class

obs_path = 'C:\\Program Files\\obs-studio\\bin\\64bit'

class_schedule = {
    'monday':{
        'data_bases':{
            'id':'92076025043',
            'password':'105407'
        }
    },
    'tuesday':{
        'calculus':{'id': '98133934689', 'password':'XXXXXX'},
        'statistics': {'id': '97679365106', 'password': 'XXXXXX'},
        'sd': {'id': '94642010910', 'password': 'XXXXXX'},
        'mgmt': {'id': '97420559935', 'password': 'XXXXXX'}
    },
    'wednesday':{
        'data_bases':{'id': '93129044428', 'password': 'XXXXXX'}
    },
    'thursday':{
        'calculus':{'id': '94371380155', 'password':'XXXXXX'},
        'statistics': {'id': '94973659096', 'password': 'XXXXXX'},
        'sd': {'id': '93162782858', 'password': 'XXXXXX'},
        'mgmt': {'id': '94595978284', 'password': 'XXXXXX'}
    }
}

def record_class():
    os.chdir(obs_path)
    os.system('start obs64.exe --startrecording --minimize-to-tray')

def enter_class(day, class_):
    id = class_schedule[day][class_]['id']
    password = class_schedule[day][class_]['password']
    os.system(f'start Zoom.exe --url="https://renata.zoom.us/j/{id}?pwd={password}"')

def class_day():
    day = datetime.datetime.today().weekday()
    hour, minute = datetime.datetime.today().hour, datetime.datetime.today().minute
    
    if day==1 or day==3:
        #tuesday classes
        if day==1 and hour==8 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('tuesday', 'calculus')
        elif day==1 and hour==10 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('tuesday', 'statistics')
        elif day==1 and hour==14 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('tuesday', 'sd')
        elif day==1 and hour==18 and 0<=minute<=20:
            enter_class('tuesday', 'mgmt')
        
        #thursday classes
        if day==3 and hour==8 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('thursday', 'calculus')
        elif day==3 and hour==10 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('thursday', 'statistics')
        elif day==3 and hour==14 and 0<=minute<=20:
            record_class()
            time.sleep(2)
            enter_class('thursday', 'sd')
        elif day==3 and hour==18 and 0<=minute<=20:
            enter_class('thursday', 'mgmt')
    
    elif day==0 or day==2:
        #monday and wednesday classes
        if day==0 and hour==14 and 0<=minute<=20:
            enter_class('monday', 'data_bases')
        elif day==2 and hour==14 and 0<=minute<=20:
            enter_class('wednesday', 'data_bases')

if __name__=='__main__':
    class_day()
