from random import choice


def valid_choice(input):
    if input == "Rock" or input == "Paper" or input == "Scissors":
        return True
    else:
        raise ValueError("Input was not rock/paper/scissors")

def valid_answer(input):
    if input == "y":
        return True
    elif input == "n":
        return False
    else:
        raise ValueError("Input not y or n")

def has_won(player1_choice, player2_choice):
    return ((player1_choice == "Rock") and (player2_choice == "Scissors")) or ((player1_choice == "Paper") and (player2_choice == "Rock")) or ((player1_choice == "Scissors") and (player2_choice == "Paper"))



choices = ("Rock", "Paper", "Scissors")
continue_game = True
round_number = 1
user_score = 0
computer_score = 0

while continue_game:
    print(f"Let's play round {round_number}")
    while True:
        try:
            user_choice = input("Your choice (Rock/Paper/Scissors)?")
            if valid_choice(user_choice):
                break
        except ValueError as err:
            print(str(err) + ". Try again")
    computer_choice = choice(choices)
    if has_won(user_choice, computer_choice):
        print(f"My choice was {computer_choice}. You win")
        user_score += 1
    else:
        print(f"My choice was {computer_choice}. I win")
        computer_score += 1
    print(f"Score: me {computer_score}, you {user_score}")
    while True:
        try:
            answer = input("Continue (y/n)?")
            if valid_answer(answer):
                pass
            else:
                continue_game = False
            break
        except ValueError as err:
            print(str(err) + ". Try again")
    round_number += 1
