# -*- coding: utf-8 -*-
"""
@author: Viorel Mihaescu
"""

import os
from datetime import datetime
from playsound import playsound
from pytz import timezone

easten_time = timezone('EST5EDT')
print(datetime.now(easten_time))


#set and check hour
def set_hour():
    print("Hello, \nThe clock is setting according to AM/PM!")
    while True:
        try:
            alarm_hour = int(input("Set the hour:"))
        except ValueError:
            print("Sorry, I didn't understand!The hour must be a number, please try again...")
            continue
        if  alarm_hour>23:
            print("Invalid,the hour must be between 0-23! Please try again...")
            continue
        if  alarm_hour<0:
            print("Sorry, the hour must not be negative!Please try again...")
            continue
        else:
            return alarm_hour

#set and check minutes    
def set_minutes():
    while True:
        try:
            alarm_minutes = int(input("Set the minutes:"))    
        except ValueError:
            print("Sorry, I didn't understand!The minutes must be a number, please try again..")
            continue
        if  alarm_minutes>59:
            print("Invalid,the minutes must be between 0-59! Please try again...")
            continue
        if  alarm_minutes<0:
            print("Sorry, the minutes can't be negative!Please try again...")
            continue
        else:
            return alarm_minutes   
        
#set and check beeps
def set_beeps():
    while True:
        try:
            beeps = int(input("How many beeps?"))
        except ValueError:
            print("Sorry, I didn't understand!The beeps must be a number, please try again..")
            continue
        if  beeps<0:
            print("Sorry,can't be negative!Please try again...")
            continue
        else:
            return beeps

#alarm ON        
def alarm_on():
    print(f"Alarm is set: {alarm_hour}:{alarm_minutes}")
    while(True):
        if(alarm_hour == datetime.now(easten_time).hour and alarm_minutes == datetime.now(easten_time).minute):
            for i in range(beeps):
               playsound('C:/Users/vio/.spyder-py3/Beep (sound effect).wav')
            print(f"The clock is {alarm_hour}:{alarm_minutes} Eastern Time (ET)")
            break

                 
alarm_hour=set_hour() 
alarm_minutes=set_minutes()
beeps=set_beeps()
alarm_on()


   