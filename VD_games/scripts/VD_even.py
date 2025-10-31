import prompt
import random

def main():
	print("Welcome to the VD-games!")
	name = prompt.string("May I have your name? ")
	print(f"Hello, {name}")
	print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
	for i in range(3):
		number = random.randint(1, 100)
		print(f"Question: {number}")
		answer = prompt.string("Your answer: ")
		if ((number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no')):
			print("Correct!")
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if answer == 'no' else 'no'}'")
			print(f"Let's try again, {name}!")
			return
	print(f"Congratulations, {name}!")
