from random import choice

def valid_choice(choice):
    '''
    Checks if the RPS choice is valid
    :param choice: RPS choice
    '''
    choice = choice.lower()
    if not (choice == "rock" or choice == "paper" or choice == "scissors"):
        raise ValueError(f"I don't understand {choice}. Try again")

def valid_input(input):
    input = input.lower()
    if not (input == "y" or input == "n"):
        raise ValueError(f"I don't understand {input}. Try again")

def computer_choice():
    choices = ('rock', 'paper', 'scissors')
    return choice(choices)

def has_won(choice, other_choice):
    if choice == 'paper' and other_choice == 'rock':
        return True
    if choice == 'rock' and other_choice == 'scissors':
        return True
    if choice == 'scissors' and other_choice == 'paper':
        return True
    return False

user_points = 0
computer_points = 0
round_number = 1
while True:
    print(f"Lets play round {round_number}")

    # Validate RPS input
    while True:
        try:
            user_choice = input("Your choice (Rock/Paper/Scissors)?")
            valid_choice(user_choice)
            break
        except ValueError as err:
            print(err)

    comp_choice = computer_choice()

    # Check who won
    if has_won(user_choice, comp_choice):
        print(f"My choice was {user_choice}. Computer choice was {comp_choice}. I win.")
        user_points += 1
    elif has_won(comp_choice, user_choice):
        print(f"My choice was {user_choice}. Computer choice was {comp_choice}. You win.")
        computer_points += 1
    else:
        print(f"My choice was {user_choice}. Computer choice was {comp_choice}. It was a tie.")
    print(f"Score: me {user_points}, you {computer_points}")

    # Validate continue input
    while True:
        try:
            user_input = input("Continue (y/n)?")
            valid_input(user_input)
            break
        except ValueError as err:
            print(err)

    if user_input == "n":
        break
    round_number += 1
