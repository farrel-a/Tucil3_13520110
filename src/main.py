from Solver import Puzzle_15_Solver

if __name__ == "__main__":
    solver = Puzzle_15_Solver()
    print("Welcome to 15 Puzzle Solver")
    print("Enter 1 for manual input")
    print("Enter 2 for test file input")
    user_input = int(input(">>> "))
    if (user_input == 1):
        solver.readMatrixFromInput()
        solver.solve()
    elif (user_input == 2):
        solver.readMatrixFromFile()
        solver.solve()
    else:
        print("invalid input")