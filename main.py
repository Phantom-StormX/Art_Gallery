import Welcome_screen
import Space_and_Nature
import pokemon
import mythology
import animals

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
""")
        encounter += 1
        break
    elif ask == "N" or ask == "n":
        print('then why did you even come here?? leave.')
        break
    else:
        print('invalid input, try again.')

which_pokemon, which_mythology, which_space, which_animal = 0, 0, 0, 0

while True:
    exhibit_entry = input('''
If you want to access one of the exhibits, type and enter its corresponding number. 
Space and Nature exhibit [1] 
Pokemon exhibit [2] 
Mythology exhibit [3] 
Animals exhibit [4] 
''')

    if exhibit_entry == '1':
        which_space = input(''' 
Awesome! my favorite exhibit! which art piece would you like to see? 
saturn [1] 
rotating galaxy [2] 
northern lights [3] 
mountains [4] 
''')
        if which_space == '1':
            print(Space_and_Nature.space_art1)
        elif which_space == '2':
            print('work in progress sorry!')
        elif which_space == '3':
            print(Space_and_Nature.space_art3)
        elif which_space == '4':
            print(Space_and_Nature.space_art4)
        break

    elif exhibit_entry == '2':
        which_pokemon = input(''' 
Awesome! which art piece would you like to see?
meowth [1] 
charmander [2] 
squirtle [3] 
ivysaur [4]''')
        if which_pokemon == '1':
            print(pokemon.pokemon_art1)
        elif which_pokemon == '2':
            print('work in progress sorry!')
        elif which_pokemon == '3':
            print('work in progress sorry!')
        elif which_pokemon == '4':
            print('work in progress sorry!')
        break

    elif exhibit_entry == '3':
        which_mythology = input(''' 
Awesome! which art piece would you like to see?
dragon [1] 
grim reaper [2] 
gryphon [3] 
mermaid [4] ''')
        if which_mythology == '1':
            print('work in progress sorry!')
        elif which_mythology == '2':
            print('work in progress sorry!')
        elif which_mythology == '3':
            print('work in progress sorry!')
        elif which_mythology == '4':
            print('work in progress sorry!')
        break

    elif exhibit_entry == '4':
        which_animal = input(''' 
Awesome! which art piece would you like to see?
frog [1] 
cat [3] 
amoeba [4] ''')
        if which_animal == '1':
            print('work in progress sorry!')
        elif which_animal == '2':
            print('work in progress sorry!')
        elif which_animal == '3':
            print('work in progress sorry!')
        elif which_animal == '4':
            print('work in progress sorry!')
        break

    else:
        print("invalid input, try again")

