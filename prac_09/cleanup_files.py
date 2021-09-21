

import os


def main():

    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            get_fixed_filename(filename)
            path_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(path_name, new_name)
            print('{} has been changed to {}'.format(path_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Remove the .txt from the filename
    new_title = ''
    old_title = (filename.replace('.TXT', '.txt').replace('.txt', ''))
    print(old_title)
    for index, char in enumerate(old_title):
        # Fix blank spaces into underscore.
        if char.isspace():
            char = '_'
        # Add a space between the characters if the next character is capital.
        elif char.isalpha():
            try:
                previous_char = old_title[index - 1]
                next_char = old_title[index + 1]
                if next_char.isupper() or next_char == '(':
                    char += '_'
                # Capitalize the character if the previous character is a underscore.
                elif previous_char == '_':
                    char = char.upper()
            except IndexError:
                pass

        new_title += char
    new_title += '.txt'
    return new_title


main()
