# importing modules add stats of random pokemon to be visible and points tracking
# load the previous score if it exists
import pickle

try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

print("High score: %d" % score)


print('Hello')
Game_choice = input('Which game would you like to play? Pokemon Fight? Wizard Wars? Or Yoyo Jedi? ')

if Game_choice == 'Pokemon Fight':
    # load the previous score if it exists

    import pickle

    try:
        with open('score.dat', 'rb') as file:
            score = pickle.load(file)
    except:
        score = 0

    print("High score: %d" % score)
    print("Welcome to  Pokemon Fight!   \n")
    nickname = input("Please enter your nickname: ")
    print("Welcome " + nickname + ", \n")
    opponent_name = "randomly selected android"
    print("You are playing against " + opponent_name +  ", lets play...\n")

    import random
    import requests

    def random_pokemon():
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        pokemon = response.json()
        return {'Pokemon': pokemon['name'], 'id': pokemon['id'], 'height': pokemon['height'], 'weight': pokemon['weight']}

    player_pokemon=random_pokemon()
    print('You were given {}'.format(player_pokemon))

    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon))

    my_stat = player_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    score = 0
    score2 = 0

    if my_stat > opponent_stat:
        print('You Win!')
        score = score + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    elif my_stat < opponent_stat:
        print('You Lose!')
        score2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    else:
        print('Draw!')
        score = score + 1
        acore2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))

    while True:
        answer = input("Do you want to fight again?")
        if answer == 'yes':
            player_pokemon = random_pokemon()
            print('Your pokemon will be {}'.format(player_pokemon))
            opponent_pokemon = random_pokemon()
            stat = input('Which stat would you like to use? (id, height, or weight)')
            chosen_stat = player_pokemon[stat]
            opponent_chosen_stat = opponent_pokemon[stat]

            if chosen_stat > opponent_chosen_stat:
                print('Congratulations you have won!')
                score = score + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            elif chosen_stat < opponent_chosen_stat:
                print('Sorry you have lost')
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            else:
                print('Awkward it appears you have drawn!')
                score = score + 1
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))
        elif answer == 'no':
            print("Your score: {} Random android: {} ".format(score, score2))
            if score > score2:
                print('You are the ultimate champion!')
            else:
                print('The android is better than you please try again')
            break
        else:
            print("error")

    with open('score.dat', 'wb') as file:
        pickle.dump(score, file)


elif Game_choice == 'Wizard Wars':
    # load the previous score if it exists

    import pickle

    try:
        with open('score.dat', 'rb') as file:
            score = pickle.load(file)
    except:
        score = 0

    print("High score: %d" % score)
    print("Welcome to  Wizard Wars!   \n")
    nickname = input("Please enter your nickname: ")
    print("Welcome " + nickname + ", \n")
    opponent_name = "randomly selected android"
    print("You are playing against " + opponent_name +  ", lets play...\n")

    import random
    import requests

    def random_character():
        wizard_number = random.randint(0, 50)
        url = 'http://127.0.0.1:5000/'.format(wizard_number)
        response = requests.get(url)
        wizard = response.json()
        return wizard[wizard_number]

    player_character = random_character()
    print('You were given {}'.format(player_character))

    stat_choice = input('Which skill would you like to use? (Magic, Cunning, Wisdom or Courage?) ')

    opponent_character = random_character()
    print('The opponent chose {}'.format(opponent_character))

    my_stat = player_character[stat_choice]
    opponent_stat = opponent_character[stat_choice]

    score = 0
    score2 = 0

    if my_stat > opponent_stat:
        print('You Win!')
        score = score + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    elif my_stat < opponent_stat:
        print('You Lose!')
        score2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    else:
        print('Draw!')
        score = score + 1
        acore2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))


    while True:
        answer = input("Do you want to fight again?")
        if answer == 'yes':
            player_character = random_character()
            print('You were given {}'.format(player_character))
            stat_choice = input('Which skill would you like to use? (Magic, Cunning, Wisdom or Courage?) ')
            opponent_character = random_character()
            print('The opponent chose {}'.format(opponent_character))
            my_stat = player_character[stat_choice]
            opponent_stat = opponent_character[stat_choice]

            if my_stat > opponent_stat:
                print('Congratulations you have won!')
                score = score + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            elif my_stat < opponent_stat:
                print('Sorry you have lost')
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            else:
                print('Awkward it appears you have drawn!')
                score = score + 1
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))
        elif answer == 'no':
            print("Your score: {} Random android: {} ".format(score, score2))
            if score > score2:
                print('You are the ultimate champion!')
            else:
                print('The android is better than you please try again')
            break
        else:
            print("error")

    with open('score.dat', 'wb') as file:
        pickle.dump(score, file)

elif Game_choice == 'Yoyo Jedi' :
    # load the previous score if it exists

    import pickle

    try:
        with open('score.dat', 'rb') as file:
            score = pickle.load(file)
    except:
        score = 0

    print("High score: %d" % score)

    print("Welcome to  Yoyo Jedi!   \n")
    nickname = input("Please enter your nickname: ")
    print("Welcome " + nickname + ", \n")
    opponent_name = "randomly selected android"
    print("You are playing against " + opponent_name + ", lets play...\n")

    import random
    import requests


    def random_char():
        char_number = random.randint(0,33)
        url = 'http://127.0.0.1:5110/'.format(char_number)
        response = requests.get(url)
        starwars = response.json()
        return starwars[char_number]


    player_char = random_char()
    print('You were given {}'.format(player_char))

    stat_choice = input('Which stat do you want to use? (Honour, Anger, Greed, or Battle Skills) ')

    opponent_char = random_char()
    print('The opponent chose {}'.format(opponent_char))

    my_stat = player_char[stat_choice]
    opponent_stat = opponent_char[stat_choice]

    score = 0
    score2 = 0

    if my_stat > opponent_stat:
        print('You Win!')
        score = score + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    elif my_stat < opponent_stat:
        print('You Lose!')
        score2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))
    else:
        print('Draw!')
        score = score + 1
        acore2 = score2 + 1
        print("Your score: {} Random android: {} ".format(score, score2))

    while True:
        answer = input("Do you want to fight again?")
        if answer == 'yes':
            player_char = random_char()
            print('Your pokemon will be {}'.format(player_char))
            opponent_pokemon = random_char()
            stat = input('Which stat would you like to use? (Honour, Anger, Greed, or Battle Skills)')
            chosen_stat = player_char[stat]
            opponent_chosen_stat = opponent_pokemon[stat]

            if chosen_stat > opponent_chosen_stat:
                print('Congratulations you have won!')
                score = score + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            elif chosen_stat < opponent_chosen_stat:
                print('Sorry you have lost')
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))

            else:
                print('Awkward it appears you have drawn!')
                score = score + 1
                score2 = score2 + 1
                print("Your score: {} Random android: {} ".format(score, score2))
        elif answer == 'no':
            print("Your score: {} Random android: {} ".format(score, score2))
            if score > score2:
                print('You are the ultimate champion!')
            else:
                print('The android is better than you please try again')
            break
        else:
            print("error")

    with open('score.dat', 'wb') as file:
        pickle.dump(score, file)
else:
    print('error, please type more carefully')

with open('score.dat', 'wb') as file:
    pickle.dump(score, file)











