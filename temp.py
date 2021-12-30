from typing import AnyStr


file1 = open('C:\\Users\\tejas\\Desktop\\Manas\\OLD\\Cs.txt')
str1 = file1.read()
li = str1.split('\n')
# print(li)
# exit()
questions = []
answer = []
# print(questions)
for i in range(1, 141, 7):
    temp = []
    for j in range(6):
        if j == 5:
            answer.append(li[i-1+j])
        temp.append(li[i-1+j])
    questions.append(temp)


print(questions, answer)
file1.close()
# file1 = open('C:\\Users\\tejas\\Desktop\\Manas\\OLD\\c.arr', 'w+')
