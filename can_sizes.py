"""
# File: cone_volume.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: parameters and arguments inside a function.
"""
"""Compute and print the volume of a right circular cone."""
import math
def main():
    vol=float
    name="1 Picnic"
    radius_cm=6.83
    height_cm=10.16
    cost_dl=0.28
    vol=compute_volume(radius_cm,height_cm)
    #surface_area=compute_surface_area(radius_cm,height_cm)
    #storage_efficiency=vol/surface_area
    print(f"{name} {vol:.2f}")

def compute_volume(radius_cm,height_cm):
    return math.pi*(radius_cm**2)*height_cm
    

# def compute_surface_area(radius_cm,height_cm):
#     surface=2*math.pi*radius_cm(radius_cm+height_cm)
#     return surface
   
main()