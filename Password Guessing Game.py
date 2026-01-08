import random

easy_word = ["Apple", "train", "tiger", "money", "india"]
medium_words = ["python", "Bottle", "monkey", "planet","laptop"]
hard_words = ["elephant", "diamond","umbrella","computer", "mountain"]

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("Enter the level (1/2/3): ").lower()
if level == '1' or level == 'easy':
    word = random.choice(easy_word)
elif level == '2' or level == 'medium':
    word = random.choice(medium_words)
elif level == '3' or level == 'hard':
    word = random.choice(hard_words)
else:   
    print("Invalid level selected. Defaulting to Easy level.")
    word = random.choice(easy_word)

attempts = 0 
print("\nGuess the secret word")

while True:
    guess = input("Enter your guess: ")
    attempts += 1

    if guess.lower() == word.lower():
        print(f"Congratulations! You've guessed the word '{word}' in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again.")

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess [i] == word[i]:
            hint += guess[i]
        else:
            hint += "_" 
    print(f"Hint: {hint}")
print("Game over")
print("Thank you for playing the Password Guessing Game!")
