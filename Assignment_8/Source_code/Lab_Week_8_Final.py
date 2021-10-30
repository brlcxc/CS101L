########################################################################
##
## CS 101 Lab
## Program Week 8
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# 1. The user is output a menu of options to choose from
# 2. The user is prompted to choose one of the options
# 3. If the user presses 1 they can add a test
# 4. If the user presses 2 they can remove a test
# 5. If the user presses 4 they can add an assignment
# 6. If the user presses 5 they can remove an assignment
# 7. If the user presses D the scores are displayed
# 8. If the user presses Q the program ends
# 9. Steps 1 and 2 are repeated until Q is pressed
## Error Handling:
# Only correct choices can be input for the menu options
# The scores chosen must be integers 
# If the user asks to remove a test or assignment that does not exist then nothing is removed
## Other Comments:
# There are two separate lists. One for the programs and one of the tests.
# They are defined globally so that they can be altered by any function 
# without the need of passing the lists to each function. 
##
########################################################################
def grade_menu():
    print('{:^30}\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit'.format('Grade Menu'))

def user_selection():
    while True:
        grade_menu()
        user_input = input('\n==> ')
        if user_input.isdigit() == False:
            user_input = user_input.upper()
        if user_input == '1':
            add_test()
        elif user_input == '2':
            remove_test()
        elif user_input == '3':
            clear_tests()
        elif user_input == '4':
            add_assignment()
        elif user_input == '5':
            remove_assignment()
        elif user_input == '6':
            clear_assignments()
        elif user_input == 'D':
            display_scores()
        elif user_input == 'Q':
            break

def display_scores():
        print('{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
        print('=' * 60)
        try:
            print('{:<15}{:^10}{:^10.1f}{:^10.1f}{:^10.2f}{:>5.2f}'.format('Tests', len(test_list), min(test_list), max(test_list), sum(test_list) / len(test_list), std_value(test_list)))
            test_weight = (sum(test_list) / len(test_list)) 
        except:
            print('{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Tests', '0', 'n/a', 'n/a', 'n/a', 'n/a'))
            test_weight = 0
        try:
            print('{:<15}{:^10}{:^10.1f}{:^10.1f}{:^10.2f}{:>5.2f}'.format('Programs', len(program_list), min(program_list), max(program_list), sum(program_list) / len(program_list), std_value(program_list)))
            program_weight = (sum(program_list) / len(program_list))
        except:
            print('{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Programs', '0', 'n/a', 'n/a', 'n/a', 'n/a'))
            program_weight = 0
        if test_weight == 0:
            total = program_weight
        elif program_weight == 0:
            total = test_weight
        else:
            total = program_weight * 0.4 + test_weight *0.6
        print('\nThe weighted scores is {:>10.2f}\n'.format(total))

def std_value(num_list):
    list_sum = 0
    list_mean = sum(num_list) / len(num_list)
    for i in num_list:
        value = (i - list_mean) ** 2
        list_sum += value 
    std = (list_sum / len(num_list)) ** (1/2)
    return std

def add_test():
    while True:
        try:
            user_input = int(input('\nEnter the new Test score 0-100 ==> '))
            test_list.append(user_input)
            print()
            break
        except:
            print('Enter a correct value')         

def remove_test():
    while True:
        try:
            user_input = int(input('\nEnter the Test to remove 0-100 ==> '))
            break
        except:
            print('Enter a correct value')    
    if user_input in test_list:
        test_list.remove(user_input)
    else:
        print('Could not find that score to remove')
    print()

def clear_tests():
    test_list.clear()

def add_assignment():
    while True:
        try:
            user_input = int(input('\nEnter the new Assignment score 0-100 ==> '))
            program_list.append(user_input)
            print()
            break
        except:
            print('Enter a correct value')

def remove_assignment():
    while True:
        try:
            user_input = int(input('\nEnter the Assignment to remove 0-100 ==> '))
            break
        except:
            print('Enter a correct value')
    if user_input in program_list:
        program_list.remove(user_input)
    else:
        print('Could not find that score to remove')
    print()

def clear_assignments():
    program_list.clear()

program_list = []
test_list = []
user_selection()