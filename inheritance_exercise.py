
class Person(object):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class Student(Person):
    def __str__(self):
        return "My name is %s. I am %s years old. I am studying at %s." % (self.name, self.age, self.school)

class Employee(Person):
    def __str__(self):
        return "My name is %s. I am %s years old. I am teaching at %s." % (self.name, self.age, self.school)

peter = Student("Peter", 9, "ABC Primary School")
john = Employee("John", 23, "ABC Primary School")

print(peter)
print(john)