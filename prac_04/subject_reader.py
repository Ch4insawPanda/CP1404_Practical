"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
data_lists=[]


def main():
    get_data()
    display_data()


def display_data():
    '''Display the data read from the file.'''
    for current_list in data_lists:
        print('{} is taught by {} and has {} students.'.format(current_list[0], current_list[1], current_list[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_lists.append(parts)
    input_file.close()

main()