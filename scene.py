"""
# File: scene.py
# Author: Herendira Gomez
# Class: CSE111 
# Assignment purpose: Drawing calling function

"""
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing 
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
   
    draw_sky(canvas, scene_width, scene_height)
    
    draw_lago(canvas, scene_width, scene_height)
    draw_text(canvas, 750, 35, "By Herendira", fill="skyBlue4")
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="deep sky blue")
    sol(canvas,100,100,500,500)
    nubes(canvas)
    arcoiris(canvas)

def sol(canvas,x,y,x1,y1):   
    draw_oval(canvas, x, y, x1, y1,width=25,outline="DarkOrange2", fill="gold") 
     


def brillo(canvas,x, y, x1, y2):
    draw_line(canvas, x, y, x1, y2,width=3, fill="aliceBlue")
    
def pajaro(canvas, x, y, x1, y2):   
    draw_line(canvas, x, y, x1, y2, width=5, fill="brown")
   
def draw_lago(canvas, scene_width, scene_height):
   
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="turquoise1")
    draw_mountains(canvas, 600, 170, 200)
    draw_mountains(canvas, 200, 170, 260)
    draw_mountains(canvas, 380, 170, 150)  
    brillo(canvas, 150, 150, 400, 150)
    brillo(canvas, 180, 100, 350, 100)
    brillo(canvas, 200, 50, 225, 50)
    nubes(canvas)
    
def draw_mountains(canvas, center_x, bottom, height):
    skirt_left = center_x + 200
    skirt_right = center_x - 200
    skirt_top = bottom + height
    draw_polygon(canvas, center_x, skirt_top, skirt_right, bottom, skirt_left, bottom,
            outline="green", width=2, fill="darkgreen")

    pajaro(canvas, 25,150,50,175)
    pajaro(canvas, 50,175,75,150)
    pajaro(canvas, 50,300,100,350)
    pajaro(canvas, 100,350,150,300)
    pajaro(canvas, 200,100,220,75)
    pajaro(canvas, 220,75,240,100)

    
def nubes(canvas):
    
        draw_oval(canvas, 750, 400,680, 425,width=25,outline="white", fill="white")
        draw_oval(canvas, 720, 430,750, 450,width=25,outline="white", fill="white")
        draw_oval(canvas, 670, 430,720, 450,width=25,outline="white", fill="white")

        draw_oval(canvas, 290,360,180,300, width=10,outline="white", fill="white") 
        draw_oval(canvas, 260,370,150,320, width=10,outline="white", fill="white")
        draw_oval(canvas, 320,380,245,349, width=10,outline="white", fill="white")       

def arcoiris(canvas):
    draw_arc(canvas,800,100, 0,400,extent=180, width=15, outline="purple")       
    draw_arc(canvas,800,110, 0,410,extent=180, width=15, outline="blue")       
    draw_arc(canvas,800,120, 0,420,extent=180, width=15, outline="yellow")
    draw_arc(canvas,800,130, 0,430,extent=180, width=15, outline="red")


main()