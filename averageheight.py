students = input("enter height of students\n").split()
for n in range(0,len(students)):
    students[n] = int(students[n])
print(students)


sum = 0
for i in students:
    sum += i
print(sum)

length = 0 
for j in students:
    length+=1
print(length)

avgheight = round(sum/length)
print(avgheight)
