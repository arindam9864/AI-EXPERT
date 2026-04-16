# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

# ------------------------------------------------------
# 2) INITIAL GREETING
# ------------------------------------------------------
print(f"{Fore.CYAN}👋 Welcome to Sentiment Spy 🕵️{Style.RESET_ALL}")

# ------------------------------------------------------
# 3) USER NAME INPUT
# ------------------------------------------------------
user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip()

if not user_name:
    user_name = "Mystery Agent"

# ------------------------------------------------------
# 4) CONVERSATION HISTORY
# ------------------------------------------------------
# Store (text, polarity, sentiment_type)
conversation_history = []

# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
print(f"\n{Fore.CYAN}Hello Agent {user_name}!{Style.RESET_ALL}")
print("Type any sentence and I will analyze its sentiment.")
print(f"Commands: {Fore.YELLOW}reset{Style.RESET_ALL}, "
      f"{Fore.YELLOW}history{Style.RESET_ALL}, "
      f"{Fore.YELLOW}exit{Style.RESET_ALL}\n")

# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
# ------------------------------------------------------
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # Empty input check
    if not user_input:
        print(f"{Fore.RED}⚠ Please enter some text.{Style.RESET_ALL}")
        continue

    # --------------------------------------------------
    # 6.1) EXIT COMMAND
    # --------------------------------------------------
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}👋 Goodbye, Agent {user_name}!{Style.RESET_ALL}")
        break

    # --------------------------------------------------
    # 6.2) RESET COMMAND
    # --------------------------------------------------
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 History cleared!{Style.RESET_ALL}")
        continue

    # --------------------------------------------------
    # 6.3) HISTORY COMMAND
    # --------------------------------------------------
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No history available yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):

                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # --------------------------------------------------
    # 6.4) SENTIMENT ANALYSIS
    # --------------------------------------------------
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")