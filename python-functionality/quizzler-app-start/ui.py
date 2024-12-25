from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz : QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height= 250,  highlightthickness=0)
        self.questiontext =self.canvas.create_text(
            150,
            125,
            text="Question",
            width= 280,
            fill= THEME_COLOR,
            font= ("Ariel", 20 , "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 50)

        self.true_img = PhotoImage(file="quizzler-app-start/images/true.png")
        self.True_button = Button(image=self.true_img, highlightthickness=0, command=self.checktrue )
        self.True_button.grid(row=2, column=0)
        self.False_img = PhotoImage(file="quizzler-app-start/images/false.png")
        self.False_button = Button(image=self.False_img, highlightthickness=0, command=self.checkfalse)
        self.False_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Ariel", 14))
        self.score_label.grid(row=0, column=1)  
        self.getnextquestion()
        self.window.mainloop()


    def getnextquestion(self):
        self.canvas.config(bg= 'white')
        if  self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questiontext, text = q_text)
        else:
            self.canvas.itemconfig(self.questiontext, text = "You've finished the quiz")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")

    def checktrue(self):
        self.updatescore(self.quiz.check_answer("True"))
    
    def checkfalse(self):
        self.updatescore(self.quiz.check_answer("False"))

    def updatescore(self, result):
        if result == True:
            self.canvas.itemconfig(self.questiontext, text = "Yay you got that correct")
            self.canvas.config(bg= 'green')
        else:
            self.canvas.itemconfig(self.questiontext, text = "Uh oh that's incorrect")
            self.canvas.config(bg= 'red')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000,self.getnextquestion)
    
        

