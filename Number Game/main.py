import random
number = random.randint(1, 101)
guess = input("Guess any integer number between 1 and 100: ")

def validate(guess):
    if guess.isnumeric() == True:
        guess_num = int(guess)
        if 1 <= guess_num <= 100:
            return guess_num
        else:
            print("Please enter an integer number between 1 and 100")
    else:
        print("Please enter an integer number")



def guess_checker(guess, number):
    score = 100
    while guess != number:
        print("Nope. Try again.")
        score -= 10
        hint(number)
        guess = int(input("Guess again: "))
    print(f"""Congratulations! You guessed the number! I'm so proud of you :^)
    Score = {score}""")
        

def even_odd(number):
    if number % 2 == 0:
        print("The number I'm thinking of is even")
    else:
        print("The number I'm thinking of is odd")

def greater_lesser(number):
    if number <= 50:
        print("The number I'm thinking of is less than or equal to fifty")
    else:
        print("The number I'm thinking of is greater than 50")

def decade(number):
    tens_place = number // 10
    print(f"The number I'm thinking of has a {tens_place} in its ten's place")

hints_dic = {1:even_odd, 2:greater_lesser, 3:decade}
def hint(number):
    hint_num = random.randint(1, 3)
    hints_dic[hint_num](number)

guess_num = validate(guess)
guess_checker(guess_num, number)