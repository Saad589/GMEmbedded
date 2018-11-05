# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:01:30 2017

@author: saad589
"""
from tkinter import *
from tkinter import ttk
import serial
import datetime
import time

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)



##    bytesToRead = ser.inWaiting()
##    data = ser.read(bytesToRead)
##    data = ser.readline()


##    print(data)



root = Tk()

header = PhotoImage(file = "Header.gif")
footer = PhotoImage(file = "Footer.gif")
sv = PhotoImage(file = "sv.gif")
rem = PhotoImage(file = "rem.gif")

label_0 = ttk.Label(root, image = header)
label_0.grid(row = 0, column = 0, columnspan = 3)


label_1 = ttk.Label(root, text="Counts:")
label_1.config(font = ('Arial', 18, 'bold'))
label_1.grid(row = 1, column = 0)




label_10 = ttk.Label(root, text = "NaN")
label_10.config(font = ('Arial', 18, 'bold'), compound = "left")
label_10.grid(row = 1, column = 2)

lab = Label(root)
lab.grid()
def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms
    bytesToRead = ser.inWaiting()
    data = ser.read(bytesToRead).decode("ascii")
    label_10.config(text = data)


# run first time
clock()




label_2 = ttk.Label(root, text="CPM:")
label_2.config(font = ('Arial', 18, 'bold'))
label_2.grid(row = 2, column = 0)


label_3 = ttk.Label(root, text="Dose (Soft Tissue):")
label_3.config(font = ('Arial', 18, 'bold'))
label_3.grid(row = 3, column = 0)

#def callback():

    
button_3 = ttk.Button(root)
button_3.grid(row = 3, column = 2) 
button_3.config(image = rem)
#button_3.config(command = callback)






label_4 = ttk.Label(root, text="Anode Voltage:")
label_4.config(font = ('Arial', 18, 'bold'))
label_4.grid(row = 4, column = 0)


label_5 = ttk.Label(root, text="Dead Time:")
label_5.config(font = ('Arial', 18, 'bold'))
label_5.grid(row = 5, column = 0)


label_6 = ttk.Label(root, text="System Voltage:")
label_6.config(font = ('Arial', 18, 'bold'))
label_6.grid(row = 6, column = 0)


label_7 = ttk.Label(root, text="Exposure:")
label_7.config(font = ('Arial', 18, 'bold'))
label_7.grid(row = 7, column = 0)


label_8 = ttk.Label(root, text="***hardware interrupt engaged***", foreground = "red")
label_8.config(font = ('Arial', 18, 'italic'))
label_8.grid(row = 8, column = 0, columnspan = 3)

label_9 = ttk.Label(root, image = footer)
label_9.grid(row = 9, column = 0, columnspan = 3)



root.mainloop()

























