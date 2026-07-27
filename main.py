'''
-1 = Rock
0 = Paper 
1 = scissors

'''
# Computer Choose random value
import random
computer = random.choice([-1, 0, 1])

# User input their value
youstr = input("Enter your Choice: ")

youDict = {"r": -1, "p": 0, "s": 1}
reversDict = {-1: "Rock", 0: "Paper", 1: "scissors"}

you = youDict[youstr]


print(f"You Choose: {reversDict[you]}\nComputer Choose: {reversDict[computer]}")

# Result Condition
if(computer == you):
    print("It's a Draw!")
else:
    if(computer ==-1 and you ==0):
        print("You Win!")
    elif(computer ==-1 and you ==1):
            print("You Loose!Better luck next Time.")
    elif(computer ==0 and you ==1):
            print("You Win!")
    elif(computer ==0 and you ==-1):
            print("You Loose!Better luck next Time.")
    elif(computer ==1 and you ==-1):
            print("You Win!")
    elif(computer ==1 and you ==0):
            print("You Loose!Better luck next Time.")
    else:
        print("Somerhing Went Wrong")
        
# THE END