# Python program to generate  quotes

import random

def get_user_input():
    name = input("Enter your name: ")
    interest = input("Enter an interest or hobby: ")
    goal = input("Enter a personal goal: ")
    return name, interest, goal

def generate_quote(name, interest, goal):
    templates = [
          f"Hey {name}, remember that {interest} is your passion. Keep pursuing your goal of {goal}.",
        f"{name}, you are amazing! Your dedication to {interest} is inspiring. Keep working towards your goal of {goal}.",
        f"Stay positive, {name}! Your love for {interest} will lead you to achieve your goal of {goal}.",
        f"{name}, embrace the journey of {interest}. Your goal of {goal} is within reach.",
    ]
    return random.choice(templates)

def save_to_file(quote):
    with open("ggenerated_quotes.txt", "a") as file:
        file.write(quote + "\n")

def main():
    print("Welcome to the Personalized Quote Generator!")

    name, interest, goal = get_user_input()
    quote = generate_quote(name, interest, goal)

    print("\nYour Personnalized Quote:")
    print(quote)

    # quote to be saved to file
    save_to_file(quote)
    print("Quote saved to  'generated_quotes.txt'.")

if __name__ == "__main__":
    main()

    