import random

def play_game():
    while True:
        number_of_guesses = 0
        secret_number = random.randint(1, 10)
        # print(f"(Secret Number for debugging: {secret_number})")  # Optional: Remove this line in production
                    
        while True:
            print(f"\nNumber of guess attempts so far is {number_of_guesses}")
            user_guess = int(input("Guess the number I am thinking of (between 1 and 10): "))

            match user_guess:
                case _ if user_guess == secret_number:
                    print("Congratulations, you guessed it!")
                    break
                case _ if user_guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case _ if user_guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")

            number_of_guesses += 1
        ask_user = input("Do you want to play again? (y/n): ").lower()
        if ask_user not in ('y', 'yes'):
            print("Thanks for playing!")
            break

play_game()

# ALTERNATIVE 
# import random

# def play_game():
#     while True:
#         secret_number = random.randint(1, 10)
#         print(f"(Secret Number for debugging: {secret_number})")  # Optional: Remove this line in production

#         while True:
#             user_guess = int(input("Guess the number I am thinking of (between 1 and 10): "))

#             match user_guess:
#                 case guess if guess == secret_number:
#                     print("Congratulations, you guessed it!")
#                     break
#                 case guess if guess > secret_number:
#                     print("Oops, your guess is a bit high. Try again!")
#                 case guess if guess < secret_number:
#                     print("Nope, your guess is a bit low. Give it another shot!")
#                 case _:
#                     print("Invalid input. Please enter a number between 1 and 10.")

#         ask_user = input("Do you want to play again? (y/n): ").lower()
#         if ask_user not in ('y', 'yes'):
#             print("Thanks for playing!")
#             break

# play_game()
