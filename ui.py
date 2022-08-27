from tkinter import Button, Tk,Canvas,Label, font
from quiz_brain import QuizBrain
import random


green="#59CE8F"
blue="#355764"
liteblue="#81CACF"
yellow="#FFEA11"
red="#FF1E00"

class Ui():
    def __init__(self,quiz:QuizBrain):
        self.num=0
        self.score=0
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Q & A")
        self.window.config(padx=20,pady=20,background=blue)
        self.score_label = Label(text=f"⚜ Score: {self.score}", fg="white", bg=blue,font=("Verdana",10,"bold"))
        self.score_label.grid(row=0, column=1)
        self.cnv=Canvas(bg=yellow,width=300,height=200)
        self.quiz_text=self.cnv.create_text(150,100,text="Welcome to Q & A 🙌",font=("arial",15,""),width=280)
        self.cnv.grid(row=1,column=0,columnspan=2,pady=50)
        self.true_button=Button()
        self.one=Button(command=lambda: self.check(self.one["text"]),text="      Start      ",height=2,bg=liteblue,font=("",11,"bold"))
        self.one.grid(row=2,column=0,pady=20,padx=20)
        self.two=Button(command=lambda: self.check(self.two["text"]),text="      Start      ",height=2,bg=liteblue,font=("",11,"bold"))
        self.two.grid(row=2,column=1,pady=20,padx=20)
        self.three=Button(command=lambda: self.check(self.three["text"]),text="      Start      ",height=2,bg=liteblue,font=("",11,"bold"))
        self.three.grid(row=3,column=0,pady=20,padx=20)
        self.four=Button(command=lambda: self.check(self.four["text"]),text="      Start      ",height=2,bg=liteblue,font=("",11,"bold"))
        self.four.grid(row=3,column=1,pady=20,padx=20)
        self.window.mainloop()

    def get_next_ques(self):
        self.cnv.config(bg=yellow)
        self.true_button.config(bg=liteblue)
        if self.quiz.still_have_quiz():
            question,answer,self.correct_answer=self.quiz.next()
            self.cnv.itemconfig(self.quiz_text,text=question)
            for_one=random.randint(0,3)
            self.one.config(text=answer[for_one])
            answer.remove(answer[for_one])
            for_two=random.randint(0,2)
            self.two.config(text=answer[for_two])
            answer.remove(answer[for_two])
            for_three=random.randint(0,1)
            self.three.config(text=answer[for_three])
            answer.remove(answer[for_three])
            self.four.config(text=answer[0])
            if self.correct_answer==self.one["text"]:
                self.true_button=self.one
            elif self.correct_answer==self.two["text"]:
                self.true_button=self.two
            elif self.correct_answer==self.three["text"]:
                self.true_button=self.three
            else: 
                self.true_button=self.four

        else:
            self.cnv.itemconfig(self.quiz_text,text="the end ✋",font=("arial",20,""))
            self.one.destroy()
            self.two.destroy()
            self.three.destroy()
            self.four.destroy()
        
        
        
    def check(self,text_button):
        if self.num==0:
            self.num=1
            self.get_next_ques()
        else:
            true_ans=self.quiz.check(text_button,self.correct_answer)
            if true_ans:
                self.cnv.config(bg=green)
                self.score+=1
                self.score_label.config(text=f"⚜ Score: {self.score}")
                self.window.after(1000,self.get_next_ques)
            else:
                self.cnv.config(bg=red)
                self.true_button.config(bg=green)
                self.window.after(1000,self.get_next_ques)