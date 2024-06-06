from tkinter import *
import tkinter

Keyboard_App = tkinter.Tk()
Keyboard_App.title('kalkulator')
mas=[0,0,'','','']
b=0

    
    
a=0
h=0

def select(value):
    global a,b,h
    
    if value=='+' or value=='-' or value=='*' or value=='/':
        h=10

    if value=='+' or value=='-' or value=='*' or value=='/':
        mas[2]=value
        input = entry.get("100.0", 'end-2c')
        entry.delete("1.0", END)
        entry.insert("1.0", input, END)
        
    if h==10:
        if value=='1':
            b=b*10+1

        if value=='2':
            b=b*10+2

        if value=='3':
            b=b*10+3

        if value=='4':
            b=b*10+4

        if value=='5':
            b=b*10+5

        if value=='6':
            b=b*10+6

        if value=='7':
            b=b*10+7

        if value=='8':
            b=b*10+8

        if value=='9':
            b=b*10+9

        if value=='0':
            b=b*10+0

        if value=='-(x)':
            mas[3]='-(x)'


        if value.isdigit():
            input = entry.get("100.0", 'end-2c')
            entry.delete("1.0", END)
            entry.insert("1.0", input, END)
            if mas[3]=='-(x)':
                mas[1]=(-mas[1])
            else:
                mas[1]=b
            entry.insert(tkinter.END, mas[1])


    else:
        if value=='1':
            a=a*10+1

        if value=='2':
            a=a*10+2

        if value=='3':
            a=a*10+3

        if value=='4':
            a=a*10+4

        if value=='5':
            a=a*10+5

        if value=='6':
            a=a*10+6

        if value=='7':
            a=a*10+7

        if value=='8':
            a=a*10+8

        if value=='9':
            a=a*10+9

        if value=='0':
            a=a*10+0
        
        if value=='-(x)':
            mas[4]='-(x)'


        if value.isdigit():
            input = entry.get("100.0", 'end-2c')
            entry.delete("1.0", END)
            entry.insert("1.0", input, END)
            if mas[4]=='-(x)':
                mas[0]=(-mas[0])
            else:
                mas[0]=a
            entry.insert(tkinter.END, mas[0])


    if value=='=':
        if mas[2]=='+':
            c=mas[0]+mas[1]

        if mas[2]=='-':
            c=mas[0]-mas[1]            

        if mas[2]=='*':
            c=mas[0]*mas[1]

        if mas[2]=='/':
            c=mas[0]/mas[1]

        input = entry.get("100.0", 'end-2c')
        entry.delete("1.0", END)
        entry.insert("1.0", input, END)
        entry.insert(tkinter.END, ('%.f'%c))
        mas[0]=c
        b=0
        a=0
        mas[4]=''
        mas[3]=''


    if value == "<-":
        input = entry.get("1.0", 'end-2c')
        entry.delete("1.0", END)
        entry.insert("1.0", input, END)

    if value == "C":
        input = entry.get("100.0", 'end-2c')
        entry.delete("1.0", END)
        entry.insert("1.0", input, END)
        a=mas[0]=0
        b=mas[1]=0
        mas[4]=''
        mas[3]=''
        h=0
    
buttons = [
    'C', 'CE', '<-', '/', '1', '2', '3', '*', '4', '5', '6', '+', '7', '8', '9', '-', '.', '0', '-(x)', '=',
]
entry = Text(Keyboard_App, width=15, height=1,font=("Arial", 27))
entry.grid(row=1, columnspan=15)

varRow = 2
varColumn = 0


for button in buttons:
    comman = lambda x=button: select(x)
    if button != " Space ":
        tkinter.Button(Keyboard_App, text=button, width=6, bg="aqua", fg="black",
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                       pady=4, bd=4, command=comman).grid(row=varRow, column=varColumn)

    if button.isdigit():
        tkinter.Button(Keyboard_App, text=button, width=6, bg="#000000", fg="white",
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                       pady=4, bd=4, command=comman).grid(row=varRow, column=varColumn)

    varColumn += 1
    if varColumn > 3:
        varColumn = 0
        varRow += 1
Keyboard_App.mainloop()