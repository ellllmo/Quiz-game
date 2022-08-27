import html

class QuizBrain:
    def __init__(self,ques_bank):
        self.num=0
        self.list=ques_bank
        self.score=0

    def still_have_quiz(self):
        return self.num<len(self.list)
           
    def next(self):
        nextlist=self.list[self.num]
        quection=f"Q.{self.num}:{html.unescape(nextlist['question'])}"
        answer=[]
        answer=html.unescape(nextlist["incorrect_answers"])
        correct_answer=html.unescape(nextlist['correct_answer'])
        answer.append(correct_answer)
        self.num+=1
        return (quection,answer,correct_answer)
        
        
    def check(self,answer,current_answer):
        if answer.lower() ==current_answer.lower() :
            return True
        else:
            return False
    