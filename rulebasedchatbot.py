import re, random
from colorama import Fore, init
init(autoreset= True)
destinations= {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountain", "Himalayas"],
    "cities": ["London", "Paris", "New York"]
}
jokes = ["why dont programmers like nature? too many bugs!", "why did the computer go to the doctor? because it had a virus!", "why do travelers always feel warm? because of all their hot spots!"]
def normaliseinput(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, Mountains or Cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normaliseinput(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no) ")
        answer = input(Fore.YELLOW + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Lets try another!")
            recommend()
        else:
            print(Fore.RED + "Travelbot: I suggest again!")
            recommend()

    else:
        print(Fore.RED + "TravelBot: sorry, I dont have that type of destination")
        recommend()
def packingtips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normaliseinput(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}")
    print(Fore.GREEN + "-Pack versatile clothes.")
    print(Fore.GREEN + "-Bring chargers and powerbanks.")
def telljokes():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")
def showhelp():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "-Suggest travel spots(say 'recommendation')")
    print(Fore.GREEN + "-Offer packing tips(say 'packing')")
    print(Fore.GREEN + "-Tell a joke(say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
def chat():
    print(Fore.CYAN + "Hello! I am TravelBot")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}")
    showhelp()
    while True:
        userinput = input(Fore.YELLOW + f"{name}: ")
        userinput = normaliseinput(userinput)
        if "recommend" in userinput or "suggest" in userinput:
            recommend()
        elif "pack" in userinput or "packing" in userinput:
            packingtips()
        elif "joke" in userinput or "funny" in userinput:
            telljokes()
        elif "exit" in userinput or "bye" in userinput:
            print(Fore.CYAN + "TravelBot: Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you please rephrase?")
chat()