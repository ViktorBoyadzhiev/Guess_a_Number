import random

computer_number = random.randint(1,100)

while True:
    player_numer = input("Guess the number (1-100): ")
    if not player_numer.isdigit():
        print("Invalid input. Try again.")
        continue
    if int(player_numer) > computer_number:
        print("Too High!")
        continue
    elif int(player_numer) < computer_number:
        print("Too Low!")
        continue
    elif int(player_numer) == computer_number:
        print("You guess it!")
        break