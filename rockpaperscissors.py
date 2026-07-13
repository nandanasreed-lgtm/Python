# 1) Import the `random` module to let the computer make a random choice.

# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.

# 3) Take the user's choice as input and store it in `user_action`.

# (Expected inputs: "rock", "paper", or "scissors".)

# 4) Create a list `possible_actions` containing the three valid moves.

# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move

# and store it in `computer_action`.

# 6) Display both choices (user and computer) using an f-string.

# 7) Compare `user_action` and `computer_action` to decide the result:

# a) If both are the same, print that it’s a tie.

# b) Else if the user chose "rock":

# i) If computer chose "scissors", user wins.

# ii) Otherwise, user loses (computer chose "paper").

# c) Else if the user chose "paper":

# i) If computer chose "rock", user wins.

# ii) Otherwise, user loses (computer chose "scissors").

# d) Else if the user chose "scissors":

# i) If computer chose "paper", user wins.

# ii) Otherwise, user loses (computer chose "rock").

# 8) After showing the result, ask the user if they want to play again

# and store the input in `play_again`.

# 9) If `play_again` is not "y", stop the game using `break`.

# Otherwise, the loop continues and a new round starts.
import random
while True:
    user_action = input("Enter your choice(rock, paper, scissors): ")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"Your choice : {user_action}\tComputer choice : {computer_action}")
    if computer_action == user_action:
        print("It's a tie")
    elif user_action == "rock" and computer_action == "scissors":
        print("You win!")
    elif user_action == "paper" and computer_action == "rock":
        print("You win!")
    elif user_action == "scissors" and computer_action == "paper":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you like to play again?(y/n) : ")
    if play_again == "y":
        continue
    else:
        break