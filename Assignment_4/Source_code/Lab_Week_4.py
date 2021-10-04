########################################################################
##
## CS 101 Lab
## Program 5 Week 4
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## PROBLEM : The user is supposed to input the number of chips they want to gamble between 1 and 100 inclusive. Those chips are added to the bank. 
# The user is then supposed to choose an amount to wager that is between 1 and the bank inclusive. A set of reels rolls and the amount wagered is 
# multiplied by 3 if there’s 2 matches and 10 if there’s 3 matches. If there are no matches the wager is deducted from the bank. The user is then 
# asked to continue wagering until there is no money in the bank.
##
## ALGORITHM : 
##
# 1.The user is asked to input the number of chips they want to start with between 1 and 100 inclusive
# 2.The user is asked how many chips they want to wager between 1 and the total chips inclusive
# 3.The result of the spin is output as well as the number of reels matched, how many chips were won/lost, and the current bank amount
# 4.Steps 2-3 are repeated until the bank is 0
# 5.The program outputs the chips lost, total spins, the maximum chips
# 6.The user is asked if they want to play again
# 7.If they says ‘yes’ steps 1-6 are repeated
# 8.If the user says ‘no’ then the program ends
## 
## ERROR HANDLING:
#When the user is asked the total number of chips they want to gamble, the question is reasked until a correct input is given. The value must be between 1 and 100 inclusive.
# When the user is asked how much they want to wager, the question is reasked until a correct input is given. The value must be between 1 and the bank inclusive.
# When the user is asked if they want to play again, the question is reasked until a correct input is given. Correct inputs are ‘y’, ‘yes’, ‘n’, and ‘no’
##
## OTHER COMMENTS:
#Any time a value is needed, it is returned from a function.  
# The variables are reset to their initial value when the while loop restarts.
# Count is used to record the number of spins.
# The arrows on the functions guarantee the data type of the returned value
##
########################################################################

import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play = input('Do you want to play again?\n')
        play = play.upper()
        if (play == 'Y' or play == 'YES'):
            return True
        elif (play == 'N' or play =='NO'):
            return False
        print('You must enter Y/YES/N/NO to continue. Please try again')

def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager?'))
        if wager > bank:
            print('The wager amount cannot be greater than how much you have    {}'.format(bank))
        elif wager < 1:
            print('the wager amount must be greater than 0. Please enter again.')
        else:
            return wager
def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    return (num1, num2, num3)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc):
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        chips = int(input('How many chips do you want to start with?'))
        if (chips > 0) and (chips < 101):
            return chips
        elif chips < 1:
            print('Too low a value, you can only choose 1 - 100 chips')
        else:
            print('Too high a value, you can only choose 1 - 100 chips')      

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    return wager * -1     

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initialbank = bank
        count = 0
        newbank = 0
        newhigh = bank
        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > newbank:
                newhigh = bank
            newbank = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count += 1
           
        print("You lost all {} in {} spins".format(initialbank, count))
        print("The most chips you had was {}".format(newhigh))
        playing = play_again()
