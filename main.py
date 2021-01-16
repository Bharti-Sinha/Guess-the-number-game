#created on 1st January 2021

import random
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

level = input("Choose a difficulty level. Type 'easy' or 'hard'. ").lower()

if level == "easy":
  attempts = 10
else:
  attempts = 5

def countdown():
  print(f"You have {attempts} attempts remaining to guess the number.")
countdown()
while attempts > 0:
  guess = int(input("Make a guess: "))
  if guess < number:
    print("Too low.\nGuess again")
    attempts = attempts - 1
    countdown()
  elif guess > number:
    print("Too high.\nGuess again")
    attempts = attempts - 1
    countdown()
  else:
    print(f"You got it. The number was {number}")
    attempts = 0




