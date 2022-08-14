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
        if isAdminExists(admin_No_Updater) == True:
            print(f"Admission number: {admin_No_Updater}")
            print(f"Student name: {studentDatabase[admin_No_Updater][0]}")
            print(f"Module name: {studentDatabase[admin_No_Updater][1]}")
            print(f"score: {studentDatabase[admin_No_Updater][2]}")
            print("Student exists !")
            print("""
Enter 1 to Update name
Enter 2 to Update module name
Enter 3 to Update score
Enter 0 to return to main menu 
            """)
            updater = int(input("What would you like to update? "))
            print(updateStudent(admin_No_Updater, updater))
        else:
            print(isAdminExists(admin_No_Updater))


    elif choice == 3: 
        print("== Remove student ==")
        admin_no_remover = input("Please enter the admission number you would like to remove: ")
        if isAdminExists(admin_no_remover) == True:
            print(f"Admission number: {admin_no_remover}")
            print(f"Student name: {studentDatabase[admin_no_remover][0]}")
            print(f"Module name: {studentDatabase[admin_no_remover][1]}")
            print(f"score: {studentDatabase[admin_no_remover][2]}")

        remove_confirmation = input("Is this the student you want to remove? (Yes/No): ")

        print(removeStudent(admin_no_remover, remove_confirmation))


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


        if searchChoice == 1: 
            admissionNumber = input("Please enter the admission number you wish to search by: ")
            print(searchData(searchChoice, admissionNumber))
        elif searchChoice == 2: 
            moduleName = input("Please enter the module name you wish to search by: ")
            print(searchData(searchChoice, moduleName))
        elif searchChoice == 3: 
            min_score = int(input("Minimum score: "))
            max_score = int(input("Maximum score: "))
            scoreLst = [min_score, max_score]
            print(searchData(searchChoice, scoreLst))
        elif searchChoice == 0: 
            print("")

        
        # if searchChoice == 1: 
        #     admin_no_searcher = input("Please enter the admission number you wish to search by: ")
        #     if adminExists(admin_no_searcher) == True: 
        #         print(f"Admission Number: {admin_no_searcher}")
        #         print(f"Student Name: {studentDatabase[admin_no_searcher][0]}")
        #         print(f"Module Name: {studentDatabase[admin_no_searcher][1]}")
        #         print(f"score: {studentDatabase[admin_no_searcher][2]}")
        #     elif adminExists(admin_no_searcher) != True: 
        #         print("No student with this Admission number was found")

                
        # elif searchChoice == 2: 
        #     module_name_searcher = input("Please enter the module name you wish to search by: ")
        #     searchModule(module_name_searcher)


    elif choice == -1: 
        break

