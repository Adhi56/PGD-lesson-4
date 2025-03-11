people=["Adhi","William","Ted","Jaden"]
print(people)

#Acess list values using index(that starts with 0)
print(people[2])
print(people[-4])

#see how many values there are in a list
print(len(people))

#append only adds value to the end of a list
people.append("Jim")
print(people)

#adds people anywhere in a list
people.insert(3,"Bob")
print(people)

#remove values from the end of list
people.pop()
print(people)

#removes values anywhere on a list
people.pop(1)
print(people)

#2D List
matrix=[[3,1,4],[5,2,6],[4,2,9]]
print(matrix)

#Number of rows
print("Number of rows :",len(matrix))

#Number of column
print("Number of columns :",len(matrix[0]))

print(matrix[0][1])
print(matrix[1][0])
print(matrix[0][2])

#Print a 2D list in Matrix format
for i in range(3):
    for g in range(3):
        print(matrix[i][g],end=" ")
    print("\n") # makes new line

rows=int(input("How many rows should there be in the matrix? \n"))
cols=int(input("How many columns should there be in the matrix? \n"))

matrix2=[]
for a in range(rows):
    temp=[]
    for b in range(cols):
        x=int(input("What should the elements inside the matrix be?"))
        temp.append(x)
    matrix2.append(temp)

print(matrix2)

for c in range(rows):
    for d in range(cols):
        print(matrix2[c][d],end=" ")
    print("\n")

n=int(input("What are the dimensions of the matrix? \n"))

matrix3=[]
for i in range(n):
    tempory=[]
    for j in range(n):
        w=int(input("What are the elements inside the matrix?? \n"))
        tempory.append(w)
    matrix3.append(tempory)

print(matrix3)

for i in range(n):
    for q in range(n):
        print(matrix3[i][q],end=" ") 
    print("\n")

#printing diagonal elements

for i in range(n):
    print(matrix3[i][i])

matrixA=[[1,3,2],[2,5,2]]
matrixB=[[6,9,5],[1,7,4]]
matrixAb=[[0,0,0],[0,0,0]]

for i in range(2):
    for f in range(3):
        matrixAb[i][f]=matrixA[i][f]+matrixB[i][f]

print(matrixAb)

for i in range(2):
    for d in range(3):
        print(matrixAb[i][d],end=" ")
    print("\n")

matrixC=[[5,8,9],[7,9,10]]
matrixD=[[1,4,6],[3,2,9]]
matrixCD=[[0,0,0],[0,0,0]]

for i in range(2):
    for w in range(3):
        matrixCD[i][w]=matrixC[i][w]-matrixD[i][w]

print(matrixCD)



