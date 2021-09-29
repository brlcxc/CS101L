########################################################################
##
## CS 101 Lab 
## Program 4 Week 3
## Bishop Lohman
## brlcxc@umsystem.edu
##
## PROBLEM : The user thinks of a number between 1 and 100 inclusive and input 
# its remainder when divided by 3, 5, and 7.  The program outputs the number that the user was thinking.
##
## ALGORITHM : 
# 1. The user thinks of a number between 1 and 100 inclusive
# 2.They give the remainder of that number when divided by 3, 5, and 7
# 3. The program outputs the number that they were thinking
# 4. The user is asked to play again
# 5. If they press ‘Y’ steps 1-4 are repeated
# 6. If they press ‘N’ the program ends
## 
## ERROR HANDLING: If the user inputs a number for the remainder that is less than 0 for any of the dividing 
# numbers they are told that the value must be greater than 0. If the user inputs a number for the remainder 
# that is the dividing number or greater they are told that the number must be less than the dividing number. 
# For both cases the user is given the opportunity to input the remainder again. When the user is asked to play
#  again the question will be reasked if any character but ‘y’ or ‘n’ is entered. The program allows for ‘y’
#  and ‘n’ to be capitalized or uncapitalized. 
##
## OTHER COMMENTS:
# The dividing number and remainders are both stored in lists.
# The remainder will only be asked if the count is less than 3. The count is only increased if a correct remainder is given.
# The for loop checks the entire range of [1, 100] for the correct number. This is done by dividing each number by the dividing 
# list and seeing if it matches with the remainder list. 
# The user is asked to play again. If the user chooses ‘y’ all values preventing the loop from running are reset.
##
########################################################################
divide_list = [3,5,7]
remainder_list = []
count = -1
check = 0
again = 0
print('Welcome to the Flarsheim Guesser!\n')
while check == 0:
    while count < 3:
        if count == -1:
            print('Please think of a number between and including 1 and 100.')
            print()
            count = 0
        again = 0
        remainder = int(input('What is the remainder when your number is divided by {} ?\n'.format(divide_list[count])))
        if remainder < 0:
            print('The value entered must be 0 or greater')
            continue
        elif remainder >= divide_list[count]:
            print('The value entered must be less than {}'.format(divide_list[count]))
            continue
        else:
            remainder_list.append(remainder)
            count += 1
            print()
    for i in range(1, 101):
        if (i % 3 == remainder_list[0]) and (i % 5 == remainder_list[1]) and (i % 7 == remainder_list[2]) and again ==  0:
            again = 1
            print('Your number was {}'.format(i))
            print('How amazing is that?\n')
    play = input('Do you want to play again? Y to continue, N to quit\n')
    play = play.upper()
    if play == 'Y':
        count = -1
        remainder_list = []
        continue
    elif play == 'N':
        check = 1
    else:
        continue
