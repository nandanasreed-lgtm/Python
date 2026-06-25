'''1.  Program runs without any errors                          →   5 marks
2.  int(input()) used to read the player's guess             →   5 marks
3.  while loop stops after 5 attempts or on correct guess    →  10 marks
4.  Hint system prints ice cold / cold / warm / hot          →  10 marks
5.  for loop shows correct hearts after each wrong guess     →   5 marks
6.  Win message shown / secret revealed if attempts run out  →   5 marks'''

secret = 32
lives = 5
while lives > 0:
    guess = int(input("Guess the number between 1 and 50: "))
    if secret == guess:
        print("That's the correct answere! You win!")
        break
    elif secret > guess:
        print("Your ice cold! Try higher number!")
    elif secret < guess:
        print("It's hot! Try lower number!")
    lives -= 1
    print(f"You have {lives} lives left!")
        
    

