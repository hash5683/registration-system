'''student file'''
class Student:
    '''student class'''
    def __init__(self, name, roll_no, degree, session, birth, semester):
        self.name = name
        self.roll_no = roll_no
        self.degree = degree
        self.session = session
        self.birth = birth
        self.semester = semester

    def print_student_details(self, student):
        ''' Print the details of a student'''
        print(f"Name        | {student.name}")
        print(f"Roll Number | {student.roll_no}")
        print(f"Degree      | {student.degree}")
        print(f"Session     | {student.session}")
        print(f"Birthdate   | {student.birth}")
        print(f"Semester    | {student.semester}/n")
