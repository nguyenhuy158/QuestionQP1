import re


# remove 'empty row' and '\n'
def removeNewline(sources):
    # remove char '\n' if it exists
    for index in range(len(sources)):
        sources[index] = sources[index].replace('\n', '')
    # remove line 'empty'
    for element in sources:
        if element == '\n' or len(element) <= 1:
            sources.remove(element)
    return sources


for index in range(1, 2):
    path = 'o-bai{}.txt'.format(index)
    with open(path, mode='r') as fi:
        lines = fi.readlines()
        lines = removeNewline(lines)
        out = '\n'.join(lines)
        while out.find('  '):
            out = out.replace('  ', ' ')
        print(out)

    # with open('o-{}'.format(path), mode='r') as fi:
    #     lines = fi.readlines()
    #     for i in range(len(lines)):
    #         lines[i] = lines[i].replace('\s+', '\n')

    # with open('o-{}'.format(path), mode='w') as fo:
    #     for e in lines:
    #         fo.write(re.sub('\s{2,}', '\n', e))

    # with open('o-{}'.format(path), mode='r') as fi:
    #     lines = fi.readlines()

    # with open('o-{}'.format(path), mode='w') as fo:
    #     for l in lines:
    #         if not("CÂU" in l or (l[1:2] in ["0", "1", "2", "3", "4", '6', '5', '7', '8', '9']) or "" in l) and len(l) > 1:
    #             fo.write('{}\n'.format(l))

    # with open('o-{}'.format(path), mode='r') as fi:
    #     lines = fi.readlines()
    #     lines = removeNewline(lines)

    # with open('o-{}'.format(path), mode='w') as fo:
    #     ques = ''
    #     for l in lines:
    #         if 'A. ' in l or 'B. ' in l or 'C. ' in l or 'D. ' in l:
    #             if len(ques) > 1:
    #                 fo.write('{}\n'.format(ques.replace('\n', '')))
    #                 ques = ''
    #             fo.write('{}\n'.format(l))
    #         else:
    #             ques += ' ' + l
