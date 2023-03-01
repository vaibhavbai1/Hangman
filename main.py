import random
from words import word_list
import art
from replit import clear

print(art.logo)
print("\n")
word = random.choice(word_list)
flag = True
lives = 6
length = len(word)
guess = []
for i in range(length):
    guess.append("_")
str1 = ""
print("Your word:")
print(str1.join(guess))
print(art.stages[lives])
while flag:
    letter = input("Guess a letter: ").lower()
    clear()
    if letter in word:
        for j in range(length):
            if letter == word[j]:
                guess[j] = letter
        str2 = ""
        print(str2.join(guess))
    else:
        str3 = ""
        print(str3.join(guess))
        lives -= 1
        print(f"Wrong guess! {letter} not in the word.")
        print(art.stages[lives])
    str4 = ""
    if str4.join(guess) == word:
        print("You win!")
        flag = False
    if lives == 0:
        print("You lost!")
        flag = False



