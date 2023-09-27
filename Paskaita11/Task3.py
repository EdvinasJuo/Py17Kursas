# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
# • Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje,
# kurioje spausdinamas pasisveikinimo tekstas
# • Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto
# eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# • Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# • Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

from tkinter import *

main = Tk()
last_text = StringVar()

def say_hello_to_user(event=None):
    ivesta = name_input.get()
    output["text"] = f"Labas {ivesta}!"
    last_text.set(output["text"])
    global last_input
    last_input = ivesta

def isvalyti():
    name_input.delete(0, END)
    output["text"] = ""
    last_text.set("")
def atkurti():
    output["text"] = f"Labas {last_input}!"

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
main.bind("<Return>", say_hello_to_user)

main.mainloop()