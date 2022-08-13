studentDatabase = {}

def addStudent(admissionNumber, studentName, moduleName, score):
    global studentDatabase
    studentDatabase[admissionNumber] = [studentName, moduleName, score]
    return "Student added!"


def updateStudent(admin_No_Updater):
    global studentDatabase
    if admin_No_Updater in studentDatabase: 
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
        if updater == 1: 
            new_name_student = input("Enter the new student name: ")
            studentDatabase[admin_No_Updater][0] = new_name_student
            return "Student name updated!"
        elif updater == 2: 
            new_name_module= input("Enter the new module name: ")
            studentDatabase[admin_No_Updater][1] = new_name_module
            return "Module name updated!"
        elif updater == 3:
            new_score = int(input("Enter the new score: "))
            studentDatabase[admin_No_Updater][2] = new_score
            return "Score updated!"
        elif updater == 0:
            return ""
    elif len(studentDatabase) == 0:
        return "There is nothing in the student database"
    elif admin_No_Updater not in studentDatabase:
        return "The admission number does not exist in the system"


def removeStudent(admin_no_remover):
    global studentDatabase
    if admin_no_remover in studentDatabase:
        print(f"Admission number: {admin_no_remover}")
        print(f"Student name: {studentDatabase[admin_no_remover][0]}")
        print(f"Module name: {studentDatabase[admin_no_remover][1]}")
        print(f"score: {studentDatabase[admin_no_remover][2]}")
        remove_confirmation = input("Is this the student you want to remove? (Yes/No): ")
        if remove_confirmation.lower() == "yes":
            del studentDatabase[admin_no_remover]
            return "student information removed!"
        elif remove_confirmation.lower() == "no":
            return "student information was not removed!"
    elif admin_no_remover not in studentDatabase:
        return "Student not found"


def getStudents(students):
    global studentDatabase
    if len(students) == 0:
        return "There is currently no student information in the system"
    for i in studentDatabase:
        print(f"""
Admission number: {i}
Student name: {students[i][0]}
Module name: {students[i][1]}
Student name: {students[i][2]}
""")


def searchStudent(searchChoice):
    global studentDatabase
    if searchChoice == 1:
        admin_no_searcher = input("Please enter the admission number you wish to search by: ")
        def searchAdmin(admin_no):
            if admin_no in studentDatabase: 
                print(f"Admission Number: {admin_no}")
                print(f"Student Name: {studentDatabase[admin_no][0]}")
                print(f"Module Name: {studentDatabase[admin_no][1]}")
                print(f"score: {studentDatabase[admin_no][2]}")
            elif admin_no not in studentDatabase: 
                print("No student with this Admission number was found")

        searchAdmin(admin_no_searcher)
    
    elif searchChoice == 2: 
        module_searcher = input("Please enter the module name you wish to search by: ")
        def searchModule(module):
            module_lst = [i for i in studentDatabase if studentDatabase[i][1] == module]
            if len(module_lst) != 0:
                for i in studentDatabase:
                    print()
                    if studentDatabase[i][1] == module:
                        print(f"Admission number: {i}")
                        print(f"Student name: {studentDatabase[i][0]}")
                        print(f"Module name: {studentDatabase[i][1]}")
                        print(f"score: {studentDatabase[i][2]}")
            else:
                print("No student with this module name was found")
            print()
        searchModule(module_searcher)


    elif searchChoice == 3: 
        print("Please enter the range of score you wish to search by: ")
        min_score = int(input("Minimum score: "))
        max_score = int(input("Maximum score: "))

        def searchScore(min_score, max_score):
            score_lst = [i for i in studentDatabase if min_score <= studentDatabase[i][2] <= max_score]
            if len(score_lst) != 0:
                for i in studentDatabase:
                    print()
                    if min_score <= studentDatabase[i][2] <= max_score:
                        print(f"Admission number: {i}")
                        print(f"Student name: {studentDatabase[i][0]}")
                        print(f"Module name: {studentDatabase[i][1]}")
                        print(f"score: {studentDatabase[i][2]}")
            else:
                print("No student with this score was found")
            print()

        searchScore(min_score, max_score)

    elif searchChoice == 0:
        return None