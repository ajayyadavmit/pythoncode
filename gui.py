'''
The word Tkinter comes from the Tk interface. The tkinter module is available in Python standard library which has to be imported while writing a program in Python to generate a GUI.

Tkinter comes with four built-in variable objects for us to handle different data types:

    StringVar: This holds characters like a Python string.
    IntVar: This holds an integer value.
    DoubleVar: This holds a double value (a number with a decimal place).
    BooleanVar: This holds a Boolean to act like a flag.

    intvar = tkinter.IntVar(win, value = 25, name ="2")
strvar = tkinter.StringVar(win, "Hello !")
boolvar = tkinter.BooleanVar(win, True)
doublevar = tkinter.DoubleVar(win, 10.25)

print(type(intvar), type(intvar.get()))
print(type(strvar), type(strvar.get()))
print(type(boolvar), type(boolvar.get()))
print(type(doublevar), type(doublevar.get()))


Tkinter supports some variables which are used to manipulate the values of Tkinter widgets. These variables work like normal variables. 
set() and get() methods are used to set and retrieve the values of these variables. 

intvar.set(1111111)
strvar.set("GFGaaaaaaaaaa")
boolvar.set(False)
doublevar.set(10.3622233211333)

print(intvar.get())
print(doublevar.get())


Tkinter uses an object-oriented approach to make GUIs.  
It uses the OBJECT CONSTRUCTOR approach to make the GUI. 
listbox = Listbox(root, bg, fg, bd, height, width, font, ..) 

w = Checkbutton ( master, options)

Parameters:

    master: This parameter is used to represents the parent window.
    options:There are many options which are available and they can be used as key-value pairs separated by commas.

Scale widget is used whenever we want to select a specific value from a range of values. It provides a sliding bar through which we can select the values by sliding from left to right or top to bottom depending upon the orientation of our sliding bar.


'''

# # GUI module in Python.. with Tkinter , we can create the GUI based applications. 
# # tkinter is available in other language RUby Perl 

# # import tkinter

# # # create an Instance of the module tkinter with class Tk() 
# # win = tkinter.Tk()

# # print(type(win))
# # print(dir(win))
# # # main loop function will keep the windows always OPEN and Running. 
# # win.mainloop()

# # widgets  >> Labels, button, Checkbox , Radiobuttons 
# # ttk is Advanced form for the Widgets sections that makes Looks and Feel Good for the tkinter Library. 

# import tkinter
# from tkinter import ttk   #ttk is advanced form of Library for UI Look and Feel. 

# win = tkinter.Tk()
# win.title("Hello Good morning !!")
# # print(dir(win))

# # tkinter.Label(win, text="enter the Name").pack()  # pack() function will place the widget at the Center of Window >> So use the GRID Layout of the Columns. 
# # ttk.Label(win, text="YOur AGE AGE Group").pack()

# name = tkinter.Label(win, text="Name Enter Here")
# print(type(name))
# name.grid(row= 0, column=0)
# place = ttk.Label(win, text="place of study ::")
# place.grid(sticky = tkinter.W)

# study = ttk.Label(win, text="Course Study")
# study.grid(sticky = tkinter.W)

# ## create a TEXT BOX for a Variable Entry Data's 
# v1_value = tkinter.StringVar()
# v1 = tkinter.Entry(win, width=22, textvariable = v1_value)
# v1.grid(row = 0, column = 2, sticky= tkinter.W)
# print(str(v1_value))

# # StringVar () function will be created for the variable name of Entry textBox. 
# s2 = tkinter.StringVar()
# v2 = ttk.Entry(win, width=10, textvariable= s2)
# v2.grid(row= 1,column = 2, sticky= tkinter.W)

# def action():
#     print(s2.get())
#     print(type(s2.get()))
#     print(sv1.get())

# sv1 = tkinter.StringVar()
# tkinter.Label(win, text="location").grid(row = 6, column = 0, sticky = tkinter.W)

# tkinter.Entry(win, textvariable=sv1, width= 33).grid(row = 6, column = 2, sticky = tkinter.W)

# # Button function 

# btn1 = tkinter.Button(win, text="submit", command= action)
# btn1.grid(row= 5, column = 2)

# tkinter.Button(win, text = "new", command = action).grid(row = 8 , column = 3, sticky = tkinter.W)
# win.mainloop()


import tkinter 
from tkinter import ttk

win = tkinter.Tk()
win.geometry('500x400')

tkinter.Label(win, bg= "red", fg= "green" , text = "enter you name here").grid()
s = tkinter.StringVar()


s2 = tkinter.Entry(win, width= 22, textvariable= s)
s2.grid(row = 0, column = 1, sticky = tkinter.W)

# Combobox creation
n = tkinter.StringVar()
monthchoosen = ttk.Combobox(win, width = 27, textvariable = n)

monthchoosen['values'] = ('av','bd','cc')
monthchoosen.grid(column = 1, row = 5)


Checkbutton1 = tkinter.IntVar()
Checkbutton2 = tkinter.IntVar()
Checkbutton3 = tkinter.IntVar()

Button1 = tkinter.Checkbutton(win, text = "Tutorial",
					variable = Checkbutton1,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Button2 = tkinter.Checkbutton(win, text = "Student",
					variable = Checkbutton2,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Button3 = tkinter.Checkbutton(win, text = "Courses",
					variable = Checkbutton3,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)
	
Button1.grid()
Button2.grid()
Button3.grid()

tkinter.Entry(win,background="red").grid(row= 1, column =1, sticky= tkinter.E)


def fn1():
    print(s.get())
    b = int(s.get())
    print(b+ 10)
    print(n.get())
    print(Checkbutton1.get())
    print(Checkbutton2.get())
    print(Checkbutton3.get())

tkinter.Button(win, text="submit", command= fn1).grid(row= 3, column = 1, sticky = tkinter.W)


# create listbox object
listbox = tkinter.Listbox(win, height = 10,
				width = 15,
				bg = "grey",
				activestyle = 'dotbox',
				font = "Helvetica",
				fg = "yellow")


# Define a label for the list.
label = tkinter.Label(win, text = " FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.grid(row = 10, column = 0, sticky = tkinter.W)
listbox.grid(row = 10 , column = 1 , sticky = tkinter.W)


win.mainloop() 

'''
'''
import tkinter as tk 
from tkinter import ttk 
win = tk.Tk()
win.title(" Play Games @@ HOME @@")
win.geometry("1400x800")

s = tk.StringVar()
tk.Label(win, bg= "red" ,text= "11111111").pack()
tk.Entry(win, background= "green",width= 22, textvariable= s).pack()

def action():
    print(f" the value is {s.get()}")

a1 = tk.IntVar()

tk.Label()
tk.Button(win, text="Submit", command= action).pack()


# Python program to demonstrate
# scale widget

v1 = tkinter.DoubleVar()

def show1():
	sel = "Horizontal Scale Value = " + str(v1.get())
	l1.config(text = sel, font =("Courier", 14)) ; a = v1.get() ; print(a)

s1 = tkinter.Scale( win, variable = v1,
		from_ = 1, to = 100,
		orient = tkinter.HORIZONTAL)

l3 = tkinter.Label(win, text = "Horizontal Scaler")

b1 = tkinter.Button(win, text ="Display Horizontal",
			command = show1,
			bg = "yellow")

l1 = tkinter.Label(win)


s1.pack(anchor = tkinter.CENTER)
l3.pack()
b1.pack(anchor = tkinter.CENTER)
l1.pack()


intvar = tkinter.IntVar(win, value = 25, name ="2")
strvar = tkinter.StringVar(win, "Hello !")
boolvar = tkinter.BooleanVar(win, True)
doublevar = tkinter.DoubleVar(win, 10.25)

print(type(intvar), type(intvar.get()))
print(type(strvar), type(strvar.get()))
print(type(boolvar), type(boolvar.get()))
print(type(doublevar), type(doublevar.get()))


intvar.set(1111111)
strvar.set("GFGaaaaaaaaaa")
boolvar.set(False)
doublevar.set(10.3622233211333)

print(intvar.get())
print(doublevar.get())
tk.mainloop()

