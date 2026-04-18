import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

budget_places = {
    "low": ["Goa", "Nepal", "Thailand"],
    "medium": ["Dubai", "Singapore", "Turkey"],
    "high": ["Switzerland", "France", "USA"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

history = []

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def detect_intent(text):
    if any(w in text for w in ["recommend", "suggest", "travel", "trip"]):
        return "recommend"
    if any(w in text for w in ["budget", "cheap", "expensive"]):
        return "budget"
    if any(w in text for w in ["pack", "packing"]):
        return "packing"
    if any(w in text for w in ["joke", "funny"]):
        return "joke"
    if any(w in text for w in ["history"]):
        return "history"
    if any(w in text for w in ["mood", "feel"]):
        return "mood"
    if any(w in text for w in ["help"]):
        return "help"
    if any(w in text for w in ["exit", "bye", "quit"]):
        return "exit"
    return "unknown"

def detect_mood(text):
    positive_words = ["happy", "good", "great", "excited"]
    negative_words = ["sad", "tired", "bad", "upset"]

    score = 0
    for w in positive_words:
        if w in text:
            score += 1
    for w in negative_words:
        if w in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

def recommend():
    print(Fore.CYAN + "TravelBot: beaches, mountains, or cities?")
    while True:
        pref = normalize(input(Fore.YELLOW + "You: "))
        if pref in destinations:
            place = random.choice(destinations[pref])
            print(Fore.GREEN + f"TravelBot: Try {place}")
            history.append(("recommend", place))
            break
        else:
            print(Fore.RED + "Choose from beaches/mountains/cities")

def budget():
    print(Fore.CYAN + "TravelBot: low, medium, or high budget?")
    while True:
        b = normalize(input(Fore.YELLOW + "You: "))
        if b in budget_places:
            place = random.choice(budget_places[b])
            print(Fore.GREEN + f"TravelBot: {place} fits your budget")
            history.append(("budget", place))
            break
        else:
            print(Fore.RED + "Type low/medium/high")

def packing():
    loc = normalize(input(Fore.CYAN + "Where to? "))
    days = input(Fore.CYAN + "Days? ")
    print(Fore.GREEN + f"Packing for {days} days in {loc}:")
    print("- Clothes")
    print("- Charger")
    print("- Toiletries")
    if "beach" in loc:
        print("- Sunscreen")
    if "mountain" in loc:
        print("- Jacket")
    history.append(("packing", loc))

def tell_joke():
    j = random.choice(jokes)
    print(Fore.YELLOW + j)
    history.append(("joke", j))

def show_history():
    if not history:
        print(Fore.RED + "No history yet")
    else:
        for i, item in enumerate(history, 1):
            print(Fore.GREEN + f"{i}. {item}")

def help_menu():
    print(Fore.MAGENTA + "Commands:")
    print("recommend | budget | packing | joke | mood | history | exit")

def mood_check(text):
    mood = detect_mood(text)
    print(Fore.CYAN + f"TravelBot: Your mood seems {mood}")
    history.append(("mood", mood))

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot")
    name = input(Fore.YELLOW + "Name: ")
    print(Fore.GREEN + f"Hi {name}")
    help_menu()

    while True:
        user = normalize(input(Fore.YELLOW + f"{name}: "))
        intent = detect_intent(user)

        if intent == "recommend":
            recommend()
        elif intent == "budget":
            budget()
        elif intent == "packing":
            packing()
        elif intent == "joke":
            tell_joke()
        elif intent == "history":
            show_history()
        elif intent == "mood":
            mood_check(user)
        elif intent == "help":
            help_menu()
        elif intent == "exit":
            print(Fore.CYAN + "TravelBot: Goodbye ✈️")
            break
        else:
            print(Fore.RED + "TravelBot: Try 'help'")

if __name__ == "__main__":
    chat()
