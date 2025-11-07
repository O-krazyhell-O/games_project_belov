import prompt

def greet_user():
	print("Welcome to the VD games!")
	name = prompt.string("May I have your name? ")
	print(f"Hello, {name}!")
	return name
