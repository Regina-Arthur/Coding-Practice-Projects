#Greet users and ask for intent to use the system
print("==========WELCOME TO MY PROGRAM==========")
print ('Welcome, you can enter student grades for your course.')
start_confirmation = input ('Would you like to enter student grades?(yes/no)\n')

#confirm intent to use the system
if start_confirmation.upper() == "YES":

    course = input("Please enter the course name: ")
    number_students = int(input("How many students will you be entering? "))
    print("""Please enter the student name, you will later be asked to enter their grade. 
            This will be done one after the other until all student information has been entered.
            Do not worry about errors, you will be allowed to correct that later.""")
    
    student_name_grade = {}
    for students in range(number_students):
        student = input("Enter a student's name please: ")
        student_name_grade[student] = int(input("Please enter their grade: "))
    print("==========Student And Grade==========")
    for student, grade in student_name_grade.items():
        print("Student name:", student, "\nStudent grade:", grade)

    change_needed = input("Is there any error in the entries:\n")
    if change_needed.upper() == "YES":
        change_in_names = input("Is there an error in the student name? ")
        if change_in_names.upper() == "YES":
            print("These are all of the name.")
            for student in student_name_grade.items():
                print("Student name:", student)
            nameChange_approval = input("Shall we begin(Yes or No): ")
            while nameChange_approval.upper() == "YES":
                studentName_toChange = input("Please enter the wrong student name:\n")
                student_grade = student_name_grade[studentName_toChange]
                studentCorrectName = input("Please enter the correct name:\n")
                student_name_grade[studentCorrectName] = student_grade
                print(student_name_grade)
                nameChange_approval = input("Do you want to change another name? YES or NO \n")

        change_in_grades = input("Is there an error in the grade:\n")
        if change_in_grades.upper() == "YES":
            print("These are all of the name and grades.")
            for student, grade in student_name_grade.items():
                print("Student name:", student, "student grade:", grade)
            gradeChange_approval = input("Shall we begin(Yes or No): ")
            while gradeChange_approval.upper() == "YES":
                studentName_forChange = input("Please enter the student name:\n")
                student_name_grade[studentName_forChange] = int(input("Please enter the correct grade:"))
                print(student_name_grade)
                gradeChange_approval = input("Do you want to change another grade? YES or NO \n")

#Calculate grade index for the score
    grade_index = []
    for grade in student_name_grade.values():
        if grade <= 40:
            grade_index.append("F")

        elif 40 <= grade < 50:
            grade_index.append("D")

        elif 50 <= grade < 60:
            grade_index.append("C")

        elif 60 <= grade < 70:
            grade_index.append("B")
        
        else:
            grade_index.append("A")

elif start_confirmation.upper() == "NO":
    print("We will be here when you need us.")

else:
    print("Please enter a valid prompt.")

#Calculation of class average
student_names = []
student_grades = []
total_grade = 0
count = 0
for student, grade in student_name_grade.items():
    student_names.append(student)
    student_grades.append(grade)
    total_grade += grade
    count += 1

average_grade = total_grade / count

#Display table of student data
print(f"{'Student Data Table':^45}")
print(f"{'STUDENT NAME':<15} {'GRADE':<15} {'GRADE INDEX':<15}")

for name, grade, index in zip(student_names,student_grades,grade_index):
    print(f"{name:<15} {grade:<15} {index:<15}")

 
#Display class average
print("Class average:",average_grade)