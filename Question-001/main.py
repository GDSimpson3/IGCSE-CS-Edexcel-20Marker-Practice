

maxStudents = 5
maxQuizes = 3
studentCount = 0
quizCount= 0




studentData = [
#    ["Bob",1,34,1000],
#    ["Jack",1,34,98],
]

while studentCount < maxStudents:
    studentCount = studentCount +1
    student = []
    studentName = str(input("Please enter the Students Name: "))
    if studentName == "":
        break
    else: 
        student.append(studentName)
        while quizCount < maxQuizes:
            quizCount = quizCount + 1
            try: 
                quizScore = int(input(f"Please enter {studentName}'s Quiz scores ({quizCount}/{maxQuizes}): ") )

                while (quizScore >= 100 or quizScore <= 0): # Here we check for the range of scores
                    quizScore = int(input(f"Please enter a score that's in the range of 0 and 100 for {studentName}'s Quiz scores ({quizCount}/{maxQuizes}): "))
            except (ValueError):   # If theres a value error - IE: it's not an int, we break the loop assuming that there are no more scores to enter
                break
                   
            else:
                student.append(quizScore)
        quizCount = 0
        if not len(student) == 1:
            studentData.append(student)



if studentCount >= maxStudents: print(f"Max students reached ({maxStudents})")


# Calculate Averages
studentAverages = []

highestAverage = [0,0.0] # [index, average]

index = 0

for student in studentData:
    
    average = 0
    for i in range(1,len(student)): # this loop gos through the score
        # print(student[i])
        average = average + student[i]

    if (average/(len(student) -1)) > highestAverage[1]:
        highestAverage = [index, average/(len(student) -1)]
    studentAverages.append(average/(len(student) -1))

    index = index + 1

print (studentAverages)
print(studentData)

print(highestAverage)

print("List of all students & their Scores!!!")
internalcount = 0


for student in studentData:
    print(f"Score for {student[0]}: ")
    for i in range(1, len(student)):
        print(f"- {student[i]}")
    print(f"Average for {student[0]}: {studentAverages[internalcount]}")

    internalcount = internalcount + 1


print("Highest Average==== ")

print(f"{studentData[highestAverage[0]][0]} Got the highest average with {highestAverage[1]}")