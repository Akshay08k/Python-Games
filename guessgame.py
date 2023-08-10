from random import *

print("Welcome to the Guessing Game! You have to guess a number between 1 and 10. Good luck!")
print("______________________________________________________________________________\n")

def game():
    guessnum = randint(1, 10)
    score = {"wins": 0, "losses": 0}
    
    while True:
        number = input("Enter your guess (1-10): ")
        
        try:
            number = int(number)
            
            if number < 1 or number > 10:
                print("Please enter a number within the range of 1 to 10.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter a number within the range of 1 to 10.")
            continue
        
        if number == guessnum:
            print(f"Congratulations, you won the game you won brazzer 1 month subscription the lucky number is {guessnum}.")
            score["wins"] += 1
        else:
            print(f"Sorry, the lucky number was {guessnum}. You lost the game.")
            score["losses"] += 1
        
        print(f"Score: Wins - {score['wins']}, Losses - {score['losses']}")
        
        choice = input("Do you want to play again? (yes or no): ")
        
        if choice.lower() == "yes":
            guessnum = randint(1, 10)
            continue
        if choice.lower() == 'no':
            print("Thanks for playing the game!")
            break
        if choice != ("yes","no"):
            print("please enter valid optioon")
            break
            

game()
