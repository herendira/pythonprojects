"""
# File: discount.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Funcions, discount, dates

"""

from datetime import datetime, timedelta
total=float
tax=float
day=int
give=float

current_date=datetime.now()
day=int(current_date.weekday())


def descuento():
    tax= quantity*0.06 
    descu=(quantity*0.10)
    total=(quantity+tax)-descu
    print("Today we have a 10% extra of your pursache!!")
    print(f"Sales tax amount:$ {tax:.2f}\nDiscount amount: ${descu:.2f}\nTotal: ${total:.2f}")
    

def sin_descuento():
    tax= quantity*0.06
    total=quantity+tax
    print(f"Sales tax amount:$ {tax:.2f}\nTotal:${total:.2f}")

def semi_desc():
    tax= quantity*0.06 
    total=(quantity+tax)
    give=50-total
    print(f"You have to spend ${give:.2f} more, so you can have 10% off of you purchase")
    return give
    

    
    


loop=True
while loop:
 quantity=float(input("What is your total? $ "))
 if quantity>0:
    if quantity>=50:
       if day==1:
          print(day) 
          descuento()
       elif day==2:
          print(day)
          descuento()
       elif day== 0 or 3 or 4 or 5 or 6: 
          print(day)
          sin_descuento() 
    else:
       if day==1 or 2:
         print(day)
         sin_descuento()
         semi_desc()   
        
       else:
           day== 0 or 3 or 4 or 5 or 6 
           print(day)
           sin_descuento()
           
 else:    
    print("Thanks for shopping with us!")
    loop=False



