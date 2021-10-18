########################################################################
##
## CS 101 Lab
## Program Week 6
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# A menu is displayed telling the user to press“1” for encryption, “2” for decryption, and “Q” to quit
# The program ends if “Q” is chosen
# If “1” is chosen the user is asked to enter a statement to encrypt. If “2” is chosen the user is 
# asked to enter a statement to decrypt
# The user is asked how much the letters should be shifted by
# The encrypted/decrypted statement is output
# Steps 1-6 are repeated
## Error Handling:
# When entering the menu options the question will repeat until a correct choice is chosen
# Lower case letters are automatically capitalized
# The entered characters are checked to see if they are in the alphabet
## Other Comments:
# The encryption and decryption functions are incredibly similar. The only difference is that the 
# shift goes backward in the decryption while the shift goes forward in the encryption.
# Rather than appending characters to a list end =”” statements are used instead
##
########################################################################
def menu():
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

def decrypt():
    statement = input('\nEnter (brief) text to decrypt: ').upper()
    shift = int(input('Enter the number to shift letters by: '))
    print('Decrypted:', end = ' ')
    for letter in statement:
        if letter.isalpha() == True:
            character = chr(ord(letter) - shift)
        else:
            character = ' '
        print(character, end ='')
    print('\n')

def encode():
    statement = input('\nEnter (brief) text to encrypt: ').upper()
    shift = int(input('Enter the number to shift letters by: '))
    print('Ecrypted:', end = ' ')
    for letter in statement:
        if letter.isalpha() == True:
            character = chr(ord(letter) + shift)
        else:
            character = ' '
        print(character, end ='')
    print('\n')

def user_input():
    while True:
        menu()
        user_input = input('Enter your selection ==> ')
        if user_input == '1':
            encode()
        elif user_input == '2':
            decrypt()
        elif user_input == 'Q':
            break

def main():
    user_input()
main()
