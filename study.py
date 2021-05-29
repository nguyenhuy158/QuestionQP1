import os
from Manager import ManagerQuestion, Question
from tkinter import *
import random
import tkinter as tk
from tkinter import messagebox


def removeNewline(sources):
    # remove line 'empty'
    for element in sources:
        if element == '\n':
            sources.remove(element)
    # remove char '\n' if it exists
    for index in range(len(sources)):
        sources[index] = sources[index].replace('\n', '')
    return sources


def inputStudyed(path='studyed.txt'):
    try:
        file = open(path, mode='r', encoding='utf8')
        lines = file.readlines()
        lines = removeNewline(lines)

        countQues = int(len(lines) / 8)
        print("we have {} question.".format(countQues))

        questions = []
        for i in range(0, 8 * (countQues - 1) + 1, 8):
            ques = Question(ques=lines[i],
                            ans1=lines[i + 1],
                            ans2=lines[i + 2],
                            ans3=lines[i + 3],
                            ans4=lines[i + 4],
                            key=lines[i+5],
                            cRight=lines[i+6],
                            cWrong=lines[i+7])
            questions.append(ques)
        file.close()
    except Exception as e:
        print(str(e))
        return None
    return questions


def clickA():
    if int(ques.key) == 1:
        ques.right()

        print('bingo')
    else:
        ques.wrong()
        if messagebox.askokcancel(title="Error", message=ques.getKey()):
            print(ques.getKey())
        else:
            window.quit()
    nextQues()


def clickB():
    if int(ques.key) == 2:
        ques.right()
        print('bingo')
    else:
        ques.wrong()
        if messagebox.askokcancel(title="Error", message=ques.getKey()):
            print(ques.getKey())
        else:
            window.quit()
    nextQues()


def clickC():
    if int(ques.key) == 3:
        ques.right()
        print('bingo')
    else:
        ques.wrong()
        if messagebox.askokcancel(title="Error", message=ques.getKey()):
            print(ques.getKey())
        else:
            window.quit()
    nextQues()


def clickD():
    if int(ques.key) == 4:
        ques.right()
        print('bingo')
    else:
        ques.wrong()
        if messagebox.askokcancel(title="Error", message=ques.getKey()):
            print(ques.getKey())
        else:
            window.quit()
    nextQues()


def changeQuestion():
    global counted
    counted += 1
    window.title(
        "==>Welcome to my Study<== {}/{}".format(counted, len(questions)))
    LabelQues.config(text=ques.getQues(), wraplength=500,
                     height=5, bg='#fcb353', font=('Arial', 20))
    btnA.config(text=ques.ans1,
                bd=0, bg='#45ccde', width=300, font=('Arial', 20))
    btnB.config(text=ques.ans2,
                bd=0, bg='#45ccde', width=300, font=('Arial', 20))
    btnC.config(text=ques.ans3,
                bd=0, bg='#45ccde', width=300, font=('Arial', 20))
    btnD.config(text=ques.ans4,
                bd=0, bg='#45ccde', width=300, font=('Arial', 20))


def nextQues():
    save(questions)
    questions.sort(key=lambda e: (
        int(e.cWrong), -int(e.cRight)), reverse=True)
    global ques
    ques = random.choice(questions[0: int(len(questions) / 3)])
    changeQuestion()


def save(source, path='./out.txt'):
    print("i'm storing...")
    try:
        with open(path, mode='w', encoding='utf8') as fo:
            for e in source:
                fo.write("{}\n".format(e.getInformation()))
            return True
    except Exception as e:
        return False


counted = 0
window = Tk()
# title game
window.title("==>Welcome to my Study<==")
window.config(background='#fcb353')
window.geometry("700x150")
window.attributes('-fullscreen', True)
window.config()

frame = Frame(window, width=500, height=300, bg='#fcb353')
frame.pack()
path = './study/out1.txt'
questions = inputStudyed(path)
ques = questions[0]

LabelQues = Label(frame,  anchor=tk.W)
LabelQues.pack()

btnA = Button(frame, command=clickA)
btnA.pack(side=TOP,  anchor=tk.W)

btnB = Button(frame, command=clickB)
btnB.pack(side=TOP,  anchor=tk.W)

btnC = Button(frame, command=clickC)
btnC.pack(side=TOP,  anchor=tk.W)

btnD = Button(frame, command=clickD)
btnD.pack(side=TOP,  anchor=tk.W)
changeQuestion()

tk.Button(text="QUIT",
          bd=0,
          bg="Orange",
          fg="white",
          command=quit,
          activebackground="blue",
          font="Firacode",
          relief="ridge",
          padx=10,
          pady=10
          ).pack()
window.mainloop()

print('see yeah')
