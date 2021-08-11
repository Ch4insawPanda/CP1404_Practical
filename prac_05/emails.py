def main():
    email_to_name = {}
    user_email = input("Enter Email :")
    while user_email != '':
        user_name = get_user_name(user_email)
        is_name = input('Is {} your name? (Y/n) :'.format(user_name)).lower()
        while is_name != 'y' and is_name != 'n':
            print('Error: Invalid Input')
            is_name = input('Is {} your name? (Y/n) :'.format(user_name)).lower()
        if is_name == 'y':
            email_to_name[user_name] = user_email
        else:
            user_name = input('Enter Name :')
            email_to_name[user_name] = user_email
        user_email = input("Enter Email :")
    for name, email in email_to_name.items():
        print('{} {}'.format(name, email))


def get_user_name(user_email):
    """Get the user name from the email"""
    user_name = user_email.split('@')
    user_name = (user_name[0]).title()
    user_name = is_split(user_name)
    return user_name


def is_split(user_name):
    """Split username into first name last name if possible."""
    if '.' in user_name:
        name_parts = user_name.split('.')
        first_name = (name_parts[0]).title()
        last_name = (name_parts[1]).title()
        user_name = ('{} {}'.format(first_name, last_name))
    return user_name


if __name__ == '__main__':
    main()
