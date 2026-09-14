import Welcome_screen

print(Welcome_screen.welcome_page)
ticket = 5
encounter = 0

while True:
    ask = input(f'you have {ticket} tickets, that is enough to enter the gallery! would you like to enter? Y/N ')
    if ask == 'Y' or ask == 'y':
        print(f"""
    welcome to the digital art gallery! 
    you only have {encounter} encounters. 
    here is a crash course of what this place is!
    this is a awesome art gallery that consists of 4 different exhibits, or themes.
    each exhibit has at least 4 art pieces...
    if you want to access one of the exhibits, type and enter its corresponding number.
""")
        exhibit_entry = input()
        break
    elif ask == "N" or ask == "n":
        print('then why did you even come here?? leave.')
        break
    else:
        print('invalid input, try again.')
