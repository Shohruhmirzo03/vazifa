import sqlite3

db = sqlite3.connect('db_name')

cursor = db.cursor()

cursor.executescript('''
--DROP TABLE IF EXISTS courses;
--DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(20),
    course_id INTEGER REFERENCES courses(course_id)
);
''')
s_n = input("Ismni kiriting: ")
c_id = int(input("Kurs id: "))


cursor.execute('''
INSERT INTO courses (course_name) VALUES (?), (?), (?)
''', ('PYTHON', 'JAVA', 'FRONTEND'))

cursor.execute('''
INSERT INTO students (fullname, course_id) VALUES (?, ?);
''', (s_n, c_id))


db.commit()
db.close()



