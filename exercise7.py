from temperature import *

"""
converts Celsius to Fahrenheit and visa versa for the cities in the dictionary and out puts
strings with the information
"""

cities = {"Boston": "0 C", "Boise": "48 F", "Phoenix": "85 F", "Miami": "40 C", "Riverside": "30 C",
          "Baltimore": "32 F"}

for key, value in cities.items():
    data = value.split(" ")
    if data[1] == "C":
        new_temp = str(to_fah(int(data[0])))
        print("In " + key + " it is " + data[0] + " degrees Celsius, \n\twhich is equivalent to " + new_temp +
              " degrees Fahrenheit")
    else:
        new_temp = str(to_cel(int(data[0])))
        print("In " + key + " it is " + data[0] + " degrees Fahrenheit, \n\twhich is equivalent to " + new_temp +
              " degrees Celsius")



