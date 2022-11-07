import sqlite3

def create_table():
    with sqlite3.connect("report.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS students (
            name  PRIMARY KEY NOT NULL,
            class_of_student CHAR(6) NOT NULL,
            age CHAR(3) NOT NULL,
            score INTEGER NOT NULL

        )""")
        connection.commit()

def add_student(name, class_of_student, score):
    with sqlite3.connect("report.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO students VALUES(
            ?,
            ?,
            ?
        )""", (name, class_of_student, score))

        

def clear_all_students(name):
      with sqlite3.connect("report.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""DELETE FROM students where name=?""", (name,))  



def view_all():
    with sqlite3.Connection("report.db") as connection:
        cursor = connection.cursor()
        
        the_report = cursor.execute("""SELECT * FROM students """).fetchall()
        connection.commit()
        return the_report


create_table()
# add_student("computers", "Jss1(grade7)", 50)
clear_all_students("computer")
print(view_all())
