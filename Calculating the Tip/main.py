def calculate_tip():
    bill = float(input("How much is your total bill? "))
    percent = ((float(input("How much would you like to tip? (Enter 10, 15, or 18 percent): "))) / 100)
    tip = bill * percent
    print(f"You're tip is ${round(tip, 2)}")

def even_bill_split():
    bill = float(input("How much is your total bill? "))
    percent = ((float(input("How much would you like to tip? (Enter 10, 15, or 18 percent): "))) / 100)
    total = bill + (bill * percent)
    real_total = round(total, 2)
    people = int(input("How many people are in your party? "))
    share = real_total / people
    print(f"Each person should pay ${round(share, 2)}")

def uneven_bill_split():
    bill = float(input("How much is your total bill? "))
    percent = ((float(input("How much would you like to tip? (Enter 10, 15, or 18 percent): "))) / 100)
    total = bill + (bill * percent)
    real_total = round(total, 2)
    people = int(input("How many people are in your party? "))
    for i in range(1, people + 1):
        pp = (float(input(f"What percentage of the bill would person {i} like to pay? "))) / 100
        share = real_total * pp
        print(f"Person {i} should pay ${round(share, 2)}")

task_dct = {'1':calculate_tip, '2':even_bill_split, '3':uneven_bill_split}
task = input("""What would you like to do?
1. Calculate the tip
2. Split the bill evenly
3. Split the bill unevenly
Enter your selection: """)

task_dct[task]()