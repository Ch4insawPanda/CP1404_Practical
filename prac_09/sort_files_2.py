import os
import shutil

TARGET_FILE = 'FilesToSort'


def main():
    os.chdir(TARGET_FILE)

    print('Sorting files in: {}'.format(TARGET_FILE))
    ext_type_to_dir = {}
    cat_list = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        type_list = create_type_list(filenames)

        for ext_type in type_list:
            file_cat = input('What category would you like to sort {} files into? '.format(ext_type))
            ext_type_to_dir[ext_type] = file_cat
            if file_cat not in cat_list:
                cat_list.append(file_cat)

        for cat in cat_list:
            try:
                os.mkdir(cat)
            except FileExistsError:
                pass

        try:
            for file in filenames:
                extension = get_extension(file).replace('.', '')
                shutil.move(file, ext_type_to_dir[extension])
        except shutil.Error:
            pass
    print('Sort Complete')


def create_type_list(filenames):
    """Create a list of the different types of extensions in the target file."""
    type_list = []
    for file in filenames:
        file_ext = get_extension(file).replace('.', '')
        if file_ext not in type_list:
            type_list.append(file_ext)
    return type_list


def get_extension(file):
    """Get the extension of target file."""
    file_type = file.split('.')[-1]
    return file_type


if __name__ == '__main__':
    main()
