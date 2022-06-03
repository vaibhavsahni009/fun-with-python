from tkinter import *
from quiz_brain import QuizBrain

from numpy import imag
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(
            text=f"Score:{self.quiz_brain.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question = self.canvas\
            .create_text(150,
                         125,
                         width=280,
                         text="question",
                         fill=THEME_COLOR,
                         font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="quizzler-app-start/images/true.png")
        false_image = PhotoImage(file="quizzler-app-start/images/false.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_selected)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_selected)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            # print(self.quiz_brain.question_number)
            self.score_label.config(text=f"Score:{self.quiz_brain.score}")
            self.canvas.itemconfigure(
                self.question, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfigure(
                self.question, text="You Have reached end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    # def update_score(self):

    def true_selected(self):

        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_selected(self):

        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, lambda: self.canvas.config(bg="white"))

        self.get_next_question()
