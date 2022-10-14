from tkinter import *
from turtle import width
from math import sqrt


root = Tk()
root.geometry('400x600')
root.title = 'Kalkulator Franek Skrobot'

def ce():
    score.delete(0, END)

def c():
    sc = score.get()
    sc = sc[:-1]
    score.delete(0, END)
    score.insert(0, sc)


def sqrt_score():
    try:
        pierwiastek = eval(score.get())
        pierwiastek = float(pierwiastek)
        score.delete(0, END)
        score.insert(0, sqrt(pierwiastek))
    except:
        score.delete(0, END)
        score.insert(0,'Err')


class Nums:

    def __init__(self):
        pass
    
    def num1():
        num1 = score.get()
        num1 += '1'
        score.delete(0, END)
        score.insert(0, num1)
    
    def num2():
        num1 = score.get()
        num1 += '2'
        score.delete(0, END)
        score.insert(0, num1)
    
    def num3():
        num1 = score.get()
        num1 += '3'
        score.delete(0, END)
        score.insert(0, num1)

    def num4():
        num1 = score.get()
        num1 += '4'
        score.delete(0, END)
        score.insert(0, num1)

    def num5():
        num1 = score.get()
        num1 += '5'
        score.delete(0, END)
        score.insert(0, num1)

    def num6():
        num1 = score.get()
        num1 += '6'
        score.delete(0, END)
        score.insert(0, num1)

    def num7():
        num1 = score.get()
        num1 += '7'
        score.delete(0, END)
        score.insert(0, num1)

    def num8():
        num1 = score.get()
        num1 += '8'
        score.delete(0, END)
        score.insert(0, num1)

    def num9():
        num1 = score.get()
        num1 += '9'
        score.delete(0, END)
        score.insert(0, num1)

    def num0():
        num1 = score.get()
        num1 += '0'
        score.delete(0, END)
        score.insert(0, num1)

    def plus():
        num1 = score.get()
        num1 += '+'
        score.delete(0, END)
        score.insert(0, num1)

    def minus():
        num1 = score.get()
        num1 += '-'
        score.delete(0, END)
        score.insert(0, num1)

    def divide():
        num1 = score.get()
        num1 += '/'
        score.delete(0, END)
        score.insert(0, num1)
    
    def multiply():
        num1 = score.get()
        num1 += '*'
        score.delete(0, END)
        score.insert(0, num1)

    def dot():
        num1 = score.get()
        num1 += '.'
        score.delete(0, END)
        score.insert(0, num1)



score = Entry(
    root,
    justify='center',
    font=('Arial', 24)
)
score.place(
    width=400,
    height=100
)

ce = Button(
    root,
    text='CE',
    command = ce
).place(
    width=100,
    height=100,
    y=100
)

backspace = Button(
    root,
    text='<-',
    command= c
).place(
    width=100,
    height=100,
    y=100,
    x=100
)

sqrt_btn = Button(
    root,
    text='√',
    command = sqrt_score
).place(
    width=100,
    height=100,
    y=100,
    x=200
)

divide = Button(
    root,
    text='÷',
    command = Nums.divide
).place(
    width=100,
    height=100,
    y=100,
    x=300
)

num7 = Button(
    root,
    text='7',
    command = Nums.num7
).place(
    width=100,
    height=100,
    y=200,
    x=0
)

num8 = Button(
    root,
    text='8',
    command =   Nums.num8
).place(
    width=100,
    height=100,
    y=200,
    x=100
)

num9 = Button(
    root,
    text='9',
    command = Nums.num9
).place(
    width=100,
    height=100,
    y=200,
    x=200
)

multiplication = Button(
    root,
    text='x',
    command = Nums.multiply
).place(
    width=100,
    height=100,
    y=200,
    x=300
)

num6 = Button(
    root,
    text='6',
    command = Nums.num6
).place(
    width=100,
    height=100,
    y=300,
    x=200
)

num5 = Button(
    root,
    text='5',
    command = Nums.num5
).place(
    width=100,
    height=100,
    y=300,
    x=100
)

num4 = Button(
    root,
    text='4',
    command = Nums.num4
).place(
    width=100,
    height=100,
    y=300,
    x=0
)

minus = Button(
    root,
    text='-',
    command = Nums.minus
).place(
    width=100,
    height=100,
    y=300,
    x=300
)

num3 = Button(
    root,
    text='3',
    command = Nums.num3
).place(
    width=100,
    height=100,
    y=400,
    x=200
)

num2 = Button(
    root,
    text='2',
    command = Nums.num2
).place(
    width=100,
    height=100,
    y=400,
    x=100
)

num1 = Button(
    root,
    text='1',
    command = Nums.num1
).place(
    width=100,
    height=100,
    y=400,
    x=0
)

add = Button(
    root,
    text='+',
    command = Nums.plus
).place(
    width=100,
    height=100,
    y=400,
    x=300
)

num0 = Button(
    root,
    text='0',
    command = Nums.num0
).place(
    width=100,
    height=100,
    y=500,
    x=0
)

dot = Button(
    root,
    text='.',
    command = Nums.dot
).place(
    width=100,
    height=100,
    y=500,
    x=100
)


def equal():
    try:
        equal = eval(score.get())
        score.delete(0, END)
        score.insert(0, equal)
    except:
        score.delete(0, END)
        score.insert(0, 'Err')


equals = Button(
    root,
    text='=',
    command = equal
).place(
    width=200,
    height=100,
    y=500,
    x=200
)

root.mainloop()