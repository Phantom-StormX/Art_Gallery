# imports grab information from the corresponding files, and uses whatever you want from it
# from uuid import main

import Welcome_screen, Space_and_Nature, pokemon, mythology, animals

if __name__ == "__main__":
    print(Welcome_screen.welcome_page)
    ticket = 5
    encounter = 0

    # main entry loop
    while True:
        ask = input(f'you have {ticket} tickets, that is enough to enter the gallery! would you like to enter? Y/N ')
        if ask == 'y':
            print(f""" 
    welcome to the digital art gallery! you only have {encounter} encounters. 
    here is a crash course of what this place is! this is an awesome art gallery that consists of 4 different exhibits, or themes. 
    each exhibit has at least 4 art pieces... 
    """)
            encounter += 1 # adds an encounter
            break # stops the loop and moves on to the next piece of code
        elif ask == 'n':
            print('then why did you even come here?? leave.')
            exit() # closes the system
        else:
            print('invalid input, try again.')

    # exhibit and art piece choice loop
    while True:
        exhibit_entry = input(f'''
    If you want to access one of the exhibits, type and enter its corresponding number. 
    or if you want to leave, type and enter 5 
    
    Space and Nature exhibit [1] 
    Pokemon exhibit          [2] 
    Mythology exhibit        [3] 
    Animals exhibit          [4] 
    Exit Gallery             [5]
    ''')

        if exhibit_entry == '1':
            which_space = input(f''' 
            Awesome! my favorite exhibit! which art piece would you like to see?
            also you have {encounter} encounters  
    saturn [1] 
    rotating galaxy [2] 
    northern lights [3] 
    mountains [4] 
    ''')
            # if user chooses space, they have to choose which art piece
            if which_space == '1':
                print(Space_and_Nature.space_art1)
                encounter += 1
            elif which_space == '2':
                print(Space_and_Nature.space_art2)
                encounter += 1
            elif which_space == '3':
                print(Space_and_Nature.space_art3)
                encounter += 1
            elif which_space == '4':
                print(Space_and_Nature.space_art4)
                encounter += 1
            else:
                print("Invalid art choice.")

        elif exhibit_entry == '2':
            which_pokemon = input(f''' 
            Awesome! which art piece would you like to see? 
            also you have {encounter} encounters
    meowth [1] 
    charmander [2] 
    squirtle [3] 
    ivysaur [4]
    ''')
            # if user chooses pokemon, they have to choose which art piece
            if which_pokemon == '1':
                print(pokemon.pokemon_art1)
                encounter += 1
            elif which_pokemon == '2':
                print(pokemon.pokemon_art2)
                encounter += 1
            elif which_pokemon == '3':
                print(pokemon.pokemon_art3)
                encounter += 1
            elif which_pokemon == '4':
                print(pokemon.pokemon_art4)
                encounter += 1
            else:
                print("Invalid art choice.")

        elif exhibit_entry == '3':
            which_mythology = input(f''' 
            Awesome! which art piece would you like to see? 
            also you have {encounter} encounters
    dragon [1] 
    grim reaper [2] 
    gryphon [3] 
    mermaid [4] 
    ''')
            # if user chooses mythology, they have to choose which art piece
            if which_mythology == '1':
                print(mythology.mythology_art1)
                encounter += 1
            elif which_mythology == '2':
                print(mythology.mythology_art2)
                encounter += 1
            elif which_mythology == '3':
                print(mythology.mythology_art3)
                encounter += 1
            elif which_mythology == '4':
                print(mythology.mythology_art4)
                encounter += 1
            else:
                print("Invalid art choice.")

        elif exhibit_entry == '4':

            which_animal = input(f''' 
            Awesome! which art piece would you like to see?
            also you have {encounter} encounters 
    frog [1] 
    aardvark [2]
    cat [3] 
    amoeba [4] 
    ''')
            # if user chooses animal, they have to choose which art piece
            if which_animal == '1':
                print(animals.animal_art1)
                encounter += 1
            elif which_animal == '2':
                print(animals.animal_art2)
                encounter += 1
            elif which_animal == '3':
                print(animals.animal_art_2_3)
                encounter += 1
            elif which_animal == '4':
                print(animals.animal_art4)
                encounter += 1
            else:
                print("Invalid art choice.")

        elif exhibit_entry == '5':
            print("Thank you for visiting the digital art gallery! bye bye!")
            break

        else:
            print("invalid input, try again")
