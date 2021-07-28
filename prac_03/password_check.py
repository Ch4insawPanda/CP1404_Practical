MIN_LENGTH = 2
MAX_LENGTH = 5

password = input('Enter a password between {} to {} characters: '.format(MIN_LENGTH, MAX_LENGTH))
while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
    print('Error: Password Does Not Meet Required Length')
    password = input('Enter a password between {} to {} characters: '.format(MIN_LENGTH, MAX_LENGTH))
print('Password Created: {}'.format(len(password)*'*'))
