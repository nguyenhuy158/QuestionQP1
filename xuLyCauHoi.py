import os
from Manager import ManagerQuestion, Question


# remove 'empty row' and '\n'
def removeNewline(sources):
    # remove line 'empty'
    for element in sources:
        if element == '\n' or len(element) <= 1 or element == '':
            sources.remove(element)

    for element in sources:
        if element == '\n' or len(element) <= 1 or element == '':
            sources.remove(element)
    # remove char '\n' if it exists
    for index in range(len(sources)):
        sources[index] = sources[index].replace('\n', '')
    return sources


# read data form file, handing
# return ManagerQuestion
def inputAndHanding(path, pathSave=''):
    try:
        file = open(path, mode='r')
        lines = file.readlines()
        lines = removeNewline(lines)
        countQues = int(len(lines) / 5)
        managerQuestion = ManagerQuestion()
        for i in range(0, 5 * (countQues - 1) + 1, 5):
            # remove 'x' and get right answer
            ans = str(input("enter key {} - {}: ".format(i, lines[i])))
            # ans = ''
            key1 = ''
            key1 = lines[i + 1] if 'A. ' in lines[i + 1] else key1
            key1 = lines[i + 2] if 'A. ' in lines[i + 2] else key1
            key1 = lines[i + 3] if 'A. ' in lines[i + 3] else key1
            key1 = lines[i + 4] if 'A. ' in lines[i + 4] else key1

            key2 = ''
            key2 = lines[i + 1] if 'B. ' in lines[i + 1] else key2
            key2 = lines[i + 2] if 'B. ' in lines[i + 2] else key2
            key2 = lines[i + 3] if 'B. ' in lines[i + 3] else key2
            key2 = lines[i + 4] if 'B. ' in lines[i + 4] else key2

            key3 = ''
            key3 = lines[i + 1] if 'C. ' in lines[i + 1] else key3
            key3 = lines[i + 2] if 'C. ' in lines[i + 2] else key3
            key3 = lines[i + 3] if 'C. ' in lines[i + 3] else key3
            key3 = lines[i + 4] if 'C. ' in lines[i + 4] else key3

            key4 = ''
            key4 = lines[i + 1] if 'D. ' in lines[i + 1] else key4
            key4 = lines[i + 2] if 'D. ' in lines[i + 2] else key4
            key4 = lines[i + 3] if 'D. ' in lines[i + 3] else key4
            key4 = lines[i + 4] if 'D. ' in lines[i + 4] else key4
            ques = Question(ques=lines[i],
                            ans1=key1,
                            ans2=key2,
                            ans3=key3,
                            ans4=key4,
                            key=ans)
            managerQuestion.addQuestion(ques)
        file.close()
        print(len(lines))
        # for i in range(len(lines)):
        #     print("{} '{}'".format(i, lines[i]))
    except Exception as e:
        print(str(e))
        return None
    # after done
    return managerQuestion


if __name__ == '__main__':
    pathOut = 'out11.txt'
    # path = input("enter file name: ")
    path = 'ppbai11.txt'
    if os.path.isfile(path):
        manager = inputAndHanding(path)
        print('i have {} question'.format(manager.count))
        print("i'm storing...")
        if (manager.save(pathOut)):
            print('success. Now you can run "study.py"')
        else:
            print('fail. try again.')
    else:
        print("sorry i can't found file. please run again.")
