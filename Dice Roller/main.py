import random
answer = input("Would you like to roll the dice? ")

while answer == 'yes':
    print(random.randint(1,6))
    answer = input("Roll again? ")