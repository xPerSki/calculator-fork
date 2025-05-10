from tkinter import *
from math import sqrt

window = Tk()
window.geometry("340x466")
window.resizable(False, False)
window.title("Kalkulator")
icon = PhotoImage(file="calc_img.png")
window.iconphoto(True, icon)

eq_field = Label(window,
                 font=("Arial", 12, "bold"),
                 text="",
                 justify="right",
                 foreground="gray")
eq_field.grid(row=0, column=0, columnspan=4, pady=2, padx=4, sticky="e")

entry_field = Label(window,
                    font=("Arial", 22, "bold"),
                    justify="right",
                    width=18,
                    anchor='e',
                    borderwidth=0,
                    bg="lightgray")
entry_field.grid(row=1, column=0, columnspan=7, padx=7, pady=(0, 5))


MR = 0


def appendCharacter(character: str):
    old = str(entry_field.cget("text"))
    if old == "" and character in "+-/*":
        pass
    else:
        if old and old[-1] in "+-/*" and character in "+-/*":
            entry_field.config(text=old[:-1] + character)
        else:
            entry_field.config(text=old + character)


def clearEntryLabel():
    entry_field.config(text=eval(eq_field.cget("text")[:-1]))


def clearAll():
    entry_field.config(text="")
    eq_field.config(text="")


def memoryRead():
    old = entry_field.cget("text")
    entry_field.config(text=old + str(MR)) if MR else None


def memoryAdd(minus=False):
    global MR
    number = str(entry_field.cget("text"))
    if minus:
        number = '-' + number

    MR += float(number) if '.' in number else int(number)
    entry_field.config(text="")


def memoryClear():
    global MR
    MR = 0


def backspace():
    old = entry_field.cget("text")
    
    if len(old) >= 3:
        if old[-3] == ")":
            entry_field.config(text=old[1:-3])
        else:
            entry_field.config(text=old[:-1])
    else:   
        entry_field.config(text=old[:-1])

def percent():
    old = entry_field.cget("text")
    val = float(old) / 100
    if int(val) == float(val):
        val = int(val)
    entry_field.config(text=str(val))


def factorial():
    result = 1
    n = entry_field.cget("text")
    try:
        for i in range(2, int(n)+1):
            result *= i
        eq_field.config(text=str(result))
        entry_field.config(text="")
    except ValueError:
        entry_field.config(text="Err")


def changeSign():
    value = str(entry_field.cget("text"))
    if '-' in value:
        entry_field.config(text=value[1:])
    else:
        entry_field.config(text='-' + value)


def equals():
    to_calculate = entry_field.cget("text")

    if to_calculate[-1] in "+-/*":
        if "(" in result:
            to_calculate += ")"
            to_calculate = to_calculate[:-2]+to_calculate[-1]
            result = eval(to_calculate)
            eq_field.config(text=to_calculate+"=")
        
        else:
            result = eval(to_calculate[:-1])
            eq_field.config(text=to_calculate[:-1]+"=")

    else:
        if "(" in to_calculate:
            to_calculate += ")"
            result = eval(to_calculate)
            eq_field.config(text=to_calculate+"=")
        
        else:
            result = eval(to_calculate)
            eq_field.config(text=to_calculate+"=")
    
    if int(result) == result:
        result = int(result)
    entry_field.config(text=result)


def toThePowerOf():
    base = entry_field.cget("text")

    try:
        if base[-1] in "+-/*" and base != "":
                entry_field.config(text=base[:-1] + "**")
        else:
            entry_field.config(text=base + "**")
    except IndexError:
        pass


def rootToThePowerOf():
    base_of_root = entry_field.cget("text")

    try:
        if base_of_root[-1] in "+-/*" and base_of_root != "":
                entry_field.config(text=f"({base_of_root[:-1]})**(")
        else:
            entry_field.config(text=f"({base_of_root})**(")
    except IndexError:
        pass
    
    


MC_button = Button(window, text="MC", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memoryClear)
MC_button.grid(row=2, column=0, pady=(0, 5))

MR_button = Button(window, text="MR", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memoryRead)
MR_button.grid(row=2, column=1, pady=(0, 5))

Mplus_button = Button(window, text="M+", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memoryAdd)
Mplus_button.grid(row=2, column=2, pady=(0, 5))

Mminus_button = Button(window, text="M-", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=lambda: memoryAdd(minus=True))
Mminus_button.grid(row=2, column=3, pady=(0, 5))

backspace_button = Button(window, text="⌫", font=("Arial", 20, "bold"), width=4, height=1, command=backspace)
backspace_button.grid(row=3, column=3)

clear_button = Button(window, text="C", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff0000", command=clearAll)
clear_button.grid(row=3, column=2)

clear_entry_button = Button(window, text="CE", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff8585", command=clearEntryLabel)
clear_entry_button.grid(row=3, column=1)

percentage_button = Button(window, text="%", font=("Arial", 20, "bold"), width=4, height=1, command=percent)
percentage_button.grid(row=3, column=0)

factiorial_button = Button(window, text="x!", font=("Arial", 20, "bold"), width=4, height=1, command=factorial)
factiorial_button.grid(row=4, column=0, pady=5)

pow_to_button = Button(window, text="xⁿ", font=("Arial", 20, "bold"), width=4, height=1, command=toThePowerOf)
pow_to_button.grid(row=4, column=1)

sqrt_by_button = Button(window, text="ⁿ√x", font=("Arial", 20, "bold"), width=4, height=1, command=rootToThePowerOf)
sqrt_by_button.grid(row=4, column=2)

divide_button = Button(window, text="/", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: appendCharacter('/'))
divide_button.grid(row=4, column=3)

button_0 = Button(window, text="0", font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('0'))
button_0.grid(row=8, column=1)

button_1 = Button(window, text=1, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('1'))
button_1.grid(row=7, column=0)

button_2 = Button(window, text=2, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('2'))
button_2.grid(row=7, column=1)

button_3 = Button(window, text=3, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('3'))
button_3.grid(row=7, column=2)

button_4 = Button(window, text=4, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('4'))
button_4.grid(row=6, column=0, pady=(0, 5))

button_5 = Button(window, text=5, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('5'))
button_5.grid(row=6, column=1, pady=(0, 5))

button_6 = Button(window, text=6, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('6'))
button_6.grid(row=6, column=2, pady=(0, 5))

button_7 = Button(window, text=7, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('7'))
button_7.grid(row=5, column=0, padx=5, pady=(0, 5))

button_8 = Button(window, text=8, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('8'))
button_8.grid(row=5, column=1, pady=(0, 5))

button_9 = Button(window, text=9, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: appendCharacter('9'))
button_9.grid(row=5, column=2, padx=5, pady=(0, 5))

multiply_button = Button(window, text="*", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: appendCharacter('*'))
multiply_button.grid(row=5, column=3)

subtract_button = Button(window, text="-", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: appendCharacter('-'))
subtract_button.grid(row=6, column=3)

add_button = Button(window, text="+", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: appendCharacter('+'))
add_button.grid(row=7, column=3)

change_button = Button(window, text="+/-", font=("Arial", 20, "bold"), width=4, height=1, command=changeSign)
change_button.grid(row=8, column=0, pady=5)

dot_button = Button(window, text=".", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: appendCharacter('.'))
dot_button.grid(row=8, column=2)

equal_to_button = Button(window, text="=", font=("Arial", 20, "bold"), width=4, height=1, bg="#00a7ff", command=equals)
equal_to_button.grid(row=8, column=3)

window.mainloop()
