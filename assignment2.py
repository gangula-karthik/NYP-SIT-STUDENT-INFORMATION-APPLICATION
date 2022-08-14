# name = Karthik Gangula
# admission number = 223715y


# Main menu 
# No students in the system then print("There is no student information in the system currently")
# When function finishes executing then the program comes back to this menu

# used exception handling for the program 
# used list comprehension for the program
# used dictionary comprehension for the program

from student_functions import *


def show_main_menu():
    global choice
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
    try: 
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Please enter a valid choice\n")
        show_main_menu()
    else: 
        if choice not in [1, 2, 3, 4, 5, -1]:
            print("Please enter a valid choice\n")
            show_main_menu()

def show_update_menu():
    print("""
Enter 1 to Update name
Enter 2 to Update module name
Enter 3 to Update score
Enter 0 to return to main menu 
        """)

def searchMenu():
    print("== Search Student ==")
    print("""
Search By:
Enter 1 to search by Admission number
Enter 2 to seach by module Name 
Enter 3 to search by Score range
Enter 0 to return to main menu
    """)

def is_score_valid(score):
    if score is None:
        return False
    else:
        return True if 100 >= score >= 0 else False

while True:

    show_main_menu()

    # if choice =1, Add a new student'''
    if choice == 1: 
        print("== Add a new student ==")
        admission_number = input("Please enter the admission number: ")

        # check if admission number is valid
        if admission_number is None:
            print("Please enter a valid admission number\n")
            continue
        
        # check if admission number already exists in the system
        if is_admission_no_exists(admission_number):
            print("Student already exists in the system\n")
            continue

        admission_number = admission_number.upper()

        # check if student is valid
        student_name = input("Please enter the student name: ")
        if student_name is None:
            print("Please enter a valid student name\n")
            continue

        student_name = student_name.title()
        
        # check if module name is valid
        module_name = input("Please enter the module name: ")
        if module_name is None:
            print("Please enter a valid student name\n")
            continue

        module_name = module_name.title()
            
        # check if score is valid
        score = float(input("Please enter the score: "))
        if is_score_valid(score) == True: 
            print(add_student(admission_number, student_name, module_name, score))
        else:
            print("Please enter a valid score\n")
            continue

    # if choice = 2, Update an existing student info
    elif choice == 2: 
        print("== Update student ==")
        
        if is_student_db_empty(student_database) == False:
            print("There are no students in the system currently, please add a student before updating\n")
            continue

        while True: 
            admission_number = input("Please enter the admission number of the student you would like to update: ")
            admission_number = admission_number.upper()

            # check if admission number already exists in the system
            if is_admission_no_exists(admission_number) == True:
                print(get_student_database(admission_number))
                print("Student exists !")
                show_update_menu()
                try: 
                    update_choice = int(input("What would you like to update? "))
                    if update_choice > 3 or update_choice < 0:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid value\n")
                    continue

                # if update_choice = 1, Update student name
                if update_choice == 1: 
                    new_name = input("Please enter the new name: ").title()
                    if update_student_name(admission_number, new_name) == True: 
                        print(f"Student name updated")
                        break
                    else: 
                        print("Student name not updated")
                    continue

                # if update_choice = 2, Update module name
                elif update_choice == 2: 
                    new_module_name = input("Please enter the new module name: ").title()
                    if update_module_name(admission_number, new_module_name) == True: 
                        print(f"Module name updated")
                        break
                    else: 
                        print("Module name not updated")
                    continue

                # if update_choice = 3, Update score
                elif update_choice == 3:
                    new_score = float(input("Please enter the new score: "))
                    if is_score_valid(new_score) == True:
                        if update_student_score(admission_number, new_score) == True:
                            print("Score updated")
                            break
                        else:
                            print("Score not updated")
                    else:
                        print("Please enter a valid score")
                    continue

                # if update_choice = 0, return to main menu
                elif update_choice == 0: 
                    break
            else:
                print("Student does not exist in the system\n")
                continue

    # if choice = 3, Remove an existing student info
    elif choice == 3: 
        print("== Remove student ==")

        if is_student_db_empty(student_database) == False:
            print("There are no students in the system currently, please add a student before removing\n")
            continue

        admission_number = input("Please enter the admission number you would like to remove: ").upper()

        # check if admission number already exists in the system
        if is_admission_no_exists(admission_number) == True:
            print(get_student_database(admission_number))
        else:
            print("Student does not exist\n")
            continue

        remove_confirmation = input("Is this the student you want to remove? (Yes/No): ")

        # check if user wants to remove the student
        if remove_confirmation.lower() == "yes": 
            if remove_student(admission_number) == True: 
                print("Student removed\n")
            else: 
                print("Student not removed")
        elif remove_confirmation.lower() == "no": 
            print("Student info not removed!\n")
        else: 
            print("Please enter a valid confirmation\n")

    # if choice = 4, Display all student information in the system
    elif choice == 4:
        print("== Display all students ==")

        # check if there are any students in the system
        if is_student_db_empty(student_database) == False:
            print("There are no students in the system currently\n")
        else:
            display_all_students()
    
    # if choice = 5, Search for a student
    elif choice == 5:
        if is_student_db_empty(student_database) == False:
            print("There are no students in the system currently, please add a student before searching\n")
            continue

        while True:  
            searchMenu()
            try: 
                search_choice = int(input("Enter your choice: "))
                if search_choice not in range(0,4):
                    raise ValueError
            except ValueError:
                print("Please enter a valid choice\n")
                continue

            if is_student_db_empty(student_database) == True:

                # if search_choice = 1, Search by admission number
                if search_choice == 1: 
                    admission_number = input("Please enter the admission number you wish to search by: ").upper()
                    if is_admission_no_exists(admission_number) == True:
                        print(search_by_admission_number(admission_number))
                    continue
                
                # if search_choice = 2, Search by module name
                elif search_choice == 2: 
                    module_name = input("Please enter the module name you wish to search by: ").title()
                    result = search_by_module_name(module_name.title())
                    if result == {}:
                        print("No Module found")
                    if is_student_db_empty(result) == True:
                        for i in result: 
                            print(f"Admission number: {i}")
                            print(f"Student name: {result[i][0]}")
                            print(f"Module name: {result[i][1]}")
                            print(f"Score name: {result[i][2]}\n")
                    continue

                # if search_choice = 3, Search by student name
                elif search_choice == 3: 
                    try:
                        min_score = float(input("Minimum score: "))
                        max_score = float(input("Maximum score: "))
                        if min_score is None or max_score is None:
                            raise ValueError
                        if min_score > max_score:
                            raise ValueError
                    except ValueError:
                        print("Please enter a valid min and max score\n")
                        continue

                    score_list = [min_score, max_score]
                    result = search_by_score(score_list)
                    if is_student_db_empty(result) == True:
                        for i in result: 
                            print(f"Admission number: {i}")
                            print(f"Student name: {result[i][0]}")
                            print(f"Module name: {result[i][1]}")
                            print(f"Score name: {result[i][2]}\n")
                    continue

                # if search_choice = 0, return to main menu
                elif search_choice == 0: 
                    break
            else:
                print("There is no student information in the system currently\n")
                break
    # if choice = -1, exit the program
    elif choice == -1: 
        break

