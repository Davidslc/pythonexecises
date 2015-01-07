gallons = float(raw_input("Please enter the number of gallons of gasoline: "))

print "Original number of gallons is: %.1f" % gallons

print "%.1f  gallons is the equivalent of %.2f liters" % (gallons, gallons * 3.78541)

print "%.1f  gallons of gasoline requires %.11f barrels of oil" % (gallons, gallons / 19.5)

print "%.1f  gallons of gasoline produces %.1f pounds of CO2" % (gallons, gallons * 20)
