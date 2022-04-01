from Solver import Puzzle_15_Solver

if __name__ == "__main__":
    solver = Puzzle_15_Solver()
    # solver.displayMatrix()
    mat = [
        [1, 2, 3, 4],
        [5, 6, 16, 8],
        [9, 10, 7, 11],
        [13, 14, 15, 12]
        ]
    # solver.setMatrix(mat)
    # solver.displayMatrix()
    solver.readMatrixFromFile()
    # solver.readMatrixFromInput()
    # solver.displayMatrix()
    solver.solve()
    # solver.displayMatrix()