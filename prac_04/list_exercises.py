TOTALNUMBERS = 5  # Total numbers to request from user
numbers_list = []


def main():
    get_number()
    number_display()


def get_number():
    for number in range(TOTALNUMBERS):
        choice = int(input('Enter Number :'))
        numbers_list.append(choice)


def number_display():
    print('The first number is {}.'.format(numbers_list[0]))
    print('The last number is {}.'.format(numbers_list[-1]))
    print('The smallest number is {}.'.format(min(numbers_list)))
    print('The largest number is {}.'.format(max(numbers_list)))
    print('The average of the numbers are {}.'.format(sum(numbers_list) / TOTALNUMBERS))


main()
