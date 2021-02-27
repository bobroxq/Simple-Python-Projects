words = input("Please enter five words, separated by spaces: ")
lzt = words.split()
for element in lzt:
    wrd = list(element)
    drw = list(reversed(wrd))
    if wrd == drw:
        print(f"{element} is a palindrome! :)")
    else:
        print(f"{element} is NOT a palidrome :(")

# ALTERNATIVES THAT ALSO WORK:
# words = input("Please enter five words, separated by spaces: ")
# lzt = words.split()
# for element in lzt:
#     wrd = element
#     drw = element[::-1]
#     if wrd == drw:
#         print(f"{element} is a palindrome! :)")
#     else:
#         print(f"{element} is NOT a palidrome :(")

# words = input("Please enter five words, separated by spaces: ")
# lzt = words.split()
# for element in lzt:
#     if element == element[::-1]:
#         print(f"{element} is a palindrome! :)")
#     else:
#         print(f"{element} is NOT a palidrome :(")