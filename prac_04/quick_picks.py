MINVALUE = 1  # Minimum value of number generated
MAXVALUE = 45  # Maximum value of number generated
NUMBEROFPICKS = 6
numbers_list = []

number_of_lines = int(input("Enter Number of Quick Picks :"))
import random

for lines in range(number_of_lines):
    pick_list = [random.randint(MINVALUE, MAXVALUE) for i in range(NUMBEROFPICKS)]
    for number in range(NUMBEROFPICKS):
        while number in pick_list:
            pick_list.remove(number)
            random_number = random.randint(MINVALUE, MAXVALUE)
            pick_list.append(random_number)
    print(pick_list)
