from random import randint

marks=[]
listA=[]
listB=[]
listC=[]

for i in range(20):
    marks.append(randint(0,100))

for i in range(20):
    if marks[i] <=30:
        listA.append(marks[i])
    elif 31 <= marks[i] <= 69:
        listB.append(marks[i])
    else:
        listC.append(marks[i])
print(marks)
print(listA)
print(listB)
print(listC)

