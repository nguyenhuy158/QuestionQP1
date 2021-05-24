import os
from Manager import ManagerQuestion, Question

for i in range(1, 2):
    path = 'out{}.txt'.format(i)

    with open(path, mode='r') as f:
        lines = f.readlines()

    print(len(lines) / 8)
    countQues = int(len(lines) / 8)
    for i in range(0, 8 * (countQues - 1) + 1, 8):
        j = 0
        while lines[i][j] >= '0' and lines[i][j] <= '9' or lines[i][j] == ' ':
            j += 1
        ques = "{}. {}".format(int(i / 8 + 1), lines[i][j:])
        lines[i] = ques
        # lines[i+1] = lines[i+1] + '.' if '.' not in lines[i+1] else lines[i+1]
        # lines[i+2] = lines[i+2] + '.' if '.' not in lines[i+2] else lines[i+2]
        # lines[i+3] = lines[i+3] + '.' if '.' not in lines[i+3] else lines[i+3]
        # lines[i+4] = lines[i+4] + '.' if '.' not in lines[i+4] else lines[i+4]

    with open(path, mode='w') as f:
        for i in lines:
            f.write('{}'.format(i))
