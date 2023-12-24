from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#--------------------------------- GENERATE WORD ---------------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv", encoding='unicode_escape')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv", encoding='unicode_escape')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Code", fill="black")
    canvas.itemconfig(card_word, text=current_card["Code"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(7000, func=flip_card)


#--------------------------------- FLIP CARD ---------------------------------#
def flip_card():
    canvas.itemconfig(card_title, text="Explanation", fill="white")
    canvas.itemconfig(card_word, text=current_card["Explanation"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

#--------------------------------- UI SETUP ---------------------------------#
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(7000, func=flip_card)

# Image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(401, 264, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"), width=600)
card_word = canvas.create_text(400, 263, text="", font=("Arial", 25, "bold"), width=600)
canvas.grid(row=0, columnspan=2)

# Buttons
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()























