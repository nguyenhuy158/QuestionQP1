import random


def inputInt(content):
    while True:
        try:
            choose = int(input(content))
            return choose
        except Exception as e:
            print('enter again!')


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

    def study(self):
        # title game
        print("==>Welcome to my Study<==")

        numberAnswered = 0
        while True:
            self.sort()
            # random choice in 1/3 question first in list
            # because they are question you is wrong
            ques = random.choice(self.list[0:int(self.count / 3)])
            print(ques)

            # user choose
            userChoose = str(
                input("[{}/{}] enter 1 2 3 4 or cancel(c) offer(o): ".format(numberAnswered, self.count)))
            while (userChoose == ''
                   or not (userChoose == '1' or userChoose == '2'
                           or userChoose == '3' or userChoose == '4' or userChoose == 'c' or userChoose == 'o')):
                userChoose = str(input("enter again: "))

            # offer
            if (userChoose == 'o'):
                print('1. thay doi dap an cau hien tai.')
                print('2. show n cau sai nhieu nhat.')
                print('3. xuat ra n cau co ti le (sai - dung) > 0.')

                # choose offer
                choose = inputInt('enter offer: ')
                if choose == 1:
                    ques.setKey()
                elif choose == 2:
                    nQuestion = inputInt('enter n = ')
                    while nQuestion < 0 or nQuestion >= self.count:
                        nQuestion = inputInt()
                    mostWrongs = self.getQuestionMostWrongs(nQuestion)
                    pathMostWrong = input("enter path to store: ")
                    self.write(mostWrongs, pathMostWrong)
                elif choose == 3:
                    pass
                else:
                    print("developing... coming soon")
                continue

            # cancel
            if (userChoose == 'c'):
                break

            # 1 2 3 4
            if (ques.check(userChoose)):
                print("congratulations")
                ques.right()
            else:
                print("you choose {} is not answer, {}".format(
                    userChoose, ques.getKey()))
                input()
                ques.wrong()
            numberAnswered += 1

    def write(self, source, path='out-studyed.txt'):
        print("i'm storing...")
        try:
            with open(path, mode='w') as fo:
                for e in source:
                    fo.write("{}\n".format(e.getInformation()))
                return True
        except Exception as e:
            return False

    def save(self, path='out-studyed.txt'):
        print("i'm storing...")
        try:
            with open(path, mode='w') as fo:
                self.sort()
                for e in self.list:
                    fo.write("{}\n".format(e.getInformation()))
                return True
        except Exception as e:
            return False

    def sort(self):
        self.list.sort(key=lambda e: (
            str(e.cWrong), str(e.cRight)), reverse=True)

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
