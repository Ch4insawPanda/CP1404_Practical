MINVALUE = 1  # Minimum value of number generated
MAXVALUE = 45  # Maximum value of number generated
NUMBEROFPICKS = 6  # Total numbers per line

number_of_lines = int(input("Enter Number of Quick Picks :"))


for lines in range(number_of_lines):
    import random
    picks_list = []
    while len(picks_list) != NUMBEROFPICKS:
        random_number = random.randint(MINVALUE, MAXVALUE)
        if random_number not in picks_list:
            picks_list.append(random_number)
    print(picks_list)
