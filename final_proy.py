from tkinter import *

def suma():
    valor=int(botonvalor["text"])
    botonvalor["text"]=f"{valor+2}"
def resta():
    valor=int(botonvalor["text"])
    botonvalor["text"]=f"{valor-2}"    
def salir():
    root.destroy()

root = Tk()
root.geometry("500x400")
#rgb0-f red green blue #006

root.title("WELCOME TO BUYING A HOUSE WITH ME")

root.config(bg='#F2B33D')
frame = Frame(root, bg='#F2B33D')

#root.iconbitmap("Masket.ico")

root.rowconfigure(2, minsize=50, weight=1)
root.columnconfigure([0,1,2], minsize=50, weight=1)

botonsuma=Button(root, text="suma 2",bg='turquoise',fg="black",activebackground='turquoise', command=suma) #se le asigna la funcion suma al boton
botonsuma.grid(row=0,column=0, sticky="nsew") #aparece el boton en ese lugar

botonvalor=Label(root, text="0",bg='white')#
botonvalor.grid(row=0, column=1)


botonresta=Button(root, text="resta 2",bg='salmon',fg="ivory3" , command=resta) #se le asigna la funcion resta al boton
botonresta.grid(row=5,column=5, sticky="nsew") #aparece el boton en ese lugar

botonvalor=Label(root, text="0", bg="orange")#
botonvalor.grid(row=0, column=1)

botonsalir=Button(root, text="SALIR",bg='salmon',fg="ivory3", command=salir)
botonsalir.grid(row=4,column=3, sticky="nsew")

#boton1=Button(root, text="START", height=3).pack()



#Button(root, text="start2").pack()
#Label(root, text="WELCOME TO BUYING A HOUSE WITH ME2").pack()

root.mainloop()
