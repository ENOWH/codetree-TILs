n = int(input())

class Student:
    def __init__(self, name, one, two, three):
        self.name, self.one, self.two, self.three = name, one, two, three
    
students = []

for _ in range(n):
    name, one, two, three = tuple(input().split())
    students.append(Student(name, int(one), int(two), int(three)))

students.sort(key = lambda x: x.one+x.two+x.three)

for student in students:
    print(student.name, student.one, student.two, student.three)