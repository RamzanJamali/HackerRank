# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note:  12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#        12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Sample input      07:05:45PM
# Sample output     19:05:45

import os


def timeConversion(s):
    time_split = s.split(":")
    hour = time_split[0]
    minutes = time_split[1]
    seconds = time_split[2][:2]
    am_pm = time_split[2][2:]
    
    if am_pm == "PM":
        if hour == "12":
            hour = hour
        else:
            hour = int(hour) + 12
    else:
        if hour == "12":
            hour = "00"
        else:
            hour = hour
        
    time = "{}:{}:{}".format(hour, minutes, seconds)
    return time

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)
