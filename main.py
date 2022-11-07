
import json

import timer

from form import age_res, class_res, name_res


print(age_res)
print(name_res)
print(class_res)

from timer import *
import tkinter as tk
from tkinter import ttk, messagebox

with open("questions.json", "r") as source:
    data = json.load(source)
    # print(data)

root = tk.Tk()
root.geometry("1000x500")

# print(d_questions)

# print(type(questions))



# radio = tk.Radiobutton(root, text="me")
# radio.place(x=0, y=20)
# radio.invoke()

# que = data["options"][1]
# options = tk.Radiobutton(root, text=que)
# options.place(x=120, y=0)

# for quest in questions:
#     list = ["me", "you"]
#     var = tk.StringVar()
#     radio = tk.Radiobutton(root,text=quest)
#     radio.bind("<Return>")
#     radio.place(x=0,y=y)
#     y+=20 
d_var = tk.IntVar()
global num
num = 1
global score
score = 0

global next_num
next_num = 2
questions = data["options"]
class options:
    def __init__(self, option):
        global num
        for quest in option:
            global d_options
            global text
            for text, value in [(quest, num)]:
                d_options = tk.Radiobutton(root, text="", value=value, variable=d_var).pack(anchor="nw", pady=10)
                print(quest[0])
                num+=1
    def destroy_all(self):
        global num
        d_options.desroy()



options(data["options"][next_num])





global number
number = 0

each_question = tk.Label(text="")

labelA = tk.Label(text = "")
labelB = tk.Label(text= "") 
labelC = tk.Label(text= "") 
labelD = tk.Label(text= "") 

class next_quest:
    def __init__(self):
        global number, score, answer
        global questions
        try:
            each_question.config(text="")

            each_question.config(text=data["questions"][number])
            each_question.place(x=30, y=200)

            # global next_num, d_options, questions
            # # d_options.update()
            # questions = data["options"][next_num][number]
            # print(questions)
            # ans_label = tk.Label(text=questions) 
            # ans_label.place(x=20,y=0)

            # questions = data["options"][next_num][1]
            # print(questions)
            # ans_label = tk.Label(text=questions) 
            # ans_label.place(x=20,y=21)

            questions = data["options"][number]



        
            labelA.config(text = questions[0])
            labelB.config(text= questions[1]) 
            labelC.config(text= questions[2]) 
            labelD.config(text= questions[3]) 

            labelA.place(x=30, y=10)
            labelB.place(x=30, y=54)
            labelC.place(x=30, y=100)
            labelD.place(x=30, y=139)
        except IndexError:
            pass



        try:
            print(questions)
            print(score)

            answer = d_var.get()

            if answer == 1:
                answer = "A"
            if answer  == 2:
                answer = "B"
            if answer == 3:
                answer = "C"
            if answer == 4:
                answer = "D"
            # try:
            print(answer)
            d_answers = data["answers"][number]
            if answer == d_answers:
                score += 1
                print(score)
            number += 1
        except IndexError:
            if number  == 50:
                submit_btn = tk.Button(text="Submit")
                submit_btn.place(x=400, y=400)
                next_btn.config(state=tk.DISABLED)
            
        # questions = data["options"][next_num]
    # d_options.destroy()

    # options(questions)

# class timer_class:
    # def __init__(self):
    #     time_student = timer.start_time()
    #     tk.Label(text=time_student).place(x=900,y=2)



next_call = next_quest()
next_btn = tk.Button(text="Next", command=next_quest)
next_btn.place(x=300, y=400)
# timer_call = timer_class() 



# scroll = tk.Scrollbar(root, command=root.yview)
# scroll.place(x=480, y=0, height=480)
# root.config(yscrollcommand = scroll.set)

root.mainloop()


# age, *classes = ("Ade", 13, "jss2")
# print(age, *classes)