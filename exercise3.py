miles_per_hour = raw_input("Please enter a speed in miles/hour: ")

# to make sure the value entered is a number
while miles_per_hour.isalpha():
    miles_per_hour = raw_input("Please enter miles/hour using numbers, not letters: ")

mph = float(miles_per_hour)

# conversions
meters_per_hour = 1609.34 * mph
yards_per_hour = 1760.0 * mph
barleycorn_per_hour = 117.647 * meters_per_hour
barleycorn_per_day = 24.0 * barleycorn_per_hour
furlong_per_hour = yards_per_hour / 220.0
furlong_per_day = 24.0 * furlong_per_hour
feet_per_hour = 5280.0 * mph
mach = (feet_per_hour / 60 / 60) / 1130.0
psl = ((meters_per_hour / 60 / 60) / 299792458.0) * 100

print "Original speed in mph is: %.1f" % mph
print "Converted to barleycorn/day is: %.1f " % barleycorn_per_day
print "Converted to furlongs/fortnight is: %.1f " % (furlong_per_day * 14)
print "Converted to Mach number is : %f" % mach
print "Converted to the percentage of the speed of light is: %g" % psl





