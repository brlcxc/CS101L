########################################################################
##
## CS 101 Lab 
## Program 3
## Bishop Lohman
## brlcxc@umsystem.edu
##
## PROBLEM : The user must first enter their name and then three separate values 
# corresponding with lab grade, exam grade, and attendance grade. The grades are then 
# properly weighted and the letter grade along with the percentage are output to the user.
##
## ALGORITHM : 
## 1. Grade equals user number
#  2. Check if grade is in the correct range
#  3. Multiply the grade by the correct weight
#  4. Add grade to weighted grade
#  5. Repeat steps 1-4 two more times
#  6. Output grade percentage and letter grade
## 
## ERROR HANDLING:
## When a value over 100 is input for a grade, a message is sent to the user and the grade 
# is set as 100. When a value below 0 is input for a grade, a message is sent to the user and 
# the grade is set as 0.
##
## OTHER COMMENTS:
##      (listed in code)
##
########################################################################
list1 = ['Labs', 'EXAMS', 'Attendance']
list2 = ['lab', 'exam', 'attendance']
#Two seperate lists are made. list1 is used when asking for a grade. list2 is used when a grade is not within the proper range.
weighted_total = 0
print('**** Welcome to the Lab grade calculator! ****\n')
name = input('Who are we calculating grades for?\n')
print()
#The range is listed as three because there are three inputs
for count in range(0, 3):
    grade = int(input('Enter the {} grade?\n'.format(list1[count])))
    #The grade is reset when the loop begins
    #These statements prevent numbers out of range from being entered
    if grade < 0:
        print('The {} value should have been zero or greater. It has been changed to zero.'.format(list2[count]))
        grade = 0
    elif grade > 100:
        print('The {} value should have been 100 or less. It has been changed to 100.'.format(list2[count]))
        grade = 100
    print()
    #These statements give the grade the proper weight
    if count == 0:
        grade *= 0.7
    elif count == 1:
        grade *= 0.2
    elif count == 2:
        grade *= 0.1
#Every time the loop runs the current grade is added to the total grade.
    weighted_total += grade
print('The weighted grade for {} is {:.1f}'.format(name, weighted_total))
#These statements assign a letter grade based off the percentage.
if weighted_total >= 90:
    letter_grade = 'A'
elif weighted_total >= 80:
    letter_grade = 'B'
elif weighted_total >= 70:
    letter_grade = 'C'
elif weighted_total >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print('{} has a letter grade of {}'.format(name, letter_grade))
print()
print('**** Thanks for using the Lab grade calculator ****')
