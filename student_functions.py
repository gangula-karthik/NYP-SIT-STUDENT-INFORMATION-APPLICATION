import sys 

studentDatabase = {}

def addStudent(admissionNumber, studentName, moduleName, score):
    global studentDatabase
    studentDatabase[admissionNumber] = [studentName, moduleName, score]
    return "Student added!"

def isAdminExists(admin_no):
    if admin_no in studentDatabase:
        return True
    elif admin_no not in studentDatabase:
        return "No such student found."

def isStudenDBEmpty():
    if len(studentDatabase) != 0:
        return True

def updateStudent(admin_No_Updater, updater):
    global studentDatabase
    if isStudenDBEmpty():
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


def removeStudent(admin_no_remover, remove_student):
    global studentDatabase
    if remove_student.lower() == "yes":
        del studentDatabase[admin_no_remover]
        return "student information removed!"
    elif remove_student.lower() == "no":
        return "student information was not removed!"


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

def searchData(id, value):
    searchresults = {}
    if id == 1:
        searchresults = (f"""
Admission number: {value}
Student name: {studentDatabase[value][0]}
Module name: {studentDatabase[value][1]}
Student name: {studentDatabase[value][2]}
""")
        return searchresults
    elif id == 2: 
        searchresults = {i: studentDatabase[i] for i in studentDatabase if studentDatabase[i][1] == value}
        return searchresults

    elif id == 3: 
        searchresults = {i: studentDatabase[i] for i in studentDatabase if value[0] <= studentDatabase[i][2] <= value[1]}
        return searchresults

    elif id == 0:
        return None

    else: 
        return "Invalid input"






# module_searcher = input("Please enter the module name you wish to search by: ")
# def searchModule(module):
#     module_lst = [i for i in studentDatabase if studentDatabase[i][1] == module]
#     if len(module_lst) != 0:
#         for i in studentDatabase:
#             print()
#             if studentDatabase[i][1] == module:
#                 print(f"Admission number: {i}")
#                 print(f"Student name: {studentDatabase[i][0]}")
#                 print(f"Module name: {studentDatabase[i][1]}")
#                 print(f"score: {studentDatabase[i][2]}")
#     else:
#         print("No student with this module name was found")
#     print()
# searchModule(module_searcher)


    # elif searchChoice == 3: 
    #     print("Please enter the range of score you wish to search by: ")
    #     min_score = int(input("Minimum score: "))
    #     max_score = int(input("Maximum score: "))

    #     def searchScore(min_score, max_score):
    #         score_lst = [i for i in studentDatabase if min_score <= studentDatabase[i][2] <= max_score]
    #         if len(score_lst) != 0:
    #             for i in studentDatabase:
    #                 print()
    #                 if min_score <= studentDatabase[i][2] <= max_score:
    #                     print(f"Admission number: {i}")
    #                     print(f"Student name: {studentDatabase[i][0]}")
    #                     print(f"Module name: {studentDatabase[i][1]}")
    #                     print(f"score: {studentDatabase[i][2]}")
    #         else:
    #             print("No student with this score was found")
    #         print()

    #     searchScore(min_score, max_score)

    # elif searchChoice == 0:
    #     return None