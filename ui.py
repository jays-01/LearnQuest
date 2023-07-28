from tkinter import*
from brain import QuizBrain

THEME = "#375362"

class QuizInterface:

    def __init__(self, brain: QuizBrain):
        self.quiz = brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME,padx=20,pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text="Some question text",fill=THEME,font=("Arial",20,"italic"),width=280)
        

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img,bg="green",highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img,bg="red",highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)


        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text=f"You have reached the end of this quiz.\n Your Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)




        
