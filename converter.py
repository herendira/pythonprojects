from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def calcular():
    try: 
       value=float(feet.get())
       meters.set((0.3048*value*10000+0.5)/10000)
    except ValueError:
          meters.set("ERROR")   
   

ventana= Tk()
ventana.title("convertidor")
ventana.resizable(False, False)

mainframe=ttk.Frame(ventana, padding="10 5 10 5")
mainframe.grid(row=0, column=0)

feet=StringVar()
meters=StringVar()

feet_entry=Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(row=0,column=2)

Label(mainframe, text="feet").grid(row=0,column=3, sticky=W)
Label(mainframe, text="Es equivalente a: ").grid(row=1,column=1, sticky=E)
Label(mainframe, textvariable=meters).grid(row=1,column=2, sticky=W)
Label(mainframe, text="metros").grid(row=1,column=3, sticky=W)

Button(mainframe, text="Calculate", command=calcular).grid(row=2, column=3, sticky=W)



ventana.mainloop()