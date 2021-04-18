class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.name[0:1] + self.last_name + self.birth_year


student_name, student_last_name, student_birth_year = [input() for _ in range(3)]

student = Student(student_name, student_last_name, student_birth_year)
print(student.student_id)
