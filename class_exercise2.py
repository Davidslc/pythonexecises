# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def __lt__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __eq__(self, other):
#         pass
#
# morning = Time(10, 30, 25)
# night = Time(20, 15, 45)
#
# print(morning < night)
#
# ######
#
# class Time:
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def __lt__(self, other):
#         return True
#
#     def __gt__(self, other):
#         return True
#
#     def __eq__(self, other):
#         return True
#
# morning = Time(6, 30, 00)
# afternoon = Time(13, 00, 00)
#
# print(morning < afternoon)
# print(afternoon < morning)

#######

class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __lt__(self, other):
        return self.hours < other.hours

    # def __gt__(self, other):  # Don't need
    #    return True

    def __eq__(self, other):
        return True

morning = Time(6, 30, 00)
afternoon = Time(13, 00, 00)

print(morning < afternoon)
print(afternoon < morning)

print(morning.__lt__(afternoon))

########

class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    # def __gt__(self, other):  # Don't need
    #    return True

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

morning = Time(6, 30, 00)
afternoon = Time(13, 00, 00)

print(morning < afternoon)
print(afternoon < morning)

#######

class Time(object):
    """
    This is the class for time. This is Josh Hancock's code.
    """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.combo = self.hours + (self.minutes / 60.) + (self.seconds / 3600.)

    #
    # def __str__(self):
    #     hours_string = "Hours: " + str(self.hours) + "\n"
    #     minutes_string = "Minutes: " + str(self.minutes) + "\n"
    #     seconds_string = "Seconds: " + str(self.seconds) + "\n"
    #
    #     combo = hours_string + minutes_string + seconds_string
    #     return combo


    def __lt__(self, other):
        return self.combo < other


    def __gt__(self, other):
        return self.combo > other


    def __eq__(self, other):
        return self.combo == other


    # def __del__(self):
    #     print "Hitting the __del__ method"


morning = Time(00, 45, 23)
afternoon = Time(14, 00, 00)

print(morning > afternoon)
print(morning < afternoon)
print(morning == afternoon)
print(morning.combo)
print(afternoon.combo)
