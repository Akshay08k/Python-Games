import random

guessnum = random.randint(1, 100)
def game():
 while True:
   
    while True:
        try:
            usernum = int(input("Enter a number to guess: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if guessnum == usernum :
        print(f"Wow you are correct the the number was {guessnum}")
        choice = input("Want to Play More(yes/no)")
        if(choice == "yes"):
            continue
            game()
    elif guessnum > usernum:
        print("Your guess was too low.")
    elif guessnum < usernum:
        print("Your guess was too high.")
    elif guessnum + 10 >= usernum >= guessnum - 10:
        print(f"Your guess was close, the number was")
    else:
        print(f"You guessed it right! The lucky number was {usernum}.")
        break
