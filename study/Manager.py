import random


def mySort(e):
    a = int(e.cRight) - int(e.cWrong)
    if (a < 0):
        return 0
    return a


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

    def study(self):
        # title game
        print("==>Welcome to my Study<==")
        print('Please enter if you can continue')

        numberAnswered = 0
        while True:
            self.list.sort(key=mySort)
            # random choice in 1/3 question first in list
            # because they are question you is wrong
            ques = random.choice(self.list[0:int(self.count / 3)])
            print(ques)

            userChoose = str(
                input("[{}/{}] enter 1 2 3 4 or cancel(c) offer(o): ".format(numberAnswered, self.count)))
            numberAnswered += 1

            while (userChoose == ''
                   or not (userChoose == '1' or userChoose == '2'
                           or userChoose == '3' or userChoose == '4' or userChoose == 'c' or userChoose == 'o')):
                userChoose = str(input("enter again:"))

            if (userChoose == 'c'):
                break

            if (userChoose == 'o'):
                print('1. thay doi dap an cau hien tai.')

                print('2. show n cau sai nhieu nhat')
                print('3. xuat ra n cau co ti le (sai - dung) > 0.')
                print('developing... coming soon')
                continue

            if (ques.check(userChoose)):
                print("congratulations")
                ques.right()
            else:
                print("you choose {} is not answer, right answer is {}".format(
                    userChoose, ques.getInfoAnswer()))
                input()
                ques.wrong()

    def save(self, path='out-studyed.txt'):
        print("i'm storing...")
        try:
            with open(path, mode='w') as fo:
                self.list.sort(key=mySort)
                for e in self.list:
                    fo.write("{}\n".format(e.getInformation()))
                return True
        except Exception as e:
            return False

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

    def changeKey(self):
        newKey = str(input("please enter new key 1 2 3 4: "))
        while (not (newKey == '1' or newKey == '2' or newKey == '3' or newKey == '4')):
            newKey = str(input("enter again: "))
        self.key = newKey

    def showTitle(self):
        print("Cau hoi: {}\n".format(self.ques))

    def check(self, e):
        if (str(self.key).__eq__(str(e))):
            return True
        return False

    def right(self):
        self.cRight = int(self.cRight) + 1

    def wrong(self):
        self.cWrong = int(self.cWrong) + 1

    def getAnswer(self):
        return self.key

    def getInfoAnswer(self):
        ans = ""
        ans = self.ans1 if self.key == '1' else ans
        ans = self.ans2 if self.key == '2' else ans
        ans = self.ans3 if self.key == '3' else ans
        ans = self.ans4 if self.key == '4' else ans
        return "{}. {}".format(self.key, ans)

    def getInformation(self):
        return str(self.ques) + "\n" + str(self.ans1) + "\n" + str(self.ans2) + "\n" + str(self.ans3) + "\n" + str(self.ans4) + "\n" + str(self.key) + "\n" + str(self.cRight) + "\n" + str(self.cWrong)

    def __repr__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n".format(self.ques, self.ans1,
                                                 self.ans2, self.ans3,
                                                 self.ans4, self.key)

    def __str__(self):
        return "\nCau hoi la({}/{}): {}\n1. {}\n2. {}\n3. {}\n4. {}\n".format(self.cRight, self.cWrong,
                                                                              self.ques, self.ans1, self.ans2, self.ans3, self.ans4)
