from tkinter import *

window = Tk()
window.geometry("340x440")
window.resizable(False, False)
window.title("Kalkulator")
icon = PhotoImage(file="calc_img.png")
window.iconphoto(True, icon)

eq_field = Label(window,
                font=("Arial",12,"bold"),
                text="",
                justify="right",
                foreground="gray")
eq_field.grid(row=0, column=0,columnspan=4,pady=1, padx=4, sticky="e")

entry_field = Entry(window, 
                        font=("Arial",24,"bold"),
                        justify="right",
                        width=18,
                        borderwidth=0,
                        bg="lightgray")
entry_field.grid(row=1, column=0, columnspan=7, padx=7, pady=(0,8))

def enter(key_enter):
    expression = entry_field.get()
    entry_field.delete(0,END)
    eq_field.config(text=expression)
    
entry_field.bind('<Return>',enter)

backspace_button = Button(window, text="⌫", font=("Arial", 20, "bold"), width=4, height=1)
backspace_button.grid(row=2, column=3)

clear_button = Button(window, text="C", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff0000")
clear_button.grid(row=2, column=2)

clear_entry_button = Button(window, text="CE", font=("Arial", 20, "bold"), width=4, height=1, bg="#ff8585")
clear_entry_button.grid(row=2, column=1)

percentage_button = Button(window, text="%", font=("Arial", 20, "bold"), width=4, height=1)
percentage_button.grid(row=2, column=0)

factiorial_button = Button(window, text="x!", font=("Arial", 20, "bold"), width=4, height=1)
factiorial_button.grid(row=3, column=0, pady=5)

pow_to_button = Button(window, text="xⁿ", font=("Arial", 20, "bold"), width=4, height=1)
pow_to_button.grid(row=3, column=1)

sqrt_by_button = Button(window, text="ⁿ√x", font=("Arial", 20, "bold"), width=4, height=1)
sqrt_by_button.grid(row=3, column=2)

divide_button = Button(window, text="/", font=("Arial", 20, "bold"), width=4, height=1)
divide_button.grid(row=3, column=3)

button_7 = Button(window, text=7, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_7.grid(row=4, column=0, padx=5)

button_8 = Button(window, text=8, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_8.grid(row=4, column=1)

button_9 = Button(window, text=9, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_9.grid(row=4, column=2,padx=5)

multiply_button = Button(window, text="*", font=("Arial", 20, "bold"), width=4, height=1)
multiply_button.grid(row=4, column=3)

button_4 = Button(window, text=4, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_4.grid(row=5, column=0, pady=5)

button_5 = Button(window, text=5, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_5.grid(row=5, column=1)

button_6 = Button(window, text=6, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_6.grid(row=5, column=2)

subtract_button = Button(window, text="-", font=("Arial", 20, "bold"), width=4, height=1)
subtract_button.grid(row=5, column=3)

button_1 = Button(window, text=1, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_1.grid(row=6, column=0)

button_2 = Button(window, text=2, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_2.grid(row=6, column=1)

button_3 = Button(window, text=3, font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_3.grid(row=6, column=2)

add_button = Button(window, text="+", font=("Arial", 20, "bold"), width=4, height=1)
add_button.grid(row=6, column=3)

change_button = Button(window, text="+/-", font=("Arial", 20, "bold"), width=4, height=1)
change_button.grid(row=7, column=0, pady=5)

button_0 = Button(window, text="0", font=("Arial", 20, "bold"), width=4, height=1, bg="gray")
button_0.grid(row=7, column=1)

dot_button = Button(window, text=".", font=("Arial", 20, "bold"), width=4, height=1)
dot_button.grid(row=7, column=2)

equal_to_button = Button(window, text="=", font=("Arial", 20, "bold"), width=4, height=1, bg="#00a7ff")
equal_to_button.grid(row=7, column=3)

window.mainloop()