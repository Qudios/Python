from random import randint

players = {}

winnner_Score = 16
default_score = 0
number_players = int(input("How many Players? "))


def current_score():
    for plrname, plrvalue in players.items():
        print(f"{plrname}: {plrvalue} Points")


def roll_dice():
    return randint(1, 6)


def check_player_won(plrname, number):
    if not number:
        if players[plrname] >= winnner_Score:
            players[plrname] = winnner_Score
            current_score()
        print(f"{plrname} Won")
        ans = input("Would you like to Play Again(Y,any)?").lower()
        if ans == "y":
            pass
        else:
            quit()
    else:
        if (players[plrname] + number) >= winnner_Score:
            current_score()
            print(f"{plrname} Won")
            ans = input("Would you like to Play Again(Y,any)?").lower()
            if ans == "y":
                pass
            else:
                quit()


def player_turn(playername):
    result = 0
    while True:
        prompt = input("Would you like to roll?(Y,any)").lower()
        if prompt == "y":
            roll = roll_dice()
            print(f"Spinned {roll} Points")
            result = result + roll
            if roll == 1:
                result = 0
                return result
            print(f"Total of {result} Points")
            check_player_won(name, result)
        else:
            players[playername] += result
            return result


for i in range(number_players):
    while (player_name := input("Name? ")) in players:
        print(player_name + " is already Taken")
    players[player_name] = default_score

while True:
    for name, value in players.items():
        print(f"Player {name} turn with {value} Points")
        print(f"Earned a Total of {player_turn(name)} Points")
        current_score()
