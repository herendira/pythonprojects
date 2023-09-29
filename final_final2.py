"""
 File: final_final.py
 Author: Herendira Gomez
 Class: CSE111 Programming Building Blocks
 Assignment purpose: Final Proyect

"""
#from tkinter import *
#from tkinter import ttk
#from PIL import Image, ImageTk
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'


loan_cap=float
montant=float

def main():
    try:
       ingresos=float(input("What is your monthly income? $ "))
       gastos=float(input("What is your monthly expenses? $ "))
       casa=float(input("What is the cost of the house you are planing to buy? $ "))
       down=float(input("What is the paydown you are planning to offer? $ "))
    
       years=float(input("Do you want to pay it in 15 or 30 years? "))
    
       tasa=float(input("Whay is the rate are you planning to use? example(3-7) "))
   
          
       loan_capacity=capacity(ingresos, gastos)

       montan=montant_loan(casa, years, tasa,down)
       print()
       print(MAGENTA+"                 Am I ready to buy a house?                    \n"+RESET)
    
       print(CYAN+f"House of: ${casa}")
       print(f"To pay in: {years:.0f} years")
       print(f"Paydown of: ${down}")
       print(f"Rate of: {tasa}\n")
       print(GREEN+f"Your loan capacity is: ${loan_capacity}\n")
       print(f"Your monthly pay aproximation will be: ${round(montan)}\n"+RESET)
       able(loan_capacity,montan)


    except UnboundLocalError as error:
        print(f"Error: {error} please write another rate: 3, 4, 5, 6 or 7, please be sure to read well the questions")

    except ValueError as val_err:
        print(f"Error: {val_err} start overagain and please select another number showed and please be sure to read well the questions ")
     

    except ZeroDivisionError as zero_div_err:
        print(f"Error: {zero_div_err} you are enter a wrong amount, please be sure to read well the questions")   


def capacity(ingresos, gastos):
    loa_cap=((ingresos-gastos)*.4)
   
    return loa_cap
   
   

def montant_loan(casa, years, tasa,down):
    
    if years==30:
        mont_loa=(casa-down)
        
        if tasa==3:
            montant=(((mont_loa*0.3)+mont_loa)/30)/12
        elif tasa==4:
            montant=(((mont_loa*0.4)+mont_loa)/30)/12
        elif tasa==5:
            montant=(((mont_loa*0.5)+mont_loa)/30)/12
        elif tasa==6:
            montant=(((mont_loa*0.6)+mont_loa)/30)/12  
        elif tasa==7:
            montant=(((mont_loa*0.7)+mont_loa)/30)/12
        else:
            print("Invalid number ") 

    if years==15:
        mont_loa=(casa-down)
        if tasa==3:
            montant=(((mont_loa*0.3)+mont_loa)/15)/12
        if tasa==4:
            montant=(((mont_loa*0.4)+mont_loa)/15)/12
        if tasa==5:
            montant=(((mont_loa*0.5)+mont_loa)/15)/12 
        if tasa==6:
            montant=(((mont_loa*0.6)+mont_loa)/15)/12  
        if tasa==7:
            montant=(((mont_loa*0.7)+mont_loa)/15)/12

            
    else:
        print("Invalid number ") 

        
    return montant

def able(loa_cap,montant):

    available=loa_cap-montant
   
    if available>0:
        print(YELLOW+"Congratulation! you are able to obtain a loan to buy the house of your dreams\n"+YELLOW)
    else:
        conseils(available)    
    

    

def conseils(available):
    print(RED+"Sorry, you are not able to have this loan"+RED)
    work_for=(available)*-1
    print()
    print(f"You need: + ${round(work_for)} extra par month to have a loan.\nSome advices:\nHave another job\nA partial job\nStart a saving account\nYou can start study something new\nRemember, is not too late to start work in the house of yours dreams\n"+RESET)
    return work_for


if __name__ == "__main__":
    main()    