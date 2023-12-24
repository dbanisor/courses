from tkinter import *
from tkinter import messagebox
from random import choice, randint, choice, shuffle
import pyperclip
import json

FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]

    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
            ### Read the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                ### Saving the updated data
                json.dump(new_data, file, indent=4)
        else:
            ### Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()

    try:
        with open("data.json") as file:
            ### Read the old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="No details for this website.")



# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas & Image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "denise.banisor@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons

generate_button = Button(text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=save, bg="gray", fg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=20, command=find_password, font=("Arial", 8, "bold"), fg="blue")
search_button.grid(column=2, row=1)




window.mainloop()