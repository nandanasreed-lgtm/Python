print("hello I am ai bot, whats your name? : ")
name = input()
print(f"nice to meet you! {name}")
print("how are you feeling today? (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print("sorry to hear that. Hope things get better soon.")
else:
    print("I hope things keep getting better.")
print(f"it was nice chatting with you {name}. Goodbye!")