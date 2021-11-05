import tkinter as tk
from tkinter.constants import CURRENT, END, LEFT
from matplotlib.pyplot import fill,grid, show, text
import math as m

from numpy import radians, square, tan
root=tk.Tk()
root.title("Calculator")
root.geometry("400x600")
data=tk.StringVar()

val=""


root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=4)
root.grid_columnconfigure(0,weight=1)

output_frame = tk.Frame(root,background='white')
output_frame.grid(row=0,column=0,sticky=tk.NSEW)
button_frame = tk.Frame(root,background='white')
button_frame.grid(row=1,column=0,sticky=tk.NSEW)

for i in range(7):
    button_frame.rowconfigure(i,weight=1)
for j in range(4):
    button_frame.columnconfigure(j,weight=1)

output_textbox = tk.Entry(output_frame,textvariable=data,bg='#FFE699' ,justify="right",border=20,font="consolas 20")
output_textbox.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

def button_click(number):
    global val
    val = val +str(number)
    data.set(val)

# disploy for enter operatoe
def btn_cal_clicked():
    global val
    if (val == "+" or val == "-" or val == "*" or val == "/"):
        data.set("Err")  
    else:
        val = str(eval(val)+0)
        data.set(val)    

def button_c():
    global val
    val=""
    data.set("")

def button_msin():
    global val
    sin=str(m.sin(m.radians(float(val))))
    data.set(sin)

def button_mcos():
    global val
    cos=str(m.cos(m.radians(float(val))))
    data.set(cos)

def button_mtan():
    global val
    tan=str(m.tan(m.radians(float(val))))
    data.set(tan)

def button_logten():
    global val
    logt=str(m.log10(m.radians(float(val))))
    data.set(logt)

#button
button_1 = tk.Button(button_frame,text=1,background='#FFCCD2',command=lambda:button_click(1),font="consolas 15")
button_2 = tk.Button(button_frame,text=2,background='#FFCCD2',command=lambda:button_click(2),font="consolas 15")
button_3 = tk.Button(button_frame,text=3,background='#FFCCD2',command=lambda:button_click(3),font="consolas 15")
button_4 = tk.Button(button_frame,text=4,background='#FFCCD2',command=lambda:button_click(4),font="consolas 15")
button_5 = tk.Button(button_frame,text=5,background='#FFCCD2',command=lambda:button_click(5),font="consolas 15")
button_6 = tk.Button(button_frame,text=6,background='#FFCCD2',command=lambda:button_click(6),font="consolas 15")
button_7 = tk.Button(button_frame,text=7,background='#FFCCD2',command=lambda:button_click(7),font="consolas 15")
button_8 = tk.Button(button_frame,text=8,background='#FFCCD2',command=lambda:button_click(8),font="consolas 15")
button_9 = tk.Button(button_frame,text=9,background='#FFCCD2',command=lambda:button_click(9),font="consolas 15")
button_0 = tk.Button(button_frame,text=0,background='#FFCCD2',command=lambda:button_click(0),font="consolas 15")
button_dot = tk.Button(button_frame,text=".",background="#FFCCD2",width=10,command=lambda:button_click("."),font="consolas 15")
button_multiple = tk.Button(button_frame,text="x",background="#FFF9B6",command=lambda:button_click("*"),font="consolas 15")
button_divide = tk.Button(button_frame,text="÷",background="#FFF9B6",command=lambda:button_click("/"),font="consolas 15")
button_plus = tk.Button(button_frame,text="+",background="#FFF9B6",command=lambda:button_click("+"),font="consolas 15")
button_minus = tk.Button(button_frame,text="-",background="#FFF9B6",command=lambda:button_click("-"),font="consolas 15")
button_sin = tk.Button(button_frame,text="sin",background='#FF9292',width=15,command=button_msin,font="consolas 15")
button_cos = tk.Button(button_frame,text="cos",background='#FF9292',width=15,command=button_mcos,font="consolas 15")
button_tan = tk.Button(button_frame,text="tan",background="#FF9292",width=15,command=button_mtan,font="consolas 15")
button_log = tk.Button(button_frame,text="log",background="#FFF9B6",width=15,command=button_logten,font="consolas 15")
button_clear = tk.Button(button_frame,text="c",background="#FFCCD2",width=15,command=button_c,font="consolas 15")


#ans
button_ans = tk.Button(button_frame,text="=",background='#FF9292',command=lambda:btn_cal_clicked())
button_ans.grid(row=6,sticky=tk.NSEW,columnspan=4)

#position
button_clear.grid(row=5,column=0,sticky=tk.NSEW)
button_0.grid(row=5,column=1,sticky=tk.NSEW)
button_dot.grid(row=5,column=2,sticky=tk.NSEW)
button_log.grid(row=5,column=3,sticky=tk.NSEW)


button_1.grid(row=4,column=0,sticky=tk.NSEW)
button_2.grid(row=4,column=1,sticky=tk.NSEW)
button_3.grid(row=4,column=2,sticky=tk.NSEW)
button_plus.grid(row=4,column=3,sticky=tk.NSEW)

button_4.grid(row=3,column=0,sticky=tk.NSEW)
button_5.grid(row=3,column=1,sticky=tk.NSEW)
button_6.grid(row=3,column=2,sticky=tk.NSEW)
button_minus.grid(row=3,column=3,sticky=tk.NSEW)

button_7.grid(row=2,column=0,sticky=tk.NSEW)
button_8.grid(row=2,column=1,sticky=tk.NSEW)
button_9.grid(row=2,column=2,sticky=tk.NSEW)
button_multiple.grid(row=2,column=3,sticky=tk.NSEW)

button_sin.grid(row=1,column=0,sticky=tk.NSEW)
button_cos.grid(row=1,column=1,sticky=tk.NSEW)
button_tan.grid(row=1,column=2,sticky=tk.NSEW)
button_divide.grid(row=1,column=3,sticky=tk.NSEW)


root.mainloop()