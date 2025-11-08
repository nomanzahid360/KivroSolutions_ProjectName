import random

print("🎉 Welcome to the Number Guessing Game! 🎯")

def number_guess():
    program_num = random.randint(1, 10)

    while True:
        try:
            get_num = int(input("👉 Choose a number (1-10): "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if get_num < 1 or get_num > 10:
            print("🚫 Please choose a number between 1 and 10!")
        elif get_num == program_num:
            print("🏆 You Win! 🎉 Great job!")
            break 
        else:
            print("❌ Wrong guess! 😢 Try again!")

    print("Thanks for playing! 👋")

number_guess()
