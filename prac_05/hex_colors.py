NAME_TO_CODE = {'blueviolet': '#8a2be2', 'cadetblue': '#5f9ea0', 'darkgoldenrod': '#b8860b', 'darkseagreen': '#8fbc8f',
                'darkslateblue': '#483d8b', 'dimgray': '#696969', 'cornflowerblue': '#6495ed', 'indianred': '#cd5c5c',
                'lavender': '#e6e6fa', 'lawngreen': '#7cfc00', 'floralwhite': '#fffaf0'}
color_code = input("Enter Color Name: ").lower()
while color_code != "":
    if color_code in NAME_TO_CODE:
        print(color_code, "is", NAME_TO_CODE[color_code])
    else:
        print("Invalid Color Code")
    color_code = input("Enter Color Name: ").lower()
