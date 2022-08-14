student_database = {}

def add_student(admissionNumber, studentName, moduleName, score):
    global student_database
    student_database[admissionNumber] = [studentName, moduleName, score]
    return "Student added!"

def is_admission_no_exists(admin_no):
    if admin_no in student_database:
        return True
    else:
        return False
    # elif admin_no not in student_database:
    #     return "No such student found."

def is_student_db_empty(result):
    if len(result) != 0:
        return True
    else:
        return False

def update_student_name(admissionNumber, newName):
    global student_database
    student_database[admissionNumber][0] = newName
    return True

def update_module_name(admissionNumber, newModuleName):
    global student_database
    student_database[admissionNumber][1] = newModuleName
    return True

def update_student_score(admissionNumber, newScore):
    global student_database
    student_database[admissionNumber][2] = newScore
    return True

def remove_student(admin_no_remover):
    global student_database
    del student_database[admin_no_remover]
    return True

def display_all_students():
    global student_database
    for i in student_database:
            print(f"""
Admission number: {i}
Student name: {student_database[i][0]}
Module name: {student_database[i][1]}
Student name: {student_database[i][2]}
    """)

def get_student_database(admission_num):
    return f"""
Admission number: {admission_num}
Student name: {student_database[admission_num][0]}
Module name: {student_database[admission_num][1]}
Student name: {student_database[admission_num][2]}
    """

def search_by_admission_number(admissionNumber):
    search_results = {}
    search_results = (f"""
Admission number: {admissionNumber}
Student name: {student_database[admissionNumber][0]}
Module name: {student_database[admissionNumber][1]}
Student name: {student_database[admissionNumber][2]}
""")
    return search_results

def search_by_module_name(moduleName):
    search_results = {}
    search_results = {i: student_database[i] for i in student_database if student_database[i][1] == moduleName}
    return search_results

def search_by_score(score):
    search_results = {}
    search_results = {i: student_database[i] for i in student_database if score[0] <= student_database[i][2] <= score[1]}
    return search_results