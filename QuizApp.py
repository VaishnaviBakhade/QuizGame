import tkinter 
from tkinter import*
from PIL import ImageTk,Image
import random

Questions = [
    "Is Python case sensitive when dealing with identifiers ?",
    "Which of the following is the correct extension of the Python file ?",
    "Whcih of the following is used to define a block of code in python language ?",
    "Which keyword is used for function in python language ?",
    "Which of the following character is used to give single-line comments in python ?",
    "What will be the value of the following Python expression 4 + 3 % 5 ?",
    "What will be the output of the following Python code snippet if x =1 ? x<<2",
    "Which of the following is the truncation division operator in python ?",
    "Which of the following functions is a built-in function in python ?",
    "Which of the following is not a core data type in Python programming ?"
]

answer_choice =[
    ["no","yes","machine dependent","none of the mentioned"],
    [".python",".pl",".py",".p"],
    ["Indentation","Key","Brackets","All of the mentioned"],
    ["Function","def","Fun","Define"],
    ["//","#","!","/*"],
    ["7","2","4","1"],
    ["4","2","1","8"],
    ["|","//","/","%"],
    ["factorial()","print()","seed()","sqrt()"],
    ["Tuples","Lists","Class","Dictionary"],
]
answers = [1,2,0,1,1,0,0,1,1,2]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes)< 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(root,font=("Consolas",20),background = "#ffffff",border = 0)
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(root,font=("Consolas",20),background = "#ffffff")
    labelresulttext.pack()
    if score >= 8:
        img = ImageTk.PhotoImage(Image.open('F:\PYTHON\3.png'))
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
        #img1.pack()
    elif(score >=5 and score < 2):
        img = ImageTk.PhotoImage(Image.open('F:\PYTHON\1.png'))
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You be perform better !!")
    else:
        img = ImageTk.PhotoImage(Image.open('F:\PYTHON\2.png'))
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should work hard !!")


        
        


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x +=1
    print(score)
    showresult(score)



ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=Questions[indexes[ques]])
        r1['text'] = answer_choice[indexes[ques]][0]
        r2['text'] = answer_choice[indexes[ques]][1]
        r3['text'] = answer_choice[indexes[ques]][2]
        r4['text'] = answer_choice[indexes[ques]][3]
        ques += 1 
    else:
        print(indexes)
        print(user_answer)
        calc()

def startQuiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(root,text= Questions[indexes[0]],font=("Consolas",16),width=500,justify='center',wraplength=400,background = "#ffffff")
    lblQuestion.pack(pady=[100,30])

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(root,text=answer_choice[indexes[0]][0],font=("Times",12),value = 0,variable =radiovar,command=selected,background = "#ffffff")
    r1.pack(pady=5)

    r2 = Radiobutton(root,text=answer_choice[indexes[0]][1],font=("Times",12),value = 0,variable =radiovar,command=selected,background = "#ffffff")
    r2.pack(pady=5)

    r3 = Radiobutton(root,text=answer_choice[indexes[0]][2],font=("Times",12),value = 0,variable =radiovar,command=selected,background = "#ffffff")
    r3.pack(pady=5)

    r4 = Radiobutton(root,text=answer_choice[indexes[0]][3],font=("Times",12),value = 0,variable =radiovar,command=selected,background = "#ffffff")
    r4.pack(pady=5)

def startIspressed():
    lb.destroy()
    btnStart.destroy()
    lbInstruction.destroy()
    lbrules.destroy()
    gen()
    startQuiz()

root = tkinter.Tk()
root.title("Quiz Game")
root.geometry("600x550")
root.config(background='#ffffff')
root.resizable(0,0)

img = ImageTk.PhotoImage(Image.open('F:\PYTHON\img1.png'))
lb = Label(image=img,background='white')
lb.pack(pady=(40,0))

btnStart = Button(root,text="Welcome",font=("comic sans Ms",24,"bold"),background='#b5cae9',foreground='black',command=startIspressed,)
btnStart.pack()

lbInstruction = Label(root,text ='Read the Rules And\nClick Welcome Once you are ready for Game!!',
background="#ffffff",
font=("Consolas",14),justify ='center',)
lbInstruction.pack(pady=(20,120))

lbrules = Label( root,text="This quiz contain 10 question\n You will 20 seconds to solve the question\nOnce you select the answer will be a final choice\nHence think before you select",
width=100,font=("Times",14),background='black',foreground='yellow')
lbrules.pack()



root.mainloop()