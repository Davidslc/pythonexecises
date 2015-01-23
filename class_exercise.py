class Person:
    def __init__(self, name, age, birthday, address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.address = address

    def __str__(self):
        name_str = "Name: " + self.name + "\n"
        age_str = "Age: " + str(self.age) + "\n"
        birthday_str = "Birthday: " + self.birthday + "\n"
        address_str = "Address: " + self.address + "\n"

        final_str = name_str + age_str + birthday_str + address_str

        return final_str

dave = Person("Dave", 20, "October 25", "36 Helm Ave")

print(dave)
