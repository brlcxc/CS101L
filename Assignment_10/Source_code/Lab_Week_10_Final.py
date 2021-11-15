########################################################################
##
## CS 101 Lab
## Program Week 10
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# 1. The user is asked to enter the name of a text file
# 2. The top 10 most frequently used words are output along with their frequency
# 3. The total number of words that are used once is displayed
# 4. The total number of unique words is displayed
## Error Handling:
# The file that is entered is checked if it exists
## Other Comments:
#The reason that part of the dictionary is deleted but a copy is still needed is because 
#1. If the key is not removed then it can get picked again after a new sorted value is chosen
#2. The copy is needed in conjunction with this because the dictionary cannot change size during iteration
#note: The copy of the dictionary is reset every time a new sorted value is chosen
#note2: The sorted value list never changes because sorted() turns the dictionary into a list(I think)
##
########################################################################
def read_in_file():
    while True:
        try:
            user_input = input('Enter the name of the file to open ')
            file = open(user_input)
            break
        except:
            print('Could not open file {}\nPlease Try again\n'.format(user_input))
    list_of_lines = file.readlines()
    return list_of_lines

def word_count():
    list_of_lines = read_in_file()
    list_of_words = []
    for line in list_of_lines:
        line.strip('\n')
        line = line.split()
        for word in line:
            word = word.strip('.')
            word = word.strip('!')
            word = word.strip(',')
            word = word.lower()
            if len(word) > 3:
                list_of_words.append(word)
    return list_of_words

def create_dict():
    list_of_words = word_count()
    word_set = set(list_of_words)
    word_count_dict = {}
    for set_word in word_set:
        for word2 in list_of_words:
            if set_word == word2:
                if set_word in word_count_dict:
                    word_count_dict[set_word] += 1
                else:
                    word_count_dict[set_word] = 1
    return word_set, word_count_dict

word_set, word_count_dict_output = create_dict()
word_count_dict = word_count_dict_output.copy()
print('\nMost frequently used words')
print('{:<13}{:<12}{:>12}'.format(' #', 'Word', 'Freq.'))
print('=' * 37)
count = 0
for sorted_value in sorted(word_count_dict.values(), reverse = True):
    for key, value in word_count_dict.copy().items():
        if value == sorted_value:
            if count < 10:
                count += 1
                print(' {:<2}{:>14}{:>20}'.format(count, key, value))
                del word_count_dict[key]
print('\nThere are {} words that occur only once'.format(len(list(filter(lambda value: value == 1, word_count_dict_output.values())))))
print('There are {} unique words in the document'.format(len(word_set)))