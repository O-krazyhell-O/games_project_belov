import random

NAME = "VD-calc"
DESCRIPTION = "What is the result of the expression?"

def generate_round():
	a, b = random.randint(1, 100), random.randint(1, 100)
	operator = random.choice(["+", "-", "*"])
	question = f"{a} {operator} {b}"
	correct_answer = eval(question)
	return question, correct_answer
