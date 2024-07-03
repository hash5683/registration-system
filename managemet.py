'''management file'''
import sqlite3
from sqlite3 import Error
from student import Student

class RegisterionSystem:
    '''class for registration system'''
    def __init__(self):
        self.conn = self.create_connection('database.db')
        print()
        self.create_table()

    def create_connection(self, db_file):
        '''creating a connection'''
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite database '{db_file}'")
        except KeyError as e:
            print(e)
        return conn

    def create_table(self):
        '''creating table'''
        sql_create_students_table = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_no TEXT NOT NULL,
                degree TEXT NOT NULL,
                session INTEGER NOT NULL,
                birth TEXT NOT NULL,
                semester INTEGER NOT NULL
            );
        """
        try:
            c = self.conn.cursor()
            c.execute(sql_create_students_table)
        except Error as e:
            print(e)

    def create(self):
        '''Adding student in table'''
        while True:
            name = input('Enter student name: ').strip().upper()
            if name.isalpha():
                break
            else:
                print('Invalid name! Name should contain only alphabets.')
        roll_no = input('Enter student roll number: ').strip().upper()
        degree = input('Enter degree program: ').strip().upper()             
        while True:
            try:
                session = int(input('Enter session year: ').strip())
                break
            except ValueError:
                print('Invalid session year! Please enter a numerical value.')      
        birth = input('Enter student birth date: ').strip()      
        while True:
            try:
                semester = int(input('Enter semester: ').strip())
                break
            except ValueError:
                print('Invalid semester! Please enter a numerical value.')
        student_data = (name, roll_no, degree, session, birth, semester)
        sql = ''' INSERT INTO students(name, roll_no, degree, session, birth, semester)
                  VALUES(?,?,?,?,?,?) '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, student_data)
            self.conn.commit()
            print('Student added successfully! \n')
        except Error as e:
            print(e)

    def retrieve(self):
        '''Retrieving student from table'''
        roll_nu = input('Enter student roll number: ').strip().upper()
        sql = "SELECT * FROM students WHERE roll_no = ?"
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (roll_nu,))
            row = cur.fetchall()
            for r in row:
                print(r)
                break
            else:
                print('Student not found! \n')
        except Error as e:
            print(e)

    def delete(self):
        '''Deleting student from table'''
        roll_nu = input('Enter student roll number: ').strip().upper()
        sql = "DELETE FROM students WHERE roll_no =?"
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (roll_nu,))
            self.conn.commit()
            print('Student deleted successfully! \n')
        except Error as e:
            print(e)

    def update(self):
        '''Updating student name'''
        roll_nu = input('Enter student roll number: ').strip().upper()
        name = input('Enter student name: ').strip().upper()
        sql = "UPDATE students SET name =? WHERE roll_no =?"
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (name, roll_nu))
            self.conn.commit()
            print('Student name updated successfully! \n')
        except Error as e:
            print(e)
    def main(self):
        '''main function'''
        print('Select an option \n')
        while True:
            print('PRESS 1 TO REGISTER A STUDENT : ')
            print('PRESS 2 TO RETRIEVE STUDENT DETAILS : ')
            print('PRESS 3 TO DELETE A STUDENT : ')
            print('PRESS 4 TO UPDATE STUDENT NAME : ')
            print('PRESS 5 TO EXIT THE PROGRAM : '+'\n')

            try:
                choice = int(input('Enter your choice: ').strip())
                if   choice == 1:
                    self.create()
                elif choice == 2:
                    self.retrieve()
                elif choice == 3:
                    self.delete()
                elif choice == 4:
                    self.update()
                elif choice == 5:
                    print('Exiting the program.')
                    break
                else:
                    print('Invalid choice! Please enter a number from 1 to 5.')
            except ValueError:
                print('Invalid input! Please enter a number.')

        self.conn.close()
