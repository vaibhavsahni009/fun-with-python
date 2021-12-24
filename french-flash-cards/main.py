BACKGROUND_COLOR = "#B1DDC6"

# path="french-flash-cards"
path="."

from tkinter import *
import pandas as pd
import random
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
word={}

######## word change

def word_change():
    global word,timer
    window.after_cancel(timer)
    word=random.choice(list_of_words)
    canvas.itemconfig(title_text,text="French")
    canvas.itemconfig(word_text,text=word["French"])
    canvas.itemconfig(background,image=card_front_img)
    
    timer=window.after(3000,flip)    

def flip():
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=word["English"],fill="white")
    canvas.itemconfig(background,image=card_back_img)
    

def is_known():
    list_of_words.remove(word)
    data=pd.DataFrame(list_of_words)
    data.to_csv(f"{path}/data/words_to_learn.csv",index=False)
    word_change()


timer=window.after(3000,flip)    

######## Read data from CSV
try:
    data=pd.read_csv(f"{path}/data/words_to_learn.csv")
    list_of_words=data.to_dict(orient="records")
except FileNotFoundError:
    data=pd.read_csv(f"{path}/data/french_words.csv")
    list_of_words=data.to_dict(orient="records")

########UI
canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file=f"{path}/images/card_front.png")
card_back_img=PhotoImage(file=f"{path}/images/card_back.png")

background=canvas.create_image(400,263,image=card_front_img)
title_text=canvas.create_text(400,150,font=("Ariel",40,"italic"),text="Title")
word_text=canvas.create_text(400,263,font=("Ariel",60,"bold"),text="word")


canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

cross_img=PhotoImage(file=f"{path}/images/wrong.png")
unknown_button=Button(image=cross_img,highlightthickness=0,command=word_change)
unknown_button.grid(row=1,column=0)


check_img=PhotoImage(file=f"{path}/images/right.png")
unknown_button=Button(image=check_img,highlightthickness=0,command=is_known)
unknown_button.grid(row=1,column=1)

word_change()
window.mainloop()