"""
# File: boxes.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Call function

"""
import math
items_number=float(input("Enter the number of items: "))
items_perbox=float(input("Enter the number of items per box: "))
resul=items_number/items_perbox

print(f"For {items_number:.0f}, packing {items_perbox:.0f} items in each box, you will need: {math.ceil(resul)} boxes")