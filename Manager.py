import random
from tkinter import *


def inputInt(content):
    while True:
        try:
            choose = int(input(content))
            return choose
        except Exception as e:
            print('enter again!')


def clickA(ques):
    if int(ques.key) == 1:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))


def clickB(ques):
    if int(ques.key) == 2:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))


def clickC(ques):
    if int(ques.key) == 3:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))


def clickD(ques):
    if int(ques.key) == 4:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))


class ManagerQuestion:
    def __init__(self):
        self.count = 0
        self.list = []

    def getNumberQuestion(self):
        return self.count

    def addQuestion(self, ques):
        self.list.append(ques)
        self.count += 1

    def showQuestion(self):
        for e in self.list:
            print(e)

    def getRank(self):
        self.sort()
        for i in range(self.count):
            print("{} - {}/{}".format(i,
                  self.list[i].cRight, self.list[i].cWrong))

    # def study(self):
    #     numberAnswered = 0

    #     ques = random.choice(self.list[0:int(self.count / 3)])

    #     # window.geometry("400x400")
    #     # window.minsize(400, 400)
    #     # window.maxsize(400, 400)

    #     # title game
    #     window.title = "==>Welcome to my Study<=="
    #     window.config(background='#fcb353')

    #     frame = Frame(window)
    #     frame.pack()

    #     question = Label(frame, text=ques.ques)
    #     question.pack()
    #     btnA = Button(frame, text=ques.ans1, command=lambda: clickA(ques))
    #     btnA.pack(side=TOP)

    #     btnB = Button(frame, text=ques.ans2, command=lambda: clickB(ques))
    #     btnB.pack(side=TOP)

    #     btnC = Button(frame, text=ques.ans3, command=lambda: clickC(ques))
    #     btnC.pack(side=TOP)

    #     btnD = Button(frame, text=ques.ans4, command=lambda: clickD(ques))
    #     btnD.pack(side=TOP)

    #     window.mainloop()

    def write(self, source, path='out-studyed.txt'):
        print("i'm storing...")
        try:
            with open(path, mode='w', encoding='utf8') as fo:
                for e in source:
                    fo.write("{}\n".format(e.getInformation()))
                return True
        except Exception as e:
            return False

    def save(self, path='out-studyed.txt'):
        print("i'm storing...")
        try:
            with open(path, mode='w', encoding='utf8') as fo:
                self.sort()
                for e in self.list:
                    fo.write("{}\n".format(e.getInformation()))
                return True
        except Exception as e:
            return False

    def sort(self):
        self.list.sort(key=lambda e: (
            int(e.cWrong), -int(e.cRight)), reverse=True)

    def get(self, index=0):
        return self.list[index]

    def getQuestionMostWrongs(self, count=5):
        mostWrongs = []
        for i in range(count):
            mostWrongs.append(self.get(i))
        return mostWrongs

    def getQuestionMostWrong(self):
        self.sort()
        return self.get(0)

    def __str__(self):
        return "managerQuestion have {} questions".format(str(self.count))


class Question:
    def __init__(self, ques, ans1, ans2, ans3, ans4, key, cRight=0, cWrong=0):
        self.ques = ques
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.key = key
        self.cRight = cRight
        self.cWrong = cWrong

    def setKey(self):
        while True:
            try:
                newKey = int(input("please enter new key 1 2 3 4: "))
                if newKey > 4 or newKey < 1:
                    continue
                self.key = newKey
                break
            except Exception as e:
                pass

    def check(self, e):
        if (str(self.key).__eq__(str(e))):
            return True
        return False

    def right(self):
        self.cRight = int(self.cRight) + 1

    def wrong(self):
        self.cWrong = int(self.cWrong) + 1

    def getQues(self):
        return "{}/{} {}".format(self.cRight, self.cWrong, self.ques)

    def getKey(self):
        ans = ""
        ans = self.ans1 if self.key == '1' else ans
        ans = self.ans2 if self.key == '2' else ans
        ans = self.ans3 if self.key == '3' else ans
        ans = self.ans4 if self.key == '4' else ans
        return "answer is {}. {}".format(self.key, ans)

    def getInformation(self):
        return str(self.ques) + "\n" + str(self.ans1) + "\n" + str(self.ans2) + "\n" + str(self.ans3) + "\n" + str(self.ans4) + "\n" + str(self.key) + "\n" + str(self.cRight) + "\n" + str(self.cWrong)

    def __repr__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n".format(self.ques, self.ans1,
                                                 self.ans2, self.ans3,
                                                 self.ans4, self.key)

    def __str__(self):
        return "\nCau hoi la({}/{}): {}\n1. {}\n2. {}\n3. {}\n4. {}\n".format(self.cRight, self.cWrong,
                                                                              self.ques, self.ans1, self.ans2, self.ans3, self.ans4)
