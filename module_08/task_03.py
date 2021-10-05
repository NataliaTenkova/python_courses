from peewee import *

conn = SqliteDatabase('studydb3.sqlite')

class BaseModel(Model):
    class Meta:
        database = conn

class Students(BaseModel):
    id_st = PrimaryKeyField()
    name = CharField(column_name = 'name')
    surname = CharField(column_name = 'surname')
    age = IntegerField(column_name = 'age')
    city = CharField(column_name = 'city')

class Courses(BaseModel):
    id_c = PrimaryKeyField()
    name = CharField(column_name = 'name')
    time_start = DateTimeField(column_name = 'time_start')
    time_end = DateTimeField(column_name = 'time_end')

class Student_Courses(BaseModel):
	student_id = ForeignKeyField(Students, to_field = "id_st")
	courses_id = ForeignKeyField(Courses, to_field = "id_c")

# Students.create_table()
# Courses.create_table()
# Student_Courses.create_table()

# student = Students(id_st = 1, name = "Max", surname = "Brooks", age=24 , city = "Spb")
# student.save()
# student = Students(id_st = 2, name = "John", surname = "Stones", age=15 , city = "Spb")
# student.save()
# student = Students(id_st = 3, name = "Andy", surname = "Wings", age=45 , city = "Manchester")
# student.save()
# student = Students(id_st = 4, name = "Kate", surname = "Brooks", age=34 , city = "Spb")
# student.save()

# courses = Courses(id_c = 1, name = "python", time_start = "21.07.2021", time_end = "21.08.2021")
# courses.save()
# courses = Courses(id_c = 2, name = "java", time_start = "13.07.2021", time_end = "16.08.2021")
# courses.save()

# st_c = Student_Courses(student_id = 1, courses_id = 1)
# st_c.save()
# st_c = Student_Courses(student_id = 2, courses_id = 1)
# st_c.save()
# st_c = Student_Courses(student_id = 3, courses_id = 1)
# st_c.save()
# st_c = Student_Courses(student_id = 4, courses_id = 2)
# st_c.save()

for student in Students.select().where(Students.age > 30):
	print(student.name)

for st_c in Student_Courses.select().join(Students).join(Courses):
 	print(st_c.Students.id_st)

conn.close()