"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            convert_celsius()
        elif choice == "F":
            convert_fahrenheit()
        else:
            print("Invalid option")
        menu()
        choice = get_choice()
    print("Thank you.")


def menu():
    """Print options for user."""
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)


def convert_celsius():
    """Convert celsius input into fahrenheit."""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def convert_fahrenheit():
    """Convert fahrenheit input into celsius."""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f'Result: {celsius:.2f}')


def get_choice():
    """Get user choice."""
    choice = input(">>> ").upper()
    return choice


main()