"""
 File: final_final.py
 Author: Herendira Gomez
 Class: CSE111 Programming Building Blocks
 Assignment purpose: Final Proyect

"""
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



def main():

    pass

def capacity(income, expenses):
    value=float(income.get())
    value2=float(expenses.get())

   
    return result.set((value-value2)*0.4)
   

def montant_loan(a,b):
    pass

def able(a,c):
    pass

def conseils():
    pass

def salir():
    root.destroy()

#configuration of my Window
root = Tk()
root.geometry("800x800")
#root.rowconfigure(10, minsize=50, weight=1)
#root.columnconfigure([0,1], minsize=50, weight=1)

#title of my window
root.title("BUYING A HOUSE AM I READY?")
root.iconbitmap("casa.ico")
#color of my window
root.config(bg='#F2B33D')
frame = Frame(root, bg='#F2B33D')


#configuration of exit botton
botonsalir=Button(root, text="EXIT",bg='salmon',fg="black", activebackground='salmon', command=salir)
botonsalir.grid(row=0,column=8,padx=5, pady=5)

img=Image.open("casa.jpg")
img=img.resize((200,200), Image.LANCZOS)
img=ImageTk.PhotoImage(img)
img_label=Label(root, image=img)

#img_label.image=img

    
img_label.grid(row=0, column=0, columnspan=2, rowspan=1 ,pady=5, padx=5)
#variables entry
income=StringVar()
expenses=StringVar()
result=StringVar()
years=StringVar()
rate=StringVar()

#income entry
incomes_entry= Entry(root, width=15, textvariable=income)
incomes_entry.grid(row=4, column=1, pady=5, padx=5)
Label(root, text="Incomes: $").grid(row=4, column=0, padx=5, pady=5)
#Label(root, text="Result").grid(row=112, column=3, sticky=E)

expense_entry= Entry(root, width=15, textvariable=expenses)
expense_entry.grid(row=5, column=1,padx=5, pady=5)

Label(root, text="Expenses: $").grid(row=5, column=0,padx=5, pady=5)
#Label(root, text="Result").grid(row=10, column=3, sticky=E)

Label(root, width=12, textvariable=result).grid(row=6, column=1,padx=5, pady=5)
Label(root, text="Result: $").grid(row=6, column=0)

boton_cal=Button(root, text="Calculate",width=10,font="System", height=10,bg='olive drab',fg="light yellow", activebackground='goldenrod',command=lambda:capacity(income, expenses))
boton_cal.grid(row=0, column=4,padx=5, pady=5)





root.mainloop()


if __name__ == "__main__":
    main()
