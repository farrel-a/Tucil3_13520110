from Solver import Puzzle_15_Solver

if __name__ == "__main__":
    # Instantiate puzzle 15 solver object
    solver = Puzzle_15_Solver()

    # Main Menu
    print("Welcome to 15 Puzzle Solver")
    print("Enter 1 for manual input")
    print("Enter 2 for test file input")
    try:
        user_input = int(input(">>> "))
        if (user_input == 1):
            solver.readMatrixFromInput()
            solver.solve()
        elif (user_input == 2):
            solver.readMatrixFromFile()
            solver.solve()
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")