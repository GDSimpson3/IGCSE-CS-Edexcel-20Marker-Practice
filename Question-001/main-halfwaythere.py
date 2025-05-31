

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
                # if quizScore == "":
                #     quizCount = 4
                #     break
            
            # while not int(quizScore) == quizScore:
            #     if quizScore == "":
            #         quizCount = 4
            #         break
            #     quizScore = input(f"Please enter A NUMERICAL VALUE FOR {studentName}'s Quiz scores ({quizCount}/{maxQuizes}): ")

                while (quizScore >= 100 or quizScore <= 0):
                    quizScore = int(input(f"Please enter a score that's in the range of 0 and 100 for {studentName}'s Quiz scores ({quizCount}/{maxQuizes}): "))
            except (ValueError):   
                break
                   
            else:
                student.append(quizScore)
        quizCount = 0
        studentData.append(student)



if studentCount >= maxStudents: print(f"Max students reached ({maxStudents})")

print(studentData)