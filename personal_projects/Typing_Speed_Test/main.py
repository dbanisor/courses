from tkinter import *
import time

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         time_format = '{:02d}:{:02d}'.format(mins, secs)
#         print('\r', time_format, end='')
#         time.sleep(1)
#         time_sec -= 1
#
# countdown(5)

# ---------------------------- LETTERS IN LABEL - LIST ------------------------------- #

letters_in_label = []

# ---------------------------- RETRIEVE INPUT AND COMPARE MECHANISM ------------------------------- #
letters_written = []

letter_index = -1

def check_letters_written(event):
    global letter_index

    # daca user-ul apasa backspace va sterge ultima litera introdusa in lista
    if event.char != '':
        letters_written.append(event.char)
        letter_index += 1
        print(letter_index)
        if letters_written[letter_index] != letters_in_label[letter_index]:
            print("there's a difference")
            letter_to_highlight = "1." + str(letter_index)
            text_field.tag_add("highlightline", letter_to_highlight)
            text_field.tag_config("highlightline", background="yellow")
    else:
        letters_written.pop()
        letter_index -= 1
    print(letters_written)



# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=100, height=50)

# Instructions label
label_1 = Label(window, font=('Helvetica 12'), text="Type the following:")
label_1.grid(row=1)

# The text to type label
var_label_2 = StringVar()

label_2 = Label(window, font=('Helvetica', 16, 'italic'), fg="red", textvariable=var_label_2)
var_label_2.set("the rain in spain stays mainly in the plain.")
label_2.grid(row=2)

for char in var_label_2.get():
    letters_in_label.append(char)
print(letters_in_label)

# Entry text
text_field = Text(window)
text_field.focus()
text_field.grid(row=3)
text_field.bind("<KeyRelease>", check_letters_written)

# Timer text
timer_text = canvas.create_text(50, 15, text="00:00", fill="black", font=("Courier", 24, "bold"))
canvas.grid(row=0)



window.mainloop()
