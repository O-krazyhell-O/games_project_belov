import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."

def generate_round():
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	question = f"{a} {b}"
	correct_answer = math.gcd(a, b)
	return question, correct_answer
