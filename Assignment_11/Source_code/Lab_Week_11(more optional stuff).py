import time

class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0, clock_type = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        time_dict = {0 : '12', 1 : '1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'11',12:'12',13:'1',14:'2',15:'3',16:'4',17:'5',18:'6',19:'7',20:'8',21:'9',22:'10',23:'11',24:'12'}
        if self.clock_type == 0:
            return '{:0>2}:{:0>2}:{:0>2}'.format(self.hour, self.minute, self.second)
        elif self.clock_type == 1:
            if self.hour < 12:
                return '{:0>2}:{:0>2}:{:0>2} am'.format(time_dict[self.hour], self.minute, self.second)
            else:
                return '{:0>2}:{:0>2}:{:0>2} pm'.format(time_dict[self.hour], self.minute, self.second)

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