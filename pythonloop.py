# get random for the game
import random

# Make them gamble on thier guesses
numberOfGuess = int(input('How many guesses do you want?\n'))

# Set the answer pulling a random int between 1 and 20
answer = random.randint(1,20)

# Start getting their guess
userGuess = int(input('Pick a number between 1 and 20\n'))

# Set this for the counter
i = 0

while userGuess != answer and numberOfGuess > i + 1:
	if userGuess > answer:
		print('Too High! Guess again')
		i = i + 1
		print('you have ' + str(numberOfGuess - i) + ' guesses remaining')
		userGuess = int(input())
	elif userGuess < answer:
		print('Too low! Guess again')
		i = i + 1
		print('you have ' + str(numberOfGuess - i) + ' guesses remaining')
		userGuess = int(input())
	else:
		break

# if they get it right
if userGuess == answer:
	print ('You win! The answer was ' + str(answer))
	print ('You had ' + str(numberOfGuess - i - 1) + ' guesses remaining')
# Ran out of guesses
else:
	print('You lose. The answer was ' + str(answer))