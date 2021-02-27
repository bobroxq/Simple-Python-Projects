from categories import*
import random
from collections import Counter

options = {'1':animals, '2':rocks, '3':baked_goods, '4':acronyms}

print("Welcome to Hangman! :^D")
choice = input("""Choose a category to begin:
1. Animals
2. Rocks
3. Baked Goods
4. Acronyms
Enter your selection: """)

category = options[choice]
position = random.randint(1, len(category))
word = category[position]
answer = list(word)

wrong_letters = []
building_word = ["*" for _ in answer]
lenth = len(answer)
while lenth > 0:
    guess = input("Guess a letter: ")
    if guess in answer:
        print("You got one!")
        for index, letter in enumerate(answer):
            if letter == guess:
                building_word[index] = guess
        print(f"Correctly guessed letters: {''.join(building_word)}")
        lenth -= answer.count(guess)
    else:
        print(f"No {guess}s in this word. Guess again!")
        wrong_letters.append(guess)
        print(f"Letters not in this word: {', '.join(wrong_letters)}")
print("You did it!")
print("".join(answer))




