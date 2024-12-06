import random as r
def guess_dice_roll():
    print("welcome to the Dice Roll System:")
    roll_system = r.randint(1,6)
    user_guess = int(input("enter your guess:"))
    if user_guess == roll_system:
        print("congratulation!,you guessed the number",roll_system)
    elif user_guess>roll_system:
        print("you have enter high number", user_guess, "actual is",roll_system)
    else:
        print("you ave enter low number", user_guess,"correct no is:", roll_system)
guess_dice_roll()