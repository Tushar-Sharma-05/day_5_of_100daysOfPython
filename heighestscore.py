marks = input("enter marks obtained by students\n").split()
for i in range(0,len(marks)):
    marks[i] = int(marks[i])

# print(max(marks))


heighest_score = 0
for j in marks:
    if j>heighest_score:
        heighest_score=j
print(heighest_score)        
