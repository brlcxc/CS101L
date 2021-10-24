########################################################################
##
## CS 101 Lab
## Program Week 7
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# 1. The user is asked to enter the minimum mpg
# 2. The user is asked to enter the input vehicle file
# 3. The user is asked to input the vehicle output file name
# 4. Any value that could not be converted in the file is displayed
# 5. The output file is written with all of the vehicles that have above the minimum mpg given
## Error Handling:
# If an improper value is entered as the mpg then an error message is given. If a non-integer is entered then 
# the user is told to enter a number. If a value greater than 99 is entered then the user is told to enter a
# number less than 100. If a value less than 0 is entered then the user is told to enter a value greater than 0.
# If a file that doesn’t exist is opened then the user is told the file can not be opened.
# If the output file is written incorrectly then the user is told that they had an IO error.
# If a value within the input file can be properly read then the user is told that it can’t be read and is given the value.
## Other Comments:
# The function is almost entirely made up of functions. Only two lines of code are in the main program. 
# Only one global variable exists.
# The file is read as a csv file.
# The output file is created in one function and then passed to another. 
# The open file is being continuously passed to that function.
##
########################################################################
import csv
def car_info():
    while True:
        try:
            mpg_input = input('Enter the minimum mpg ==> ')
            if mpg_input.lstrip('-').isdigit() == False:
                raise ValueError('You must enter a number for the fuel economy')
            else:
                mpg_input = int(mpg_input)
            if (mpg_input > 0) and (mpg_input < 100):
                return mpg_input
            elif mpg_input <= 0:
                raise ValueError('Fuel economy given must be greater than 0')
            elif mpg_input >= 100:
                raise ValueError('Fuel economy must be less than 100')
        except ValueError as error_statement:
            print(error_statement)

def file_input(mpg_input):
    print()
    while True:
        try:
            user_input = input('Enter the name of the input vehicle file ==> ')
            input_test = open(user_input)
            input_test.close()            
            output_file = output_file_write()
            with open(user_input) as csvfile:
                car_check = csv.reader(csvfile, delimiter='\t')
                next(car_check)
                print()
                for row in car_check:
                    car_line(mpg_input, row, output_file)
            output_file.close()
            break
        except FileNotFoundError:
            print('Could not open file {}'.format(user_input))

def car_line(mpg_input, row, output_file):
    try:
        if (row[-3]).isdigit() == False:
            raise ValueError('Could not convert value {} for vehicle {} {} {}'.format(row[-3], row[0], row[1], row[2]))
        if int(row[-3]) >= mpg_input:
            output = '{:<5}{:<20}{:<40}{:>10}.000\n'.format(row[0], row[1], row[2],  row[-3])
            output_file.write(output)
    except ValueError as error_statement:
        print(error_statement)

def output_file_write():
    print()
    while True:
        try:
            user_input = input('Enter the name of the file to output to ==> ')
            output = open(user_input, 'w')
            return output
        except IOError:
            print('There is an IO Error {}'.format(user_input))

mpg_input = car_info()
file_input(mpg_input)