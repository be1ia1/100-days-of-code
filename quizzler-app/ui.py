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

        self.canvas = Canvas(width=300, height=250,
                             bg='white', highlightthickness=0)
        q_text = self.quiz.next_question()
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=q_text,
                                                     font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, sticky=EW, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=lambda: self.quiz.check_answer("True"))
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=lambda: self.quiz.check_answer("False"))
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
