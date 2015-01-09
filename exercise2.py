# request user input for gallons
gallons = raw_input("Please enter the number of gallons of gasoline: ")

while gallons.isalpha():
    gallons = raw_input("Words don't work for me. Give me a number: ")

gallons = float(gallons)

# assign variables product values
liters = 3.78541
barrels_oil = 19.5
co2 = 20.0
gas_ethanol = (115000.0 / 75700.0)
dollars = 4.0

# print statements that run conversions using variables and float decimal-place string formatting
print "Original number of gallons is: %.1f" % gallons

print "%.1f  gallons is the equivalent of %.2f liters" % (gallons, gallons * liters)

print "%.1f  gallons of gasoline requires %.2f barrels of oil" % (gallons, gallons / barrels_oil)

print "%.1f  gallons of gasoline is energy equivalent to %.2f gallons of ethanol" % (gallons, gallons * gas_ethanol)

print "%.1f  gallons of gasoline requires %.2f US dollars" % (gallons, gallons * dollars)
