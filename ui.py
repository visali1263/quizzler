from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Visali's Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, font=(10))
        self.score.config(fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=350, width=400, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(200, 175,width=380, text="Question here", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        tick_img = PhotoImage(file='images/true.png')
        self.true = Button(image=tick_img, highlightthickness=0, command=self.true_ans)
        self.true.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.false = Button(image=wrong_img, highlightthickness=0, command=self.false_ans)
        self.false.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def true_ans(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
