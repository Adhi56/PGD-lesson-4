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
