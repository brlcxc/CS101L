########################################################################
##
## CS 101 Lab
## Program Week 9
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
## Error Handling:
##
########################################################################
import csv

def month_from_number(number):
    month_dict = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
    return month_dict[number]

def read_in_file():
    while True:
        try:
            user_input = input('Enter the name of the crime data file ==> ')
            file = open(user_input, encoding='utf-8')
            break
        except:
            print('Could not find the file specified. {} not found'.format(user_input))
    info_list = []
    file_csv = csv.reader(file)
    for line in file_csv:
        info_list.append(line)
    file.close()
    del info_list[0]
    return info_list

def create_reported_date_dict(list_info):
    occurence_dict = {}
    for line in list_info:
        if line[1] in occurence_dict:
            occurence_dict[line[1]] += 1
        else:
            occurence_dict[line[1]] = 1
    return occurence_dict

def create_reported_month_dict(list_info):
    occurence_dict = {}
    for line in list_info:
        date = line[1].split('/')
        month = int(date[0].strip('0'))
        if month not in occurence_dict:
            occurence_dict[month] = 1
        else:
            occurence_dict[month] += 1
    return occurence_dict

def create_offense_dict(list_info):
    occurence_dict = {}
    for line in list_info:
        if line[7] in occurence_dict:
            occurence_dict[line[7]] += 1
        else:
            occurence_dict[line[7]] = 1
    return occurence_dict

def create_offense_by_zip(list_info):
    crime_by_zip = {}
    for line in list_info:
        zip_code = {}
        if line[7] not in crime_by_zip:
            for line2 in list_info:
                    if line2[7] == line[7]:
                        if line2[13] not in zip_code:
                            zip_code[line2[13]] = 1
                        else:
                            zip_code[line2[13]] += 1
                        crime_by_zip[line[7]] = zip_code
    return crime_by_zip


if __name__ == "__main__":
    data_list = read_in_file()
    date_dict = create_reported_date_dict(data_list[:])
    reported_dict = create_reported_month_dict(data_list[:])
    offense_dict = create_offense_dict(data_list[:])
    offense_by_zip_dict = create_offense_by_zip(data_list[:])
    max_in_month = max(reported_dict, key=reported_dict.get)
    most_offense = max(offense_dict, key=offense_dict.get)
    print('\nThe month with the highest # of crimes is {} with {} offenses'.format(month_from_number(max_in_month), reported_dict[max_in_month]))
    print('The offense with the highest # of crimes is {} with {} offenses\n'.format(most_offense, offense_dict[most_offense]))
    while True:
        try:
            offense = input('Enter an offense ')
            number  = offense_dict[offense]
            break
        except:
            print('Not a valid offense found, please try again')
    print('\n{} offenses by Zip Code'.format(offense))
    print('{:<15}{:>15}'.format('Zip Code', '# Offenses'))
    print('=' * 30)
    for zip_code, total in (offense_by_zip_dict[offense]).items():
        print('{:<15}{:>15}'.format(zip_code, total))