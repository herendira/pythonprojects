import tkinter as tk

frameA = tk.Frame(background="#c8c8c8")
frameB = tk.Frame(width=200, height = 200, background="#646464")
# Nested Frame. framebb is created within frameB without width or height
framebb = tk.Frame(frameB, background="#646464")
frameC = tk.Frame(width=100, height = 100, background="bisque")

frameA.pack(side='top', fill=None)
frameB.pack(side='top')
# expand is the key parameter to center the framebb within frameB
framebb.pack(expand=True)
frameC.pack(side='bottom')

#frameA.pack_propagate(False)
frameB.pack_propagate(False)
frameC.pack_propagate(False)


tk.Label(frameA, text = "Text within the frame A").pack()

a = tk.Button(framebb, text = "A").pack()
b = tk.Button(framebb, text = "B").pack()
c = tk.Button(framebb, text = "C").pack()
d = tk.Button(frameC, text = "D").pack()
e = tk.Button(frameC, text = "E").pack()

tk.mainloop()