import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

WORDS_TO_LEARN_FILE = 'flash-card-project-start/data/words_to_learn.csv'
ENGLISH_WORDS_FILE = 'flash-card-project-start/data/english_words.csv'

try:
    data = pd.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    data = pd.read_csv(ENGLISH_WORDS_FILE)

data_dict = data.to_dict(orient='records')
data_to_learn = []

class FlashCard():

    def __init__(self) -> None:
        self.timer = None
        self.update(answer=None)
    def update(self, answer):
        if self.timer:
            window.after_cancel(self.timer)
        self.card = random.choice(data_dict)
        if answer is True:
            data_dict.remove(self.card)
        elif len(data_to_learn) == 2:
            new_data = pd.DataFrame.from_dict(data_to_learn)
            new_data.to_csv(WORDS_TO_LEARN_FILE, encoding='utf-8', sep=',', index=False)
        elif answer is False:
            data_to_learn.append(self.card)
            print(len(data_to_learn))

            
        canvas.itemconfig(lang_id, text='English', fill='black')
        canvas.itemconfig(text_id, text=self.card['English'], fill='black')
        canvas.itemconfig(card_background, image=front)
        self.timer = window.after(2000, self.show_answer)
    def show_answer(self):
        canvas.itemconfig(card_background, image=back)
        canvas.itemconfig(lang_id, text='Ukrainian', fill='white')
        canvas.itemconfig(text_id, text=self.card['Ukrainian'], fill='white')

window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

back = tk.PhotoImage(file='flash-card-project-start/images/card_back.png')
front = tk.PhotoImage(file='flash-card-project-start/images/card_front.png')
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front)
canvas.grid(column=0,row=0, columnspan=2, sticky=tk.EW)
lang_id = canvas.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
text_id = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

card = FlashCard()

no_image = tk.PhotoImage(file='flash-card-project-start/images/wrong.png')
no_button = tk.Button(image=no_image, highlightthickness=0, command=lambda: card.update(False))
no_button.grid(column=0, row=3)

yes_image = tk.PhotoImage(file='flash-card-project-start/images/right.png')
yes_button = tk.Button(image=yes_image, highlightthickness=0, command=lambda: card.update(True))
yes_button.grid(column=1, row=3)

window.mainloop()