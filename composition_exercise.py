class Employee:
    def __init__(self, name, age='', title='', wage='', company='', description=''):
        self.name = name
        self.age = age
        self.job = Job(title, wage, company, description)

    def __str__(self):
        return "My name is %s and I am %s years old and I am a %s" % (self.name, self.age, self.job.title)

class Job:
    def __init__(self, title, wage, company, description):
        self.title = title
        self.wage = wage
        self.company = company
        self.description = description

larry = Employee("Larry", 29, "Developer", "PyClown", 150000, "Blah, blah, blah")

print(larry)
