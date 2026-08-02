'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the playerʼs guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number

'''
import random
target = random.randint(1, 100)

def play_game(player_name):
    target = random.randint(1, 100)
    attempts = 0
    print(f"\n{player_name}, Start guessing.")
    
    while True:
        guess = int(input(f"{player_name}, Guess the number: "))  
        attempts +=1
        
        
        if(guess == target):
            print("Congratulation!! You Guess Correct Number.")
            break
        elif(guess>target):
            print("Lower The Number.")
        else:
            print("Higher The Number.")
           

    return attempts

player1_attempts = play_game("player1")
player2_attempts = play_game("player2")

print("/n_______RESULT________")
print(f"Player1 Attempts: {player1_attempts}")
print(f"Player2 Attempts: {player2_attempts}")

if (player1_attempts<player2_attempts):
    print("Player1 is the WINNER!")
elif(player2_attempts<player1_attempts):
    print("Player2 is the WINNER!")
else:
    print("It's a tie.")
     

