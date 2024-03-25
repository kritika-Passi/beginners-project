import random 
#coding a random number game
def guess_game(x, total_guess):
    low = 0
    high = x 
    user_input = ""

    while user_input != "correct":
        if low != high:
            comp_guess = random.randint(low,high)
            total_guess += 1
            print(comp_guess)
            user_input = input('is it "correct", or "too low" or "too high"? ').lower()
            if user_input == "too low":
                low = comp_guess + 1
            elif user_input == "too high": 
                high = comp_guess - 1 
        else:
            low = comp_guess   
    print("yay you guessed it right")
    return total_guess
            
            
x=int(input("enter the end limit : "))
print(guess_game(x,total_guess=0))
