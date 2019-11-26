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
    c = PCA9685(channel=0,address=0x40,busnum=1)
    
    c.run(int(pwm_value.get()))
    
    print (pwm_value.get())
def change():
    filea = open("/home/jetson/mycar/config.py", "r+")
    fileaString = filea.read()
    
    idFilter = 'STEERING_LEFT_PWM ='
    idPosition = fileaString.find(idFilter)
    filea.seek(idPosition+20,0)
    filea.write(left_entry.get())
    
    idFilter = 'STEERING_RIGHT_PWM ='
    idPosition = fileaString.find(idFilter)
    filea.seek(idPosition+21,0)
    filea.write(right_entry.get())

    print ('更改成功！')
    filea.close()

master = Tk()
master.title('轉向校準')
master.geometry('400x300')
master.configure(background = 'white')

pwm_value = Scale(master, from_=200, to=500, orient=HORIZONTAL)
pwm_value.set(340)
pwm_value.pack()

try_btn = Button(master, text='try',command=show_values)
try_btn.pack()

left_frame = Frame(master)
left_frame.pack(side=TOP)
left_label = Label(left_frame, text='最左邊:')
left_label.pack(side=LEFT)
left_entry = Entry(left_frame)
left_entry.pack(side=LEFT)

right_frame = Frame(master)
right_frame.pack(side=TOP)
right_label = Label(right_frame, text='最右邊:')
right_label.pack(side=LEFT)
right_entry = Entry(right_frame)
right_entry.pack(side=LEFT)


change_btn =  Button(master, text='更改',command=change)
change_btn.pack()

master.mainloop()
