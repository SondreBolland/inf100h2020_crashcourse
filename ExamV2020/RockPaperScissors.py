from random import choice

continue_game = True
round_number = 1
choices = ["rock", "paper", "scissors"]
human_score = 0
computer_score = 0


def valid_choice(choice):
    choice = choice.lower()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        raise Exception(f"I don't understand {your_choice}. Try again.")

def valid_continue_answer(answer):
    answer = answer.lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        raise Exception(f"I don't understand {answer}. Try again.")


def win(choice1, choice2):
    return ((choice1 == "rock") and (choice2 == "scissors")) or ((choice1 == "paper") and (choice2 == "rock")) or ((choice1 == "scissors") and (choice2 == "paper"))


while continue_game:
    print(f"Let's play round {round_number}")
    while True:
        try:
            your_choice = input("Your choice (Rock/Paper/Scissors)?")
            if valid_choice(your_choice):
                break
        except Exception as err:
            print(err)
    computer_choice = choice(choices)
    if win(your_choice, computer_choice):
        print(f"My choice was {computer_choice}. You win")
        human_score += 1
    elif your_choice == computer_choice:
        print(f"My choice was {computer_choice}. It's a tie.")
    else:
        print(f"My choice was {computer_choice}. I win")
        computer_score += 1
    print(f"Score: me {computer_score}, you {human_score}")
    while True:
        try:
            continue_answer = input("Continue (y/n)?")
            if valid_continue_answer(continue_answer):
                round_number += 1
            else:
                continue_game = False
            break
        except Exception as err:
            print(err)


