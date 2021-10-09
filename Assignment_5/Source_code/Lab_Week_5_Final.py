########################################################################
##
## CS 101 Lab
## Program Week 5
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## PROBLEM : The user is asked to enter a library card code. If the card number number is valid then 
# the school and grade of the student is output to the user. If not, the user is told that the card is inavlid. 
# The user is also given the reason why it is invalid.
##
## ALGORITHM : 
# 1. The user is prompted to enter a library card number
# 2. If nothing is entered then the program ends
# 3. The digits of the card are checked for their validity 
# 4. If a digit in the card was entered improperly then the user is told the card is invalid and is given the reason as to why it is invalid
# 5. If the card is valid then the school and grade of the student is output 
# 6. Steps 1-5 are repeated
## 
## ERROR HANDLING:
# The verify_check_digit function checks the validity of the card. The length is checked to see if it is 10. The first five 
# characters are checked to see if they are letters. The sixth character is checked to see if it is 1-3. The seventh 
# character is checked to see if it is 1-4. The last three characters are checked to see if they are numbers. Finally 
# the last character is checked to see if it matches with the calculated check digit. If any of these values are incorrect 
# the program tells the user that the card is invalid and why.
##
## OTHER COMMENTS:
# character_value is only used in the get_check_digit function. This is because it would not properly work in the verify_check_digit 
# function since numbers could show up as the same value as letters. This is why the ord() function is used on each individual character. 
##
########################################################################
def get_school(card_number):
    school_type = ['School of Computing and Engineering SCE', 'School of Law', 'College of Arts and Sciences']
    if card_number[5] == '1':
        return school_type[0]
    elif card_number[5] == '2':
        return school_type[1]
    elif card_number[5] == '3':
        return school_type[2]

def get_grade(card_number):
    grade_type = ['Freshman', 'Sophmore', 'Junior', 'Senior']
    if card_number[6] == '1':
        return(grade_type[0])
    if card_number[6] == '2':
        return(grade_type[1])
    if card_number[6] == '3':
        return(grade_type[2])
    if card_number[6] == '4':
        return(grade_type[3])

def character_value(character):
    if character.isdigit() == True:
        value = int(character)
    else:
        character = character.upper()
        value = ord(character)
        value -= 65
    return value

def get_check_digit(card_number):
    total = 0
    for i in range(len(card_number)):
        total += ((i + 1) * character_value(card_number[i]))
    total = total % 10
    return(total)

def verify_check_digit(card_number):
    if len(card_number) != 10:
        return(False, 'The length of the number given must be 10')
    for i in range(5):
        if ((ord(card_number[i]) - 65) < 0) or ((ord(card_number[i]) - 65) > 25):
            return(False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(i, card_number[i]))
    for i in range(7, 10):
        if ord(card_number[i]) not in range(48, 59):
            return(False, 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format(i, card_number[i]))
    if ord(card_number[5]) not in range(49, 52):
        return(False, 'The sixth character must be 1 2 or 3')
    if ord(card_number[6]) not in range(49, 53):
        return(False, 'The seventh character must be 1 2 3 or 4')
    if get_check_digit(card_number) != int(card_number[9]):
        return(False, 'Check Digit {} does not match calculated value {}.'.format(card_number[9], get_check_digit(card_number)))
    return(True, '')

if __name__ == "__main__":
    print('{:^60}'.format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('=' * 60)   
    while True:
        user_input = input('Enter Library Card. Hit Enter to Exit\n')
        if len(user_input) == 0: 
            break
        check, error_statement = verify_check_digit(user_input)
        if check != False:
            print('Library card is valid.')
            print('The card belongs to a student in {}'.format(get_school(user_input)))
            print('The card belongs to a {}\n'.format(get_grade(user_input)))
        else:
            print('Library card is invalid.')
            print(error_statement)
            print()
