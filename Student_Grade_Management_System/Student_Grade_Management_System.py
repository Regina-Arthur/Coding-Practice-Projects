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

    error_check = input("Is there any error in the entries: \n ")
    if error_check.upper == "YES":
        error_in_name = input("Is there an error in the student name? ")
        if error_in_name.upper == "YES":
            print("These are all of the name.")
            for student, grade in student_name_grade:
                print("Student name:", student)
            key = input("Shall we begin(Yes or No): ")
            while key.upper == "YES":
                print("we shall continue this later")

        error_in_grade = input("Is there an error in the grade")
        if error_in_name.upper == "YES":
            print("These are all of the name and grades.")
            for student,grade in student_name_grade:
                print("Student name:", student, "student grade:", grade)
            key = input("Shall we begin(Yes or No): ")
            while key.upper == "YES":
                print("we shall continue this later")

    grade_index = []
    for student, grade in student_name_grade:
        if grade < 40:
            grade_index.append("F")

        elif 40 <= grade < 50:
            grade_index.append("D")

        elif 50 <= grade < 60:
            grade_index.append("C")

        elif 60 <= grade < 70:
            grade_index.append("B")
        
        else:
            grade_index.append("A")
    
    else:
        print("Then let's continue: ")

elif start_confirmation.upper() == "NO":
    print("We will be here when you need us.")

else:
    print("Please enter a valid prompt.")

#Calculate grade for the score

#Store student record in the list

#Data entry and calculation of class average

#Display table of student data
 
#Display class average