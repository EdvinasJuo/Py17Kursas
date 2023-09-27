## TKINTER
import webbrowser
## YRA DAR - PyQt5

from tkinter import *
#
# langas = Tk()
# langas.geometry("500x700")  # Nurodom lango pradini dydi
# uzrasas = Label(langas, text="Tiesiog tekstas")
#
# uzrasas.pack()  ## ATVAIZDAVIMAS SU .pack()
# langas.mainloop()  ## SUKASI BEGALINIS CIKLAS KOL IJUNGTA PROGRAMA


# langas = Tk()
#
# langas.geometry("500x700")
#
# virsutinis = Frame(langas)  ## PADARO DU LANGUS
# apatinis = Frame(langas)    ## PADARO DU LANGUS
#
# mygtukas1 = Button(virsutinis, text="Pirmas mygtukas")
# mygtukas2 = Button(virsutinis, text="Antras mygtukas")
# mygtukas3 = Button(virsutinis, text="Trecias mygtukas")
# mygtukas4 = Button(apatinis, text="Ketvirtas mygtukas")
#
# virsutinis.pack()
# apatinis.pack(side = BOTTOM)  #ATVAIZDUOTAS APACIOJ
# mygtukas1.pack(side = LEFT)
# mygtukas2.pack(side = LEFT)
# mygtukas3.pack(side = LEFT)
# mygtukas4.pack()
#
# langas.mainloop()

# ************-------------------------------------------------------------
# langas = Tk()
#
# # langas.geometry("500x700")
#
# uzrasas1 = Label(langas, text="Vardas")
# label1 = Entry(langas)
#
# uzrasas2 = Label(langas, text="Pavarde")
# label2 = Entry(langas)
# varnele = Checkbutton(langas, text="Pazymekite varnele")
#
# uzrasas1.grid(row = 0, column = 0, sticky = E)  # KITAS ATVAIZDAVIMO BUDAS, STICKY NURODOMAS SU W,E,S,N. Pasaulio kryptim
# label1.grid(row = 0, column = 1)
# uzrasas2.grid(row = 1, column = 0, sticky = E)
# label2.grid(row = 1, column = 1)
# varnele.grid(row = 3, columnspan = 2)   # ISPLECIA PER DU STULPELIUS.
#
# langas.mainloop()


# ---------------------------------------------------

# langas = Tk()
# langas.geometry("400x500")
#
# def spausdinti(event):
#     print("Paspaustas kairys peles mygtukas!")
#
# def spausdinti2(event):
#     print("Paspaustas desinys peles mygtukas!")
#
# def spausdinti3(event):
#     print("Paspaustas klavisas 'ENTER' !")
#
# mygtukas = Button(langas, text="Spausdinti")
# mygtukas.pack()
#
# mygtukas.bind("<Button-1>", spausdinti)   # <Button-1> Nurodomos eventas. (KODAS)
# mygtukas.bind("<Button-3>", spausdinti2)
# langas.bind("<Return>", spausdinti3)
#
# langas.mainloop()



# ---------------------------------------------------

# langas = Tk()
# # langas.geometry("400x500")
# def spausdina():
#     ivesta = laukas.get()
#     output["text"] = ivesta
#
#
# uzrasas = Label(langas, text="Iveskite zodi")
# laukas = Entry(langas)
# output = Label(langas, text="")
# mygtukas = Button(langas, text="Ivesti", command=spausdina)
#
# uzrasas.grid(row=0, column = 0)
# laukas.grid(row=0, column = 1)
# mygtukas.grid(row = 1, columnspan = 2)
# output.grid(row = 2, columnspan = 2)
#
# langas.mainloop()


# ---------------------------- SCROLLBAR

# langas = Tk()
#
# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]  ## GAUNA PAZYMETA SKAICIU IS LISTBOXO
#     labelis1["text"] = pasirinkta
#
# scrollbaras = Scrollbar(langas)
# boksas = Listbox(langas, yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=boksas.yview)
# sarasas = range(1, 201)
# boksas.insert(END, *sarasas)
# mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
# labelis1 = Label(langas, text="")
#
#
#
# boksas.pack(side = LEFT)
# mygtukas.pack()
# labelis1.pack()
# scrollbaras.pack(side = RIGHT, fill = Y)
#
# langas.mainloop()


#------------------------------------ MENU LANGAS---------------------------
# langas = Tk()
#
# def pirmas():
#     print("Pirmas")
#
# meniu = Menu(langas)
# langas.config(menu = meniu)
# submeniu = Menu(meniu, tearoff=0)
# submeniu2 = Menu(meniu, tearoff=0)
# submeniu3 = Menu(meniu, tearoff=0)
#
# meniu.add_cascade(label="Meniu", menu= submeniu)
# submeniu.add_command(label="Pirmas", command=pirmas)
# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trecias")
#
# meniu.add_cascade(label="Meniu2", menu= submeniu2)
# submeniu2.add_command(label="1", command=pirmas)
# submeniu2.add_command(label="2")
#
# meniu.add_cascade(label="Meniu3", menu= submeniu3)
# submeniu3.add_command(label="Naujas", command=pirmas)
#
#
# langas.mainloop()


#---------------------- STATUS JUOSTA

langas = Tk()

def daro():
    status["text"] = "Dabar kazka daro..."

status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
mygtukas = Button(langas, text="Kazka daro", command=daro)
entris = Entry(langas)

status.grid(row=1, columnspan = 2, sticky = W+E)
mygtukas.grid(row = 0, column = 0)
entris.grid(row = 0, column = 1)

langas.mainloop()


#---------------------- URL ATIDARYMAS
# langas = Tk()
#
# def callBack(url):
#     webbrowser.open_new(url)
#
# link1 = Label(langas, text="Google", fg="blue", cursor="hand2")
# link2 = Label(langas, text="Delfi", fg="blue", cursor="hand2")
#
# link1.bind("<Button-1>", lambda e: callBack("www.google.lt"))
# link2.bind("<Button-1>", lambda e: callBack("www.delfi.lt"))
# link1.pack()
# link2.pack()
#
# langas.mainloop()


#--------------NUOTRAUKU ATIDARYMAS
#
# langas = Tk()
# from PIL import ImageTk, Image
# img = ImageTk.PhotoImage(Image.open("images.jpg"))
#
# panel = Label(langas, image=img)
#
# panel.pack(fill="both", expand = "yes")
# langas.mainloop()


#---------------KINTAMUJU NAUDOJIMAS
# langas = Tk()
#
# kintamasis = IntVar()
#
# def keisti():
#     kintamasis.set(15)
#
# def spausdinti():
#     print(kintamasis.get())
#
# mygtukas_k = Button(langas, text="keisti", command=keisti)
# mygtukas_s = Button(langas, text= "spausdinti", command=spausdinti)
#
# mygtukas_k.pack()
# mygtukas_s.pack()
#
# langas.mainloop()



#------------------ KELIU LANGU ATIDARYMAS
# langas = Tk()
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Frame(self.master)
#         self.button = Button(self.frame, text="New window", width=25, command=self.new_window)
#         self.button.pack()
#         self.frame.pack()
#
#
#     def new_window(self):
#         self.window = Toplevel(self.master)
#         self.window2 = Demo2(self.window)
#
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Frame(self.master)
#         self.button = Button(self.frame, text="Quit", width=25, command=self.close_window)
#         self.button.pack()
#         self.frame.pack()
#
#     def close_window(self):
#         self.master.destroy()
#
#
# Demo1(langas)
#
# langas.mainloop()