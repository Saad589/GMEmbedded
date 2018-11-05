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


ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=9600)


root = Tk()
root.title("Radiation Logger by Saad Islam")


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
label_10.config(font = ('Arial', 18, 'bold'), compound = "right")
label_10.grid(row = 1, column = 2)





label_2 = ttk.Label(root, text="CPM:")
label_2.config(font = ('Arial', 18, 'bold'))
label_2.grid(row = 2, column = 0)

label_20 = ttk.Label(root, text="NaN")
label_20.config(font = ('Arial', 18, 'bold'))
label_20.grid(row = 2, column = 2)


label_3 = ttk.Label (root, text="Dose, uSv (Soft Tissue):")
label_3.config(font = ('Arial', 18, 'bold'))
label_3.grid(row = 3, column = 0)

label_30 = ttk.Label (root, text="NaN")
label_30.config(font = ('Arial', 18, 'bold'))
label_30.grid(row = 3, column = 2)





label_4 = ttk.Label(root, text="Anode Voltage, V:")
label_4.config(font = ('Arial', 18, 'bold'))
label_4.grid(row = 4, column = 0)

label_40 = ttk.Label(root, text="440")
label_40.config(font = ('Arial', 18, 'bold'))
label_40.grid(row = 4, column = 2)


label_5 = ttk.Label(root, text="Dead Time, sec:")
label_5.config(font = ('Arial', 18, 'bold'))
label_5.grid(row = 5, column = 0)

label_50 = ttk.Label(root, text="190uS ")
label_50.config(font = ('Arial', 18, 'bold'))
label_50.grid(row = 5, column = 2)


label_6 = ttk.Label(root, text="System Voltage, V:")
label_6.config(font = ('Arial', 18, 'bold'))
label_6.grid(row = 6, column = 0)

label_60 = ttk.Label(root, text="5.24")
label_60.config(font = ('Arial', 18, 'bold'))
label_60.grid(row = 6, column = 2)


label_7 = ttk.Label(root, text="Exposure, mR:")
label_7.config(font = ('Arial', 18, 'bold'))
label_7.grid(row = 7, column = 0)

label_70 = ttk.Label(root, text="NaN")
label_70.config(font = ('Arial', 18, 'bold'))
label_70.grid(row = 7, column = 2)


label_8 = ttk.Label(root, text="***hardware interrupt engaged***", foreground = "red")
label_8.config(font = ('Arial', 18, 'italic'))
label_8.grid(row = 8, column = 0, columnspan = 3)

lab = Label(root)
lab.grid(row = 9, column = 0, columnspan = 3)
def clock():
    #ser.flush()
    #ser.flushInput()
    #ser.flushOutput()
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(100, clock) # run itself again after 1000 ms
    #bytesToRead = ser.inWaiting()
    #data = ser.read(bytesToRead)
    
    ser.write(b'0')
    data_1 = ser.readline().decode("ascii").split("\r\n")
    label_10.config(text = data_1)

    ser.write(b'1')
    data_2 = ser.readline().decode("ascii").split("\r\n")
    label_20.config(text = data_2)

    ser.write(b'2')
    data_3 = ser.readline().decode("ascii").split("\r\n")
    label_30.config(text = data_3)

    ser.write(b'3')
    data_4 = ser.readline().decode("ascii").split("\r\n")
    label_70.config(text = data_4)


# run first time
clock()


label_9 = ttk.Label(root, image = footer)
label_9.grid(row = 10, column = 0, columnspan = 3)



root.mainloop()

























