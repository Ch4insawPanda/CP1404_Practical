from prac_08.silver_service_taxi.silver_service_taxi import SilverServiceTaxi
from prac_08.Taxi.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    total_bill = 0
    total_distance = 0
    user_input = main_menu()
    while user_input != 'q':
        if user_input == 'c':
            current_taxi = choose_taxi()
        else:
            total_bill += drive(current_taxi)
        display_bill(total_bill)
        user_input = main_menu()
    print('-------------------------------')
    display_bill(total_bill)
    print('You travelled {}km.'.format(distance_tracker(total_distance)))
    display_taxis()

    quit()


def main_menu():
    """Display menu, get input and show total bill."""
    display_menu()
    user_choice = get_valid_input()
    return user_choice


def display_menu():
    """List choices for the user to choose. """
    print("Let's drive!")
    print('q)uit, c)hoose taxi, d)rive')


def display_bill(bill):
    """Display the total cost of the trip."""
    print('Bill to date :${}'.format(bill))


def get_valid_input():
    """Get the users' input and make sure it's valid."""
    choice = input('>>>').lower()
    while choice not in ['q', 'c', 'd']:
        print('Invalid Option')
        display_menu()
        choice = input('>>>').lower()
    return choice


def choose_taxi():
    """Display a list of taxis' for the user to choose from, and return the users' choice."""
    display_taxis()
    try:
        taxi_choice = int(input('Choose Taxi: '))
        if taxi_choice < 0 or taxi_choice > len(taxis) - 1:
            print('Invalid Taxi Choice')
            return None
        print('{} has been chosen.'.format(taxis[taxi_choice].name))
        return taxis[taxi_choice]
    except ValueError:
        print('Invalid Taxi Choice')
        return None


def display_taxis():
    """Display available taxis."""
    print('Taxis available:')
    for index, taxi in enumerate(taxis):
        print('{} - {}'.format(index, taxi))


def distance_tracker(total_distance):
    """Keep track of the total amount of distance travelled."""
    for taxi in taxis:
        total_distance += taxi.odometer
    return total_distance


def drive(current_taxi):
    """Drive the taxi a certain number of miles."""
    if current_taxi is None:
        print('Error: Cannot drive without Taxi')
        return 0
    else:
        try:
            miles_drive = int(input('Drive how far? '))
            if miles_drive < 0:  # Loop to check for negative number
                print('Error: Drive cannot be Negative')
                return 0.0
            current_taxi.drive(miles_drive)
            fare = current_taxi.get_fare()
            print('Your {} trip will cost you ${}'.format(current_taxi.name, fare))
            current_taxi.start_fare()
            return fare
        except ValueError:
            print('Error: Invalid Input')
            return 0.0


if __name__ == '__main__':
    main()
