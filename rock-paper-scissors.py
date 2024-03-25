import random

options = ["rock" , "paper" , "scissors"]
user_input = ""
num_of_wins_user = 0
num_of_wins_comp = 0
num_of_ties = 0

while user_input != "end":
    user_input = input("Enter your guess: ").lower()
    if user_input not in options :
        print("invalid input")
    else:
        comp_guess = random.choice(options)
        print(comp_guess)
        if (user_input == "rock" and comp_guess == "scissors") or (user_input == "scissors" and comp_guess == "paper") or (user_input == "paper" and comp_guess == "rock") :
            num_of_wins_user += 1
            print("you won!")
        elif user_input == comp_guess :
            num_of_ties += 1
            print("that a tie!")
        else:
            num_of_wins_comp += 1
            print("computer won!")
        

print("the end")
print("you won " , num_of_wins_user, " times.")
print("computer won " , num_of_wins_comp , " times.")
print("total ties ", num_of_ties)




