TOTALNUMBERS = 5  # Total numbers to request from user
numbers_list = []


def main():
    get_number()
    number_display()


def get_number():
    '''Get a number of values depending on the total numbers.'''
    for number in range(TOTALNUMBERS):
        choice = int(input('Enter Number :'))
        numbers_list.append(choice)


def number_display():
    '''Display the different values from the users input'''
    print('The first number is {}.'.format(numbers_list[0]))
    print('The last number is {}.'.format(numbers_list[-1]))
    print('The smallest number is {}.'.format(min(numbers_list)))
    print('The largest number is {}.'.format(max(numbers_list)))
    print('The average of the numbers are {}.'.format(sum(numbers_list) / TOTALNUMBERS))


main()


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_password = input('Enter Password :')
if user_password in usernames:
    print('Access Granted')
else:
    print('Access Denied')