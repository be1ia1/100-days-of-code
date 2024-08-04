from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.config(background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        q_text = self.quiz.next_question()
        self.question_text = self.canvas.create_text(150, 125,
                                text=q_text,
                                font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0,row=1, columnspan=2, sticky=EW, pady=50)

        yes_image = PhotoImage(file='images/true.png')
        self.yes_button = Button(image=yes_image, highlightthickness=0)
        self.yes_button.grid(column=0, row=2)
        no_image = PhotoImage(file='images/false.png')
        self.no_button = Button(image=no_image, highlightthickness=0)
        self.no_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)