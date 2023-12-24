from tkinter import *


def button_clicked():
    miles = float(user_entry.get())
    km = miles * 1.609344
    result.config(text=f"{km}")


# Window
converter_window = Tk()
converter_window.title("Mile to Km Converter")
converter_window.config(padx=20, pady=20)


# Entry
user_entry = Entry(width=10)
user_entry.get()
user_entry.grid(column=1, row=0)
user_entry.focus()
user_entry.insert(END, 0)


# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)


# Labels

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

result = Label(text=0)
result.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


converter_window.mainloop()