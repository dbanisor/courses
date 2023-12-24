from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

### Window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

### Labels
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New New Text")
### The method below places the label onto the screen and centers it. Otherwise it won't appear on the screen.
my_label.grid(column=0, row=0)

### Buttons
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

### Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


### The code below is what keeps the window on the screen.
window.mainloop()
