from VD_games import greet_user
import prompt

MAX_ROUNDS = 3

def run_game(game):
	print(game.NAME)
	name = greet_user()
	print(game.DESCRIPTION)
	for _ in range(MAX_ROUNDS):
		question, correct_answer = game.generate_round()
		print(question)
		answer = prompt.string("Your answer: ")
		if answer == str(correct_answer):
			print("Correct!")
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
			print(f"Let's try again, {name}!")
			break
	else:
		print(f"Congratulations, {name}!")
