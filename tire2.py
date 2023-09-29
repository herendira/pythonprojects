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

current_date=datetime.now()

print(f"{current_date:%Y-%m-%d}")

width=float(input("What is the with of the tire? "))
radio=float(input("What is the ratio? "))
diameter=float(input("What is the diameter? "))
        
volume=(math.pi*(width**2)*radio*((width*radio)+(2540*diameter)))/10000000000

print(f"The approximate volume is {volume:.2f} liters")