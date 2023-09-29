"""
# File: tire_volume.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Program that reads from the keyboard 
# the three numbers for a tire and computes and outputs
#  the volume of space inside that tire.

"""
import math
from datetime import datetime
phone_number=str
#Asking part
name=input("Client Name: ")
width=float(input("Enter the width of the tire in mm (ex 205): "))
radio=float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter=float(input("Enter the diameter of the wheel in inches (ex 15):"))
current_date=datetime.now()

#compute part
volume=(math.pi*(width**2)*radio*((width*radio)+(2540*diameter)))/10000000000
print(f"The approximate volume is {volume:.2f} liters")

#Exceeding the Requirements part
op=input("Are you interested in buying a set of new tires? yes/not ")
if op.lower()=="yes":
    phone_number=input("Phone Number: ")
    if width==205 and radio==60 and diameter==15:
        print("The price is: $357.99 per tire without tax")
    elif width==165 and radio==65 and diameter==14:
         print("The price is: $216.37 per tire without tax")
    elif width==175 and radio==65 and diameter==14:
         print("The price is: $305.98 per tire without tax")
    elif width==185 and radio==60 and diameter==14:
         print("The price is: $325.79 per tire without tax")           
    else:
        print("We dont have that size in our stock, we apologize.")
else:
     op.lower()=="not"  
     phone_number=input("Phone Number: ")
     print("Thanks for your visit")     

#Open and appending info to a file. I save the information more readable to the user.
with open("volumes.txt", "at") as volume_file:
    print(f"\nDate:{current_date:%Y-%m-%d}\nClient Name: {name}\nPhone Number: {phone_number}\nTire width: {width:.2f}\nTire diameter: {diameter:.2f}\nTire Ratio: {radio:.2f}\nThe Volume in liters is: {volume:.2f}", file=volume_file)
