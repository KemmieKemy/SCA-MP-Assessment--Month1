#Password Generator
import random, string

print('Password Generator')

#User Input
letter = int(input('Enter the number of Letters that you want in your Password: '))
number = int(input('Enter the number of Numbers that you want in your Password: '))
character = int(input('Enter the number of Characters that you want in your Password: '))

all_numbers =  ''.join(random.choice(string.digits) for i in range(number))
all_letters = ''.join(random.choice(string.ascii_letters) for i in range(letter))
all_characters = ''.join(random.choice(string.punctuation) for i in range(character))

formation = all_numbers + all_letters + all_characters
pwd_gen = random.sample(formation, len(formation)) 
password = ''.join((pwd_gen))
if len(formation) < 6:
    print('Password should be minimum of 6 characters, try again')
else:
        print('Your password is {}' .format(password))