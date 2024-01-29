import sqlite3

conn = sqlite3.connect('school.db')
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

c.execute('''
    CREATE TABLE Students(
        id INTEGER PRIMARY KEY,
        name TEXT)
''')

c.execute('''
    CREATE TABLE Classes(
        id INTEGER PRIMARY KEY,
        name TEXT)
''')

c.execute('''
    CREATE TABLE Enrollment(
        student_id INTEGER,
        class_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES Students(id),
        FOREIGN KEY(class_id) REFERENCES Classes(id))
''')

students = [('John Doe',), ('Jane Smith',), ('Mike Johnson',)]
c.executemany('INSERT INTO Students(name) VALUES (?)', students)

classes = [('Math',), ('English',), ('Science',)]
c.executemany('INSERT INTO Classes(name) VALUES (?)', classes)

enrollments = [(1, 1), (1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
c.executemany('INSERT INTO Enrollment(student_id, class_id) VALUES (?, ?)', enrollments)

def fetchdata():
    c.execute('''
        SELECT Students.name
        FROM Students
        JOIN Enrollment ON Students.id = Enrollment.student_id
        JOIN Classes ON Enrollment.class_id = Classes.id
        WHERE Classes.name = 'Math'
    ''')
    students_in_math = c.fetchall()
    for student in students_in_math:
        print(student[0])

def updatedata():
    c.execute('''
        UPDATE Students
        SET name = 'Michael Johnson'
        WHERE name = 'Mike Johnson'
    ''')
def deletedata():
    c.execute('''
        DELETE FROM Students
        WHERE name = 'John Doe'
    ''')

conn.commit()
fetchdata()
conn.close()
