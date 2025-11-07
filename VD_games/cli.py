from VD_games import engine
from VD_games import brain_calc, even, gcd
import prompt

def main():
	print("Choose the game: ")
	print("1 - Calculator")
	print("2 - Even/odd")
	print("3 - Greatest Common Divisor (GCD)")
	choice = prompt.string("Your choice: ")
	
	match choice:
		case "1":
			engine.run_game(brain_calc)
		case "2":
			engine.run_game(even)
		case "3":
			engine.run_game(gcd)
		case _:
			print("Invalid choice. Try again.")

if __name__ == "__main__":
	main()
