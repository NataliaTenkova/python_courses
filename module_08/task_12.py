import sqlite3

def create_connection():
	conn = sqlite3.connect('studydb.sqlite') 
	return conn

def create_db(conn):
	cursor = conn.cursor()

	cursor.execute("CREATE TABLE IF NOT EXISTS Students (id integer primary key, name varchar(50), surname varchar(100), age integer, city varchar(100))")
	cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id integer primary key, name varchar(200), time_start datetime, time_end datetime)")
	cursor.execute("CREATE TABLE IF NOT EXISTS Student_Courses (student_id integer, courses_id integer, FOREIGN KEY(student_id) REFERENCES Students(id),  FOREIGN KEY(courses_id) REFERENCES Courses(id) )")

	cursor.execute('''INSERT INTO Students (id,name,surname, age, city) VALUES (1, 'Max', 'Brooks', 24, 'Spb')''')
	cursor.execute('''INSERT INTO Students (id,name,surname, age, city) VALUES (2, 'John', 'Stones', 15, 'Spb')''')
	cursor.execute('''INSERT INTO Students (id,name,surname, age, city) VALUES (3, 'Andy', 'Wings', 45, 'Manchester')''')
	cursor.execute('''INSERT INTO Students (id,name,surname, age, city) VALUES (4, 'Kate', 'Brooks', 34, 'Spb')''')


	cursor.execute('''INSERT INTO Courses (id,name,time_start, time_end) VALUES (1,'python','21.07.2021', '21.08.2021')''')
	cursor.execute('''INSERT INTO Courses (id,name,time_start, time_end) VALUES (2, 'java', '13.07.2021', '16.08.2021')''')


	cursor.execute("INSERT INTO Student_Courses (student_id, courses_id) VALUES (1, 1)")
	cursor.execute("INSERT INTO Student_Courses (student_id, courses_id) VALUES (2, 1)")
	cursor.execute("INSERT INTO Student_Courses (student_id, courses_id) VALUES (3, 1)")
	cursor.execute("INSERT INTO Student_Courses (student_id, courses_id) VALUES (4, 2)")

	conn.commit()

def select_data(query, conn):
	cursor = conn.cursor()
	cursor.execute(query)

	rows = cursor.fetchall()

	for row in rows:
	     print(row)


connect = create_connection()

#create_db(connect)

select_data("SELECT * FROM Students WHERE age > 30", connect)
print()
select_data("SELECT s.* FROM Students s LEFT JOIN Student_Courses sc on sc.student_id = s.id LEFT JOIN Courses c on c.id = sc.courses_id WHERE c.name = 'python'", connect)
print()
select_data("SELECT s.* FROM Students s LEFT JOIN Student_Courses sc on sc.student_id = s.id LEFT JOIN Courses c on c.id = sc.courses_id WHERE c.name = 'python' and s.city = 'Spb'", connect)

connect.close()