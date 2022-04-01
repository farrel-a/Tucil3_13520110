from Solver import Puzzle_15_Solver
if __name__ == "__main__":
    solver = Puzzle_15_Solver()
    # solver.displayMatrix()
    mat = [
            [2,1,7,3],
            [4,5,6,8],
            [9,15,11,12],
            [13,14,10,0]
                        ]
    # solver.setMatrix(mat2)
    # solver.displayMatrix()
    solver.readMatrixFromFile()
    # solver.readMatrixFromInput()
    # solver.displayMatrix()
    solver.solve()