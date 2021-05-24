import os
from Manager import ManagerQuestion, Question


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
        file = open(path, mode='r')
        lines = file.readlines()
        lines = removeNewline(lines)

        countQues = int(len(lines) / 8)
        input("we have {} question.".format(countQues))

        managerQuestion = ManagerQuestion()
        for i in range(0, 8 * (countQues - 1) + 1, 8):
            ques = Question(ques=lines[i],
                            ans1=lines[i + 1],
                            ans2=lines[i + 2],
                            ans3=lines[i + 3],
                            ans4=lines[i + 4],
                            key=lines[i+5],
                            cRight=lines[i+6],
                            cWrong=lines[i+7])
            managerQuestion.addQuestion(ques)
        file.close()
    except Exception as e:
        print(str(e))
        return None
    return managerQuestion


if __name__ == '__main__':
    path = input("enter path: ")
    if os.path.isfile(path):
        manager = inputStudyed(path)
        if manager != None:
            manager.study()
        if manager.save(path):
            print('see yah')
        else:
            print('error. all answer is not save')
    else:
        print("please run xuLyCauHoi.py first")
