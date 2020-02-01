#Guess the number
import random
n = random.randint(0, 20)
guess = int(input('Please enter any number between 0 and 20: '))
# To check that Guess 
if guess < n:
    print("Your guess is too low")
elif guess > n:
    print("Your guess is too high")
else:
    print("You Guessed Right!")
print('The Guessed number is ' + (str(n)))