MIN_LENGTH = 2
MAX_LENGTH = 5


def main():
    user_input = get_valid_password()
    print_asterisk(user_input)


def get_valid_password():
    """Get a valid password within the range."""
    password = input('Enter a password between {} to {} characters: '.format(MIN_LENGTH, MAX_LENGTH))
    while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print('Error: Password Does Not Meet Required Length')
        password = input('Enter a password between {} to {} characters: '.format(MIN_LENGTH, MAX_LENGTH))
    return password


def print_asterisk(user_input):
    """Print a number of asterisks."""
    print('Password Created: {}'.format(len(user_input) * '*'))


main()
