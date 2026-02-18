class Student:
    def __init__(self, no, name, marks):
        self.no = no
        self.name = name
        self.marks = marks

    def getName(self):
        return self.name   # FIXED (was returning no)

    def getMarks(self):
        return self.marks

    def getNo(self):
        return self.no


class School:
    def getHighestMarksStudent(self, students):
        highest = max(students, key=lambda student: student.marks)
        return highest


s1 = Student(1, "prasad", 580)
s2 = Student(2, "ram", 560)
s3 = Student(3, "Kiran", 540)

students = [s1, s2, s3]

school = School()
s4 = school.getHighestMarksStudent(students)

print("Highest Marks Student:", s4.name, s4.marks)
