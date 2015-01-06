gallons = float(raw_input("Please enter the number of gallons of gasoline: "))

print "Original number of gallons is: %f" % gallons

print "%f  gallons is the equivalent of %f liters" % (gallons, gallons * 3.78541)

print "%f  gallons of gasoline requires %f barrels of oil" % (gallons, gallons * .051282051)
