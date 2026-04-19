import pandas as pd
import random
from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except:
    print(Fore.RED + "Dataset not found!")
    exit()

def senti(p):
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def show_movie(row):
    overview = row["Overview"]
    polarity = TextBlob(overview).sentiment.polarity

    print(Fore.CYAN + "\n🎬 Movie Details:")
    print(Fore.YELLOW + f"Title: {row['Series_Title']}")
    print(Fore.GREEN + f"Genre: {row['Genre']}")
    print(Fore.BLUE + f"IMDB Rating: {row['IMDB_Rating']}")
    print(Fore.MAGENTA + f"Overview: {overview}")
    print(Fore.CYAN + f"Sentiment: {senti(polarity)} ({polarity:.2f})\n")

def ai_recommend():
    genre = input(Fore.YELLOW + "Enter genre: ").strip()
    mood = input(Fore.YELLOW + "Enter your mood: ").strip()
    rating_input = input(Fore.YELLOW + "Enter minimum rating or 'skip': ").strip()

    data = df

    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]

    if rating_input.lower() != "skip":
        try:
            rating = float(rating_input)
            data = data[data["IMDB_Rating"] >= rating]
        except:
            print(Fore.RED + "Invalid rating")

    if data.empty:
        print(Fore.RED + "No movies found")
        return

    data = data.sample(frac=1)

    for _, row in data.iterrows():
        polarity = TextBlob(row["Overview"]).sentiment.polarity
        if polarity >= 0:
            show_movie(row)
            return

    print(Fore.RED + "No suitable movie found")

def random_recommend():
    row = df.sample().iloc[0]
    show_movie(row)

print(Fore.CYAN + "🎬 Welcome to Movie Recommendation System 🎬")
name = input(Fore.YELLOW + "Enter your name: ")

while True:
    print(Fore.GREEN + "\nChoose option:")
    print("1. AI Recommendation")
    print("2. Random Recommendation")

    choice = input(Fore.YELLOW + "Enter 1 or 2: ")

    if choice == "1":
        ai_recommend()
    elif choice == "2":
        random_recommend()
    else:
        print(Fore.RED + "Invalid choice")

    again = input(Fore.YELLOW + "\nDo you want another recommendation? (yes/no): ").lower()
    if again != "yes":
        print(Fore.CYAN + f"Goodbye {name}! 🎬")
        break
