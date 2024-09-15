# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from pandas import read_csv
import pandas as pd
import random

# ---------------------------- CONSTANTS------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- GENERATING WORDS ------------------------------- #
try:
    data= read_csv('flash-card-project-start/data/wordstolearn.csv')
except FileNotFoundError:
    data = read_csv("flash-card-project-start/data/french_words.csv")
french_words = data.to_dict(orient= "records")

def randomwords():
    global englishword, frenchword,fliptimer
    if fliptimer:
        window.after_cancel(fliptimer)
    current_words = random.choice(french_words)
    frenchword= current_words["French"]
    englishword = current_words["English"]
    canvas.itemconfig(card, image = front_img)
    canvas.itemconfig(title_text, text='French',fill = "black")
    canvas.itemconfig(word_text, text=frenchword, fill = "black" )
    fliptimer = window.after(3000, func=flipcard)
    
    

def flipcard():
    canvas.itemconfig(title_text, text='English', fill= "white")
    canvas.itemconfig(word_text, text=englishword, fill = "white")
    canvas.itemconfig(card, image = back_img)

# ---------------------------- UPDATING DATA ------------------------------- #
def correctword():
    global french_words
    datatoremove={'French': frenchword, 'English': englishword}
    french_words.remove(datatoremove)
    df = pd.DataFrame(french_words)
    df.to_csv("flash-card-project-start/data/wordstolearn.csv", index=False)
    randomwords()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas= Canvas(width=800, height= 526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
front_img =PhotoImage(file="flash-card-project-start/images/card_front.png")
back_img =PhotoImage(file="flash-card-project-start/images/card_back.png")
card = canvas.create_image(400, 263, image = front_img)
title_text = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic" ), fill="black")
word_text = canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold" ),  fill="black")
canvas.grid(row=1, column=1, columnspan=2)
fliptimer = None
randomwords()

tick_image = PhotoImage(file="flash-card-project-start/images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=correctword)
tick_button.grid(row=2, column=2)
cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0,command=randomwords)
cross_button.grid(row=2, column=1)
window.mainloop()
