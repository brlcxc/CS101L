import math

def total(values):
    return sum(values)

def average(values):
    if len(values) == 0:
        return math.nan
    return sum(values) / len(values)

def median(values):
    new_list = sorted(values)
    if len(new_list) == 0:
        raise ValueError
    if len(new_list) != 0: 
        if len(new_list) % 2 == 0:
            return ((new_list[len(new_list) // 2 -1] + new_list[len(new_list) // 2]) / 2)
        return new_list[len(new_list)//2]
