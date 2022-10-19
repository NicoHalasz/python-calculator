# Nico Halasz
# 15/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import everything from the tkinter library
from turtle import color # import the colours from the turtle library

def button_press(num):   # defining what happenes when you press a button (exluding equals and clear)
    global equation_text

    equation_text = equation_text + str(num) # adds the button input onto the equation

    equation_label.set(equation_text) # sets the label to the new equation 

def equals(): # defining what happenes when you press the equals button
    global equation_text

    equation_text = equation_text.replace("÷","/") # replaces any ÷ with a / for the equation
    equation_text = equation_text.replace("×","*") # replaces any × with a * for the equation

    try:  # try is used in try...expect blocks. It defines a block of ocde test if it contains any errors.
          # You can define different blocks for different errpr types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text)) # sets the variable "total" to the completed equation

        equation_label.set(total) # sets the label to the variable "total" which is storing the completed equation

        equation_text = total # sets the equation to the variable "total" which is storing the completed equation

    except SyntaxError: # check for syntax error

        equation_label.set("Order does not make sense") # displays "Order does not make sense" if there is a syntax error

        equation_text = "" # resets equation if there is a syntax error

    except ZeroDivisionError: # checks for division by zero

        equation_label.set("Cannot divide by 0") # displays "Cannot divide by 0" if the user divides by zero

        equation_text = "" # resets the equation if the user divides by 0


def clear(): # defining wht happens when you press the clear/reset button
    global equation_label
    global equation_text

    equation_label.set("") # sets the label to nothing

    equation_text = " " # sets the equation to nothing


window = Tk()
window.title("Python Calculator") # Set the name of the window
window.geometry("400x500") # Set the size of the window
window.configure(bg="royalblue4") # Set the background colour of the window

equation_text = "" # sets the equation to nothing when you first start up the calculator

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="springgreen3", width=23, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# create the buttons (0 - 9)

button1 = Button(frame, text=1, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(0))
button0.grid(row=3, column=0)

# create the operation buttons

plus = Button(frame, text='+', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('+'))
plus.grid(row=1, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('-'))
minus.grid(row=2, column=3)

multiply = Button(frame, text='×', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('×'))
multiply.grid(row=3, column=2)

divide = Button(frame, text='÷', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('÷'))
divide.grid(row=3, column=1)

# create equals

equal = Button(window, text='=', height=4, width=40, font=35, bg="brown1", activebackground="coral2", command=equals)
equal.pack() 

# create decimal

decimal = Button(frame, text='.',  height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('.'))
decimal.grid(row=3, column=3)

# create clear button

clear = Button(frame, text='Reset', height=4, width=9, font=35, bg="greenyellow", activebackground="olivedrab1", command=clear)
clear.grid(row=0, column=3)

window.mainloop()