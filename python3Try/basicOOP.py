class Person:
    name = 'Ivan'
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):  # _set || __set show only in class
        self.name = name
        self.age = age


vlad = Person('Vlad', 22)
#  vlad.set('Vlad', 22)
print(vlad.name)


class Student(Person):
    course = 1

    def set(self, name, age, course):  # _set || __set show only in class
        self.name = name
        self.age = age
        self.course = course


sasha = Student('sasha', 23)
#  sasha.set('sasha', 23)
print(sasha.age)
sasha.set('david', 25, 5)
print(sasha.course)
