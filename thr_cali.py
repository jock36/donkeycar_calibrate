# !/usr/bin/python3

from tkinter import *
from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle

import os
import time

from docopt import docopt
import numpy as np

import donkeycar as dk

from donkeycar.parts.transform import Lambda, TriggeredCallback, DelayedTrigger
from donkeycar.parts.datastore import TubHandler
from donkeycar.parts.controller import LocalWebController, JoystickController
from donkeycar.parts.throttle_filter import ThrottleFilter
from donkeycar.parts.behavior import BehaviorPart
from donkeycar.parts.file_watcher import FileWatcher
from donkeycar.parts.launch import AiLaunch

def show_values():
    c = PCA9685(channel=1,address=0x40,busnum=1)
    
    c.run(int(pwm_value.get()))
    
    print (pwm_value.get())
def change():
    filea = open("/home/jetson/mycar/config.py", "r+")
    fileaString = filea.read()
    
    idFilter = 'THROTTLE_FORWARD_PWM ='
    idPosition = fileaString.find(idFilter)
    filea.seek(idPosition+23,0)
    filea.write(for_entry.get())
    
    idFilter = 'THROTTLE_STOPPED_PWM ='
    idPosition = fileaString.find(idFilter)
    filea.seek(idPosition+23,0)
    filea.write(stop_entry.get())

    idFilter = 'THROTTLE_REVERSE_PWM ='
    idPosition = fileaString.find(idFilter)
    filea.seek(idPosition+23,0)
    filea.write(rev_entry.get())

    print ('更改成功！')
    filea.close()

master = Tk()
master.title('油門校準')
master.geometry('400x300')
master.configure(background = 'white')

pwm_value = Scale(master, from_=200, to=500, orient=HORIZONTAL)
pwm_value.pack()

try_btn = Button(master, text='try',command=show_values)
try_btn.pack()

for_frame = Frame(master)
for_frame.pack(side=TOP)
for_label = Label(for_frame, text='前進:')
for_label.pack(side=LEFT)
for_entry = Entry(for_frame)
for_entry.pack(side=LEFT)

stop_frame = Frame(master)
stop_frame.pack(side=TOP)
stop_label = Label(stop_frame, text='停止:')
stop_label.pack(side=LEFT)
stop_entry = Entry(stop_frame)
stop_entry.pack(side=LEFT)

rev_frame = Frame(master)
rev_frame.pack(side=TOP)
rev_label = Label(rev_frame, text='後退:')
rev_label.pack(side=LEFT)
rev_entry = Entry(rev_frame)
rev_entry.pack(side=LEFT)

change_btn =  Button(master, text='更改',command=change)
change_btn.pack()

master.mainloop()
