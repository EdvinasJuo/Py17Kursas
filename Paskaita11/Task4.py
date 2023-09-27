# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:
# • Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# • Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# • Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų
# programos langą

from tkinter import *

main = Tk()
last_text = StringVar()
status_bar = Label(main, textvariable=last_text, bd=1, relief=SUNKEN, anchor=W)

def say_hello_to_user(event=None):
    ivesta = name_input.get()
    output["text"] = f"Labas {ivesta}!"
    last_text.set(output["text"])
    global last_input
    last_input = ivesta
    last_text.set("Sukurta")

def isvalyti():
    name_input.delete(0, END)
    output["text"] = ""
    last_text.set("")
    last_text.set("Išvalyta")

def atkurti():
    output["text"] = f"Labas {last_input}!"
    last_text.set("Atkurta")

def iseiti():
    main.destroy()


meniu = Menu(main)
main.config(menu = meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu= submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)


name = Label(main, text="Iveskite varda")
name_input = Entry(main)
output = Label(main, text="")
mygtukas = Button(main, text="Patvirtinti", command=say_hello_to_user)


name.grid(row = 0, column = 0)
name_input.grid(row = 0, column = 1)
mygtukas.grid(row = 0, column = 2)
output.grid(row = 1, columnspan = 3)
status_bar.grid(row=2, columnspan=3, sticky=W+E)

main.bind("<Return>", say_hello_to_user)

main.mainloop()