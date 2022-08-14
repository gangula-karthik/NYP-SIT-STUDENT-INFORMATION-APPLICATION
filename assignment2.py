# name = Karthik Gangula
# admission number = 223715y


# Main menu 
# No students in the system then print("There is no student information in the system currently")
# When function finishes executing then the program comes back to this menu

from student_functions import *


def mainMenu():
    print("***** Welcome to SIT Mini Student Information System *****")
    print(f"Number of students in the system: {len(student_database)}")
    print("""
These are the functions available:
Enter 1 to Add a new student
Enter 2 to Update an existing student info 
Enter 3 to Remove an existing student info 
Enter 4 to Display all student information in the system 
Enter 5 to Search for the student(s)
Enter -1 to Exit the application 
    """)

def searchMenu():
    global searchChoice
    print("== Search Student ==")
    print("""
Search By:
Enter 1 to search by Admission number
Enter 2 to seach by module Name 
Enter 3 to search by Score range
Enter 0 to return to main menu
    """)
    searchChoice = int(input("Your choice: "))


while True:

    mainMenu()

    choice = int(input("Enter your Choice: "))

    if choice == 1: 
        print("== Add a new student ==")
        admissionNumber = input("Please enter the admission number: ")
        studentName = input("Please enter the student name: ")
        moduleName = input("Please enter the module name: ")
        score = float(input("Please enter the score: "))

        if is_admission_no_exists(admissionNumber):
            print("Student already exists in the system")
        else: 
            print(add_student(admissionNumber, studentName, moduleName, score))
    
    elif choice == 2: 
        print("== Update student ==")
        admin_No_Updater = input("Please enter the admission number of the student you would like to update: ")

        if is_admission_no_exists(admin_No_Updater) == True:
            print(get_student_database(admin_No_Updater))
            print("Student exists !")
            print("""
Enter 1 to Update name
Enter 2 to Update module name
Enter 3 to Update score
Enter 0 to return to main menu 
            """)
            updater = int(input("What would you like to update? "))
            if updater == 1: 
                newName = input("Please enter the new name: ")
                if update_student_name(admin_No_Updater, newName) == True: 
                    print(f"Student name updated")
                else: 
                    print("Student name not updated")
            elif updater == 2: 
                newModuleName = input("Please enter the new module name: ")
                if update_module_name(admin_No_Updater, newModuleName) == True: 
                    print(f"Module name updated")
                else: 
                    print("Module name not updated")
            elif updater == 3:
                newScore = float(input("Please enter the new score: "))
                if update_student_score(admin_No_Updater, newScore) == True: 
                    print(f"Score updated")
                else: 
                    print("Score not updated")
            elif updater == 0: 
                continue
        else:
            print("Student does not exist in the system")
            continue


    elif choice == 3: 
        print("== Remove student ==")
        admin_no_remover = input("Please enter the admission number you would like to remove: ")
        if is_admission_no_exists(admin_no_remover) == True:
            print(get_student_database(admin_no_remover))
        else:
            print("Student does not exist")

        remove_confirmation = input("Is this the student you want to remove? (Yes/No): ")
        if remove_confirmation.lower() == "yes": 
            if remove_student(admin_no_remover) == True: 
                print("Student removed")
            else: 
                print("Student not removed")
        elif remove_confirmation.lower() == "no": 
            print("Student info was not removed!")



    elif choice == 4:
        print("== Display all students ==")
        display_all_students()
    
    elif choice == 5:
        searchMenu()
        if is_student_db_empty(student_database) == True:
            if searchChoice == 1: 
                admissionNumber = input("Please enter the admission number you wish to search by: ")
                if is_admission_no_exists(admissionNumber) == True:
                    print(search_by_admission_number(admissionNumber))
                searchMenu()
            elif searchChoice == 2: 
                moduleName = input("Please enter the module name you wish to search by: ")
                result = search_by_module_name(moduleName)
                if is_student_db_empty(result) == True:
                    for i in result: 
                        print(f"Admission number: {i}")
                        print(f"Student name: {result[i][0]}")
                        print(f"Module name: {result[i][1]}")
                        print(f"Score name: {result[i][2]}")
                searchMenu()
            elif searchChoice == 3: 
                min_score = int(input("Minimum score: "))
                max_score = int(input("Maximum score: "))
                print()
                scoreLst = [min_score, max_score]
                result = search_by_score(scoreLst)
                if is_student_db_empty(result) == True:
                    for i in result: 
                        print(f"Admission number: {i}")
                        print(f"Student name: {result[i][0]}")
                        print(f"Module name: {result[i][1]}")
                        print(f"Score name: {result[i][2]}\n")
                searchMenu()
            elif searchChoice == 0: 
                break
        else:
            print("There is no student information in the system currently")
            continue

    elif choice == -1: 
        break

