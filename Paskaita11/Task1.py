from tkinter import *

main = Tk()

def say_hello_to_user():
    ivesta = name_input.get()
    output["text"] = f"Labas {ivesta}!"

name = Label(main, text="Iveskite varda")
name_input = Entry(main)
output = Label(main, text="")
mygtukas = Button(main, text="Patvirtinti", command=say_hello_to_user)

name.grid(row = 0, column = 0)
name_input.grid(row = 0, column = 1)
mygtukas.grid(row = 0, column = 2)
output.grid(row = 1, columnspan = 3)

main.mainloop()