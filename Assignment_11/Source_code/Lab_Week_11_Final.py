########################################################################
##
## CS 101 Lab
## Program Week 11
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# 1. The user enters hours, minutes, and seconds
# 2. A clock is displayed and outputs the time as time progresses
## Error Handling:
# When seconds and minutes get to 60 they are converted to minutes and hours respectively 
## Other Comments:
# The program uses if statements in the str return so that the correct clock format is output
##
########################################################################
import time

class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0, clock_type = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        if self.clock_type == 0:
            return '{:0>2}:{:0>2}:{:0>2}'.format(self.hour, self.minute, self.second)
        elif self.clock_type == 1:
            if self.hour < 12:
                if self.hour == 0:
                    return '{:0>2}:{:0>2}:{:0>2} am'.format('12', self.minute, self.second)
                else:
                    return '{:0>2}:{:0>2}:{:0>2} am'.format(self.hour, self.minute, self.second)
            else:
                return '{:0>2}:{:0>2}:{:0>2} pm'.format(self.hour, self.minute, self.second)

    def tick(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1

def main():
    hour = int(input('What is the current hour ==> '))
    minute = int(input('What is the current minute ==> '))
    second = int(input('What is the current second ==> '))
    clock = Clock(hour, minute, second, 1)
    while True:
        print(clock)
        time.sleep(1)
        clock.tick()

if __name__ == "__main__":
    main()