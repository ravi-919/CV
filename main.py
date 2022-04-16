from tkinter import *
from PIL import ImageTk, Image
import pandas
import random
from gtts import gTTS
import os
import playsound

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    language = 'fr'
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    audio = gTTS(text=current_card['French'], lang=language)
    audio.save('french.mp3')
    playsound.playsound('/Users/Jaisinghani/Desktop/pycharm_projects/flash-card-project-start/french.mp3', True)
    os.remove('french.mp3')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card_back_img = ImageTk.PhotoImage(Image.open(('images/card_back.png')))
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=is_known)
right_button.grid(column=1, row=1, padx=15, pady=15)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=next_card)
wrong_button.grid(column=0, row=1, padx=15, pady=15)

next_card()


window.mainloop()