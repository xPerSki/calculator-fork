from tkinter import *

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
                 foreground="gray",
                 anchor="e",
                 width=32)
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
    if entry_field.cget("text") == "ERR":
        if character not in "+-/*.":
            entry_field.config(text=character)
        else:
            pass
        return
    
    old = str(entry_field.cget("text"))
    if old == "" and character in "+-/*.":
        pass
    else:
        if old and old[-1] == "(" and character == "-":
            entry_field.config(text=old + character)
        elif old and old[-1] == "(" and character in "+/*.":
            pass
            
        else:
            if old and old[-1] in "*/" and character == "-":
                    entry_field.config(text=old + character)
            elif old and old[-1] in "+/*." and character in "+-/*.":
                entry_field.config(text=old[:-1] + character)

            else:
                if old and old[-1] == "-" and character == "-":
                    pass
                elif old and old[-1] == "-" and old[-2] in "*/(" and character in "+-*/.":
                    pass
                elif old and old[-1] == "-" and character in "+-*/.":
                    entry_field.config(text=old[:-1] + character)
                else:
                    entry_field.config(text=old + character)


def clearEntryLabel():
    if eq_field.cget("text"):
        entry_field.config(text=eval(eq_field.cget("text")[:-1]))
    else:
        entry_field.config(text='')


def clearAll():
    entry_field.config(text="")
    eq_field.config(text="")


def memoryRead():
    old = str(entry_field.cget("text"))
    if len(old) > 0:
        sign = '+' if MR > 0 else ''
    else:
        sign = ''
    entry_field.config(text=old + sign + str(MR)) if MR else None


def memoryAdd(minus=False):
    global MR
    if entry_field.cget("text"):
        number = str(entry_field.cget("text"))
        if minus:
            number = '-' + number

        MR += float(number) if '.' in number else int(number)
        entry_field.config(text="")
    else:
        pass


def memoryClear():
    global MR
    MR = 0


def backspace():
    if entry_field.cget("text") == "ERR":
        pass
        return
    
    old = entry_field.cget("text")
    if len(str(old)) > 0:
        if old[-1] == "(":
            entry_field.config(text=old[1:-4])
        else:
            entry_field.config(text=old[:-1])
    else:
        pass


def percent():
    old = str(entry_field.cget("text"))
    try:
        if len(old) > 2 and old[-1] in "+-/*." and old[-2] in "+-/*.":
            old = old[:-2]
            
        elif old and old[-1] in "+-/*.":
                    old = old[:-1]

        val = float(old) / 100
        if int(val) == float(val):
            val = int(val)
        entry_field.config(text=str(val))
        eq_field.config(text=old+"/100"+"=")
    except Exception:
        pass


def factorial():
    result = 1
    n = str(entry_field.cget("text"))
    try:
        if len(n) > 2 and n[-1] in "+-/*." and n[-2] in "+-/*.":
            n = n[:-2]
        elif n and n[-1] in "+-/*.":
            n = n[:-1]
        elif n and n[0] == "-":
            raise ValueError

        for i in range(2, int(n)+1):
            result *= i
            eq_field.config(text=str(n)+"!=")
            entry_field.config(text=result)
            
    except Exception:
        entry_field.config(text="ERR")


def changeSign():
    if entry_field.cget("text") == "ERR":
        pass
        return
    
    value = str(entry_field.cget("text"))
    if len(value) > 0:
        if '-' in value:
            entry_field.config(text=value[1:])
        else:
            entry_field.config(text='-' + value)
    else:
        pass


def toThePowerOf():
    if entry_field.cget("text") == "ERR":
        pass
        return
    
    base = entry_field.cget("text")
    if base:
        if (base[-1] in "*-" and base[-2] in "*(") or base[-1] == "(":
            pass
        elif base[-1] in "+-/*." and base[-2] in "+-/*.":
            entry_field.config(text=base[:-2] + "**")
        elif base[-1] in "+-/*." and base != "":
            entry_field.config(text=base[:-1] + "**")
        else:
            entry_field.config(text=base + "**")
    else:
        pass


def rootToThePowerOf():
    if entry_field.cget("text") == "ERR":
        pass
        return
    
    base_of_root = str(entry_field.cget("text"))
    if base_of_root:
        if base_of_root[-1] in "+-/*." and base_of_root != "":
            entry_field.config(text=f"({base_of_root[:-1]})**(")
        else:
            entry_field.config(text=f"({base_of_root})**(")
    else:
        pass


def equals():
    if entry_field.cget("text") == "ERR":
        entry_field.config(text="")
        return

    to_calculate = str(entry_field.cget("text"))
    if to_calculate:
        if to_calculate[-1] == "*" and to_calculate[-2] == "*":
            to_calculate = to_calculate[:-2]
            result = eval(to_calculate)
            eq_field.config(text=to_calculate+"=")

        elif to_calculate[-1] in "+-/*.":
            if "(" in to_calculate:
                to_calculate += ")"
                to_calculate = to_calculate[:-2]+to_calculate[-1]
                result = eval(to_calculate)
                eq_field.config(text=to_calculate+"=")
            
            else:
                result = eval(to_calculate[:-1])
                eq_field.config(text=to_calculate[:-1]+"=")

        else:   
            try:
                if "(" in to_calculate:
                    to_calculate += ")"
                    result = eval(to_calculate)
                    eq_field.config(text=to_calculate+"=")
                
                else:
                    result = eval(to_calculate)
                    eq_field.config(text=to_calculate+"=")

            except Exception:
                entry_field.config(text="ERR")

        try:
            if int(result) == float(result):
                result = int(result)
            entry_field.config(text=result)

        except Exception:
            entry_field.config(text="ERR")
    else:
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
