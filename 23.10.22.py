# OOP
import random
class Student:
    group = 'B2910'
    def __init__(self, name, age, height=160):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Name student {self.name} \nAge student {self.age} old'

    def __del__(self):
        print('DELETE object')

    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
    def __init__(self):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness += 3

    def to_sleep(self):
        print('I want to sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.progress += 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed extremaly...')
            self.alive = False

    def end_to_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'live'
        print(f"{day:=50}")
        live_cube = random.randint
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_to_day()
        self.is_alive()
    def info_student(self):
        print(f'Name student {self.name}\n'
              f'Age student {self.age} old')


stud1 = Student(name=None, age=18)
stud2 = Student(name='Dima', age=12)
print(stud1)
print(stud2)
print(bool(stud1))
print(bool(stud2))
print(len(stud1))

# print(stud1.name)
# print(stud1.age)
# print(stud1.group)
#
# print(stud2.name)
# print(stud2.age)
# print(stud2.group)
#
# print(Student.group)
#
# Student.group = 'V2910'
#
# print(Student.group)
# print(stud1.group)
# print(stud2.group)
# stud1.group = 'B2911'
# print(stud1.group)
# print(Student.group)
# print(stud2.group)
# stud2.group = '3910'
# print(stud2.group)
# stud3 = Student(name='Anna', age=17)
# print(stud3.group)





