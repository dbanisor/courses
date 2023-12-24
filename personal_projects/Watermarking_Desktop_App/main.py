from PIL import Image
from tkinter import *

window =Tk()
window.config(padx=10, pady=10)


canvas = Canvas(width=1200, height=700)
background_image = PhotoImage(file="tomato.png")
canvas.create_image((600, 350), image=background_image)
canvas.pack()









window.mainloop()