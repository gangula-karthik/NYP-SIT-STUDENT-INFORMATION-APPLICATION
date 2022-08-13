# name = Karthik Gangula
# admission number = 223715y


# Main menu 
# No students in the system then print("There is no student information in the system currently")
# When function finishes executing then the program comes back to this menu


from student_functions import *


def mainMenu():
    print("***** Welcome to SIT Mini Student Information System *****")
    print(f"Number of students in the system: {len(studentDatabase)}")
    print("""
These are the functions available:
Enter 1 to Add a new student
Enter 2 to Update an existing student info 
Enter 3 to Remove an existing student info 
Enter 4 to Display all student information in the system 
Enter 5 to Search for the student(s)
Enter -1 to Exit the application 
    """)
gfdohi
while True:

    mainMenu()

    choice = int(input("Enter your Choice: "))

    if choice == 1: 
        print("== Add a new student ==")
        admissionNumber = input("Please enter the admission number: ")
        studentName = input("Please enter the student name: ")
        moduleName = input("Please enter the module name: ")
        score = float(input("Please enter the score: "))
        
        print(addStudent(admissionNumber, studentName, moduleName, score))
    
    elif choice == 2: 
        print("== Update student ==")
        admin_No_Updater = input("Please enter the admission number of the student you would like to update: ")
        if updateStudent(admin_No_Updater) != None:
            print(updateStudent(admin_No_Updater))


    elif choice == 3: 
        print("== Remove student ==")
        admin_no_remover = input("Please enter the admission number you would like to remove: ")

        print(removeStudent(admin_no_remover))


    elif choice == 4:
        print("== Display all students ==")
        getStudents(studentDatabase)
    
    elif choice == 5:
        print("== Search Student ==")
        print("""
        Search By:
        Enter 1 to search by Admission number
        Enter 2 to seach by module Name 
        Enter 3 to search by Score range
        Enter 0 to return to main menu
        """)
        searchChoice = int(input("Your choice: "))
        searchStudent(searchChoice)


    elif choice == -1: 
        break


