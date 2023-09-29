from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Frame, Label, Button
from tkinter.font import Font


def main():

   root = Tk()
   root.geometry("900x1000")
   #root.rowconfigure(10, minsize=50, weight=1)
   #root.columnconfigure([0,1], minsize=50, weight=1)

   #title of my window
   root.title("BUYING A HOUSE AM I READY?")
   root.iconbitmap("casa.ico")
   #color of my window
   root.config(bg='#F2B33D', padx=10, pady=10)
   #frame = Frame(root, bg='#F2B33D', padx=20, pady=10)
   
   img=Image.open("casa.jpg")
   img=img.resize((200,200), Image.LANCZOS)
   img=ImageTk.PhotoImage(img)
   img_label=Label(root, image=img)

    #img_label.image=img

   #lbl_adv=Label(root,)
   img_label.grid(row=0, column=0, columnspan=2, rowspan=1 ,pady=5, padx=5)
   everything(root)
   root.mainloop()


def everything(root):
  
   
   
    #variables entry(function "capacity")
    income=StringVar()
    expenses=StringVar()
    result=StringVar()
    #variables entry(function "montant_loan")
    casa=StringVar()
    down=StringVar()
    years=StringVar()
    rate=StringVar()
    montant_result=StringVar()
    available=StringVar()
    work_for1=StringVar()

    #fonts
   

    #income entry(function "capacity")
    incomes_entry= Entry(root, width=15,justify="center",font=("Verdana",11),bg='#F2B00D', textvariable=income)
    incomes_entry.grid(row=4, column=1, pady=5, padx=5)
    #income Label(function "capacity")
    Label(root, text="Monthly incomes: $",font=("Verdana",15),bg='#F2B33D').grid(row=4, column=0, padx=5, pady=5)
    

    expense_entry= Entry(root, width=15,justify="center",font=("Verdana",11),bg='#F2B00D', textvariable=expenses)
    expense_entry.grid(row=5, column=1,padx=5, pady=5)

    Label(root, text="Monthly expenses: $",font=("Verdana",15),bg='#F2B33D').grid(row=5, column=0,padx=5, pady=5)
   

   
    

    #function montant_loan entries and labels
    #entry casa
    casa_entry= Entry(root,width=15,justify="center",font=("Verdana",11),bg='#F2B00D',fg="darkblue", textvariable=casa)
    casa_entry.grid(row=6, column=1, pady=5, padx=5)
    Label(root, text="House value: $",font=("Verdana",15),bg='#F2B33D').grid(row=6, column=0, padx=5, pady=5)

    
    #entry down payment
    down_entry= Entry(root, width=15,justify="center",font=("Verdana",11),bg='#F2B00D', textvariable=down)
    down_entry.grid(row=7, column=1, pady=5, padx=5)
    Label(root, text="Down payment: $",font=("Verdana",15),bg='#F2B33D').grid(row=7, column=0, padx=5, pady=5) 
    #entry years
    years_entry= Entry(root, width=15, justify="center",font=("Verdana",11),bg='#F2B00D', textvariable=years)
    years_entry.grid(row=8, column=1, pady=5, padx=5)
    Label(root, text="Years, 15 or 30: ",font=("Verdana",15),bg='#F2B33D').grid(row=8, column=0, padx=5, pady=5) 
    #entry rate
    rate_entry= Entry(root, width=15, justify="center",font=("Verdana",11),bg='#F2B00D', textvariable=rate)
    rate_entry.grid(row=9, column=1, pady=5, padx=5)
    Label(root, text="%Rate (3-7): ",font=("Verdana",15),bg='#F2B33D').grid(row=9, column=0, padx=5, pady=5)

    

    Label(root, width=12, textvariable=result,font=("Verdana",15),bg='#F2B33D').grid(row=10, column=1,padx=5, pady=5)
    Label(root, text="Borrowing capacity: $",font=("Verdana",15),bg='#F2B33D').grid(row=10, column=0)
    #botton calculate(function "capacity")
    boton_cal=Button(root, text="Calculate\nborrow\ncapacity",width=10,font="Verdana", height=10,bg='olive drab',fg="light yellow", activebackground='goldenrod',command=lambda:capacity(income, expenses))
    boton_cal.grid(row=0, column=4,padx=5, pady=5)

    Label(root, width=12, textvariable=montant_result,font=("Verdana",15),bg='#F2B33D').grid(row=11, column=1,padx=5, pady=5)
    Label(root, text="Loan montly payment: $",font=("Verdana",15),bg='#F2B33D').grid(row=11, column=0)

    #botton calculate(function "capacity")
    boton_cal_month=Button(root, text="Calculate\nyour montly\npayment",width=10,font="Verdana", height=10,bg='olive drab',fg="light yellow", activebackground='goldenrod',command=lambda:montant_loan(casa, years, rate, down))
    boton_cal_month.grid(row=0, column=5,padx=5, pady=5)

    #Label Work for
    lbl_work=Label(root,width=12,font=("Verdana",15),bg='#F2B33D', textvariable=work_for1)
    lbl_work.grid(row=12, column=1, padx=5, pady=5)
    lbl_extra=Label(root, text="You need this quantity\n extra par month: ",font=("Verdana",15),bg='#F2B33D')
    lbl_extra.grid(row=12, column=0)

    #label Advices
    lbl_adv=Label(root,justify="center",font=("Verdana",16),bg='#F2B33D', textvariable=available)
    lbl_adv.grid(row=17, column=1,columnspan=7, rowspan=5, padx=5, pady=5)
    
    lbl_ava=Label(root,justify="center", text="Am I available?: ",font=("Verdana",16,"bold"),bg='#F2B33D')
    lbl_ava.grid(row=16, column=0, pady=30)
   
    #botton calculate(function "capacity")
    boton_cal_able=Button(root, text="Am I\navailable?",width=10,font="Verdana", height=10,bg='olive drab',fg="light yellow", activebackground='goldenrod',command=lambda:able(result,montant_result,))
    boton_cal_able.grid(row=0, column=6,padx=5, pady=5)

    botonclear=Button(root, text="CLEAR",font="Verdana", bg='Beige',fg="black", activebackground='salmon', command=lambda: clear(incomes_entry,expense_entry,casa_entry,down_entry,years_entry,rate_entry,available, work_for1,montant_result, result))
    botonclear.grid(row=11,column=5,padx=5, pady=5)

     #configuration of exit botton
    botonsalir=Button(root, text="EXIT",bg='salmon',fg="black",font="Verdana", activebackground='salmon', command=lambda: salir(root))
    botonsalir.grid(row=11,column=6,padx=5, pady=5)


    def capacity(income, expenses):
        result1=0
        value=float(income.get())
        value2=float(expenses.get())

   
        result1=(value-value2)*0.4
        return result.set(result1)
   

    def montant_loan(casa, years, tasa, down):
        montant=0
        mont_loa=0
        casa2=float(casa.get())
        years2=float(years.get())
        tasa2=float(tasa.get())
        down2=float(down.get())

        if years2==30:
           mont_loa=(casa2-down2)
           
           if tasa2==3:
            montant=(((mont_loa*0.3)+mont_loa)/30)/12
           elif tasa2==4:
            montant=(((mont_loa*0.4)+mont_loa)/30)/12
           elif tasa2==5:
            montant=(((mont_loa*0.5)+mont_loa)/30)/12
           elif tasa2==6:
            montant=(((mont_loa*0.6)+mont_loa)/30)/12  
           elif tasa2==7:
            montant=(((mont_loa*0.7)+mont_loa)/30)/12
        #else:
            #print("Invalid number ") 

        if years2==15:
           mont_loa=(casa2-down2)
           if tasa2==3:
            montant=(((mont_loa*0.3)+mont_loa)/15)/12
           if tasa2==4:
            montant=(((mont_loa*0.4)+mont_loa)/15)/12
           if tasa2==5:
            montant=(((mont_loa*0.5)+mont_loa)/15)/12 
           if tasa2==6:
            montant=(((mont_loa*0.6)+mont_loa)/15)/12  
           if tasa2==7:
            montant=(((mont_loa*0.7)+mont_loa)/15)/12

            
        #else:
         #print("Invalid number ") 

        
        return montant_result.set(round(montant))

    def able(result,montant_result):
        available1=0
        loa_cap2=float(result.get())
        montant2=float(montant_result.get())

        available1=loa_cap2-montant2
   
        if available1>0:
           
          
           message="""Congratulation! \nyou are able to obtain\n a loan to buy\n the house of your dreams"""
           available.set(message)
        else:
          
           #print("Sorry, you are not able to have this loan")
           work_for=(available1)*-1
           message2="""Sorry, you are not able to have this loan.\nSome advices:\nHave another job.\nA partial job.\n Start a saving account.\n You can start study something new.\nRemember,\nis not too late to start working\n in the house of yours dreams"""
           available.set(message2)
           work_for1.set(work_for)
       

     
 


def clear(incomes_entry,expense_entry,casa_entry,down_entry,years_entry,rate_entry, available, work_for1,montant_result, result):
   
    incomes_entry.delete(0, END)
    
    expense_entry.delete(0, END)
    casa_entry.delete(0, END)
    down_entry.delete(0, END)
    years_entry.delete(0, END)
    rate_entry.delete(0, END)
    
    montant_result.set("")
    available.set("")
    work_for1.set("") 
    result.set("")


def salir(root):
    root.destroy()  










if __name__ == "__main__":
    main()
