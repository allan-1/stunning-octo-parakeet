import random

wordlist = ["Jokes", "Testimony", "School", "Brother", "Charts"]


guess = int(input("Enter the number of trial : "))

start = 0
words = random.choice(wordlist)
answer = input("Enter a letter : ")
for word in wordlist:
    if answer in word:
        print("letter")
    else:
        print("letter not in word")

    