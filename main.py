from textblob import TextBlob
import json
from datetime import datetime
import os

FILE_NAME = "history.json"


# -------- Ensure file exists --------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)


# -------- Emotion Detection --------
def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    text_lower = text.lower()

    if any(word in text_lower for word in ["angry", "mad", "furious", "hate"]):
        return "Angry 😠"
    elif any(word in text_lower for word in ["excited", "amazing", "awesome"]):
        return "Excited 🤩"
    elif polarity > 0:
        return "Happy 😊"
    elif polarity < 0:
        return "Sad 😢"
    else:
        return "Neutral 😐"


# -------- Save History --------
def save_history(text, emotion):
    initialize_file()

    with open(FILE_NAME, "r") as f:
        history = json.load(f)

    history.append({
        "text": text,
        "emotion": emotion,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)


# -------- View History --------
def view_history():
    initialize_file()

    with open(FILE_NAME, "r") as f:
        history = json.load(f)

    if len(history) == 0:
        print("\nNo history found.")
        return

    print("\n--- Emotion History ---")
    for i, item in enumerate(history, 1):
        print(f"{i}. [{item['time']}]")
        print(f"   Text: {item['text']}")
        print(f"   Emotion: {item['emotion']}\n")


# -------- Clear History --------
def clear_history():
    confirm = input("Are you sure you want to delete history? (y/n): ")

    if confirm.lower() == 'y':
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
        print("History cleared!")
    else:
        print("Cancelled.")


# -------- Help --------
def show_help():
    print("\n--- Help ---")
    print("1 → Detect emotion from text")
    print("2 → View saved history")
    print("3 → Clear history")
    print("4 → Help menu")
    print("5 → Exit")


# -------- Menu --------
def menu():
    print("\n====== Emotion Detection CLI ======")
    print("1. Analyze Text Emotion")
    print("2. View History")
    print("3. Clear History")
    print("4. Help")
    print("5. Exit")


# -------- Main --------
initialize_file()

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter your sentence: ")

        if text.strip() == "":
            print("⚠ Please enter valid text")
        else:
            emotion = detect_emotion(text)
            print("Detected Emotion:", emotion)
            save_history(text, emotion)

    elif choice == '2':
        view_history()

    elif choice == '3':
        clear_history()

    elif choice == '4':
        show_help()

    elif choice == '5':
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice.")