"""
Friends from Earth want to know were is Louis, so Louis decides to 
write a program that will make his friends guess the name of planet.
"""

corrext_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# -------------------------------------------------------------
# Alternative 1
# -------------------------------------------------------------



# while corrext_guess is not True:
#     # Prompt user to enter a guess and assign it to 'guess' variable
#     guess = input("Louis Says: Can you guess my planet? >>> ").title()
#     if guess == planet:
#         print("Right guess!! Louis is at Zortan")
#         # Set the 'correct_guess' to 'True' and break from 'while' loop
#         corrext_guess = True
#     else:
#         # Display a message for wrong guess
#         print("Louis Says: Wrong Choise, try again!")
#         print("------------------------------------")
#         print()

# --------------------------------------------------------------
# Alternative 2
# --------------------------------------------------------------

while True:
    # Prompt user to enter a guess and assign it to 'guess' variable
    guess = input("Louis Says: Can you guess my planet? >>> ").title()
    if guess == planet:
        print("Right guess!! Louis is at Zortan")
        # Set the 'correct_guess' to 'True' and break from 'while' loop
        break
    else:
        # Display a message for wrong guess
        print(f"Louis Says: {guess} is a Wrong Choise, try again!")
        print("------------------------------------")
        print()