def even_odd(num):
    if num % 2 == 0:
        print("That number is even!")
        if num == 2:
            print("It is also a prime number!")
    else:
        print("That number is odd!")
        # lzt = []
        for i in range(2, num):
            if num % i == 0:
                # lzt.append(num)
                break
        else:
            print("It is also a prime number!")


        # if len(lzt) == 8:
        #     print("It is also a prime number!")

num = int(input("What number are you thinking of? "))
even_odd(num)
print("Play again?")