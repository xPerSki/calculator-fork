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


def append_character(character: str):
    old = str(entry_field.cget("text"))
    if old and old[-1] in "+-/*^" and character in "+-/*^":
        entry_field.config(text=old[:-1] + character)
    else:
        entry_field.config(text=old + character)


def clear_entry_label():
    entry_field.config(text=eval(eq_field.cget("text")[:-1]))


def clear_all():
    entry_field.config(text="")
    eq_field.config(text="")


def memory_read():
    old = entry_field.cget("text")
    entry_field.config(text=old + str(MR)) if MR else None


def memory_add(minus=False):
    global MR
    number = str(entry_field.cget("text"))
    if minus:
        number = '-' + number

    MR += float(number) if '.' in number else int(number)
    entry_field.config(text="")


def memory_clear():
    global MR
    MR = 0


def backspace():
    old = entry_field.cget("text")
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


def change_sign():
    value = str(entry_field.cget("text"))
    if '-' in value:
        entry_field.config(text=value[1:])
    else:
        entry_field.config(text='-' + value)


def equals():
    to_calculate = entry_field.cget("text")
    eq_field.config(text=to_calculate+"=")
    result = eval(to_calculate)
    if int(result) == result:
        result = int(result)
    entry_field.config(text=result)


MC_button = Button(window, text="MC", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memory_clear)
MC_button.grid(row=2, column=0, pady=(0, 4))

MR_button = Button(window, text="MR", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memory_read)
MR_button.grid(row=2, column=1, pady=(0, 4))

Mplus_button = Button(window, text="M+", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=memory_add)
Mplus_button.grid(row=2, column=2, pady=(0, 4))

Mminus_button = Button(window, text="M-", font=("Arial", 9, "bold"), width=8, bg="black", foreground="white", command=lambda: memory_add(minus=True))
Mminus_button.grid(row=2, column=3, pady=(0, 4))

backspace_button = Button(window, text="⌫", font=("Arial", 20, "bold"), width=4, height=1, command=backspace)
backspace_button.grid(row=3, column=3)

clear_button = Button(window, text="C", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff0000", command=clear_all)
clear_button.grid(row=3, column=2)

clear_entry_button = Button(window, text="CE", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff8585", command=clear_entry_label)
clear_entry_button.grid(row=3, column=1)

percentage_button = Button(window, text="%", font=("Arial", 20, "bold"), width=4, height=1, command=percent)
percentage_button.grid(row=3, column=0)

factiorial_button = Button(window, text="x!", font=("Arial", 20, "bold"), width=4, height=1, command=factorial)
factiorial_button.grid(row=4, column=0, pady=5)

pow_to_button = Button(window, text="xⁿ", font=("Arial", 20, "bold"), width=4, height=1)
pow_to_button.grid(row=4, column=1)

sqrt_by_button = Button(window, text="ⁿ√x", font=("Arial", 20, "bold"), width=4, height=1)
sqrt_by_button.grid(row=4, column=2)

divide_button = Button(window, text="/", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: append_character('/'))
divide_button.grid(row=4, column=3)

button_0 = Button(window, text="0", font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('0'))
button_0.grid(row=8, column=1)

button_1 = Button(window, text=1, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('1'))
button_1.grid(row=7, column=0)

button_2 = Button(window, text=2, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('2'))
button_2.grid(row=7, column=1)

button_3 = Button(window, text=3, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('3'))
button_3.grid(row=7, column=2)

button_4 = Button(window, text=4, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('4'))
button_4.grid(row=6, column=0, pady=(0, 5))

button_5 = Button(window, text=5, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('5'))
button_5.grid(row=6, column=1, pady=(0, 5))

button_6 = Button(window, text=6, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('6'))
button_6.grid(row=6, column=2, pady=(0, 5))

button_7 = Button(window, text=7, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('7'))
button_7.grid(row=5, column=0, padx=5, pady=(0, 5))

button_8 = Button(window, text=8, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('8'))
button_8.grid(row=5, column=1, pady=(0, 5))

button_9 = Button(window, text=9, font=("Arial", 20, "bold"), width=4, height=1, bg="gray", command=lambda: append_character('9'))
button_9.grid(row=5, column=2, padx=5, pady=(0, 5))

multiply_button = Button(window, text="*", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: append_character('*'))
multiply_button.grid(row=5, column=3)

subtract_button = Button(window, text="-", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: append_character('-'))
subtract_button.grid(row=6, column=3)

add_button = Button(window, text="+", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: append_character('+'))
add_button.grid(row=7, column=3)

change_button = Button(window, text="+/-", font=("Arial", 20, "bold"), width=4, height=1, command=change_sign)
change_button.grid(row=8, column=0, pady=5)

dot_button = Button(window, text=".", font=("Arial", 20, "bold"), width=4, height=1, command=lambda: append_character('.'))
dot_button.grid(row=8, column=2)

equal_to_button = Button(window, text="=", font=("Arial", 20, "bold"), width=4, height=1, bg="#00a7ff", command=equals)
equal_to_button.grid(row=8, column=3)

window.mainloop()
