import random
number = random.randint(1, 20)
print("im thinking of a number between 1 and 20 take a guess")

for guessesTaken in range(1, 7):
    guess = int(input())
    if guess < number:
        print('too low')
    elif guess > number:
        print('too high')
    else:
        break
if guess == number:
 print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
 print('Nope. The number I was thinking of was ' + str(number))
 
