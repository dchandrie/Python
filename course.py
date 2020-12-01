class student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age=age
        self.grade= grade
    def get_grade(self):
        return self.grade
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Course:
    def __init__(self, name, max_student):
        self.name=name
        self.max_student= max_student
        self.students =[]
    def add_student(self, student):
        if len(self.students)<self.max_student:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        pass
s1 = student("Tim", 19, 95)
s2= student("Bill", 19, 75)
s3=student("Jill", 19, 65)
# s4=student("Greg", 18, 72)
# s5=student("Meg", 17, 89)
# s6=student("Tom", 19, 92)
course = Course("Engineering", 5)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.students[0].name, course.students[0].age, course.students[0].grade)
print(course.students[1].name, course.students[1].age, course.students[1].grade)
print(course.students[2].name, course.students[2].age, course.students[2].grade)
# print(course.students[3].name, course.students[3].age, course.students[3].grade)
# print(course.students[4].name, course.students[4].age, course.students[4].grade)
# print(course.students[5].name, course.students[5].age, course.students[5].grade)
