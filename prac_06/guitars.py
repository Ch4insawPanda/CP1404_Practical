from prac_06.guitar import Guitar

guitar_list = []


def main():
    get_guitar()
    # For data testing
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    display_guitars()


def get_guitar():
    """Get user input for guitar until blank"""
    name = input("Name :")
    while name != '':
        year = int(input("Year :"))
        cost = float(input("Cost :"))
        guitar_list.append(Guitar(name, year, cost))
        name = input("Name :")


def display_guitars():
    """Display all inputted guitars"""
    index = 1
    if not guitar_list:
        print('I have no guitars')
    else:
        print('These are my guitars :')
        for guitar in guitar_list:
            if guitar.is_vintage():
                print(
                    'Guitar {}: {} ({}), worth ${:.2f} (vintage)'.format(index, guitar.name, guitar.year, guitar.cost))
            else:
                print('Guitar {}: {} ({}), worth ${:.2f}'.format(index, guitar.name, guitar.year, guitar.cost))
            index += 1


if __name__ == '__main__':
    main()
