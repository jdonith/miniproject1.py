import random
number = random.randrange(1,20)
guess = int(input("Guess a number between 1 and 20: "))
while number!= guess:
  if guess < number:
    print("Too low!")
    guess = int(input("Guess again: "))
  elif guess > number:
    print("Too high!")
    guess = int(input("Guess again: "))
  else:
    break
print("You guessed it right!!!")

