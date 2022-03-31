import os

class Puzzle_15_Solver:
    def __init__(self):
        self._matrix = [
                        [1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,0]
                        ]
    
    def _validMatrix(self, matrixInput):
        # check whether matrix is valid 15-puzzle matrix
        arr = []
        if (len(matrixInput)) != 4:
            return False
        else:
            for i in range(len(matrixInput)):
                if len(matrixInput[i]) != 4:
                    return False
                else:
                    for a in matrixInput[i]:
                        arr.append(a)
            arr.sort()
            for i in range(16):
                if arr[i] != i:
                    return False
            return True
            
    
    def setMatrix(self, matrixInput):
        if (self._validMatrix(matrixInput)):
            self._matrix = matrixInput
        else:
            print("Invalid Matrix Input")

    def displayMatrix(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                print(self._matrix[i][j], end=" ")
            print()

    def readMatrixFromInput(self):
        mat = []
        for i in range(4):
            inputArr = input().split()
            arr = [int(e) for e in inputArr]
            mat.append(arr)
        self.setMatrix(mat)
    
    def readMatrixFromFile(self):
        filename = input("Insert filename in /test : ")
        path = f"test\\{filename}"
        if os.path.isfile(path):
            f = open(path, "r")
            mat = [[int(n) for n in line.split(" ")] for line in f]
            self.setMatrix(mat)
        else:
            print("File not found !")

