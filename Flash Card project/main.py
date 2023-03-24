from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
timer = 3000
n_card = {}
words_known = []

try:
    words_data = pandas.read_csv("data/words_to_learn.csv", sep=";")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv", sep=";")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = words_data.to_dict(orient="records")

def rand_card():
    global timer, n_card
    window.after_cancel(timer)
    n_card = choice(words_to_learn)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=n_card["Inglese"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    timer = window.after(3000, flip_card, n_card["Italiano"])


def flip_card(card):
    canvas.itemconfig(title_text, text="Italiano", fill="white")
    canvas.itemconfig(word_text, text=card, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def delete_card():
    words_to_learn.remove(n_card)
    words_known.append(n_card)
    words_df = pandas.DataFrame(words_known, columns=["Inglese", "Italiano", "Frase inglese", "Traduzione frase"])
    words_df.to_csv("data/words_known.csv", index=False)
    words_to_learn_df = pandas.DataFrame(words_to_learn, columns=["Inglese", "Italiano", "Frase inglese", "Traduzione frase"])
    words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    rand_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightcolor=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=rand_card)
x_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
v_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=delete_card)
v_button.grid(column=1, row=1)

rand_card()

window.mainloop()
