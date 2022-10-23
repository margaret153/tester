# OOP

class Student:
    def __init__(self, name, age, group):
        print(id(self))
        self.name = name
        self.age = age
        self.group = group
stud1 = Student(name='Oleg', age=18, group='B2910')
#print(id(stud1))
print(stud1.name)
print(stud1.age)
print(stud1.group)
stud2 = Student(name='Polina', age=12, group='B2910')
print(stud2.name)
print(stud2.age)
print(stud2.group)

print(Student.group)






