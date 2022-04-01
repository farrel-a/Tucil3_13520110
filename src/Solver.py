import os
import platform

class Puzzle_15_Solver:
    def __init__(self):
        self._matrix = [
                        [1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16]
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
                if arr[i] != i+1:
                    return False
            return True

    def _getIndex(self, a):
        for i in range(4):
            for j in range(4):
                if (self._matrix[i][j] == a):
                    return i, j
        raise Exception("Index not found")

    
    def _less(self, a):
        # for each b where position(b) > position(a) but value(b) < value(a)
        result = 0
        i, j = self._getIndex(a)
        j+=1
        while(i < 4):
            while (j < 4):
                if (self._matrix[i][j] < a):
                    result += 1
                j += 1
            i += 1
            j = 0
        return result
    
    def _getAllLess(self):
        result = 0
        for i in range(4):
            for j in range(4):
                result += self._less(self._matrix[i][j])
        return result
    
    def _reachAble(self):
        all_less = self._getAllLess()
        idx_16i, idx_16j = self._getIndex(16)
        X = 0
        if ((idx_16i == 0 or idx_16i == 2) and (idx_16j == 1 or idx_16j == 3)):
            X = 1
        elif ((idx_16i == 1 or idx_16i == 3) and (idx_16j == 0 or idx_16j == 2)):
            X = 1
        total = all_less + X
        # if even then reachable
        return total%2 == 0 
    
    def solve(self):
        if (self._reachAble()):
            # branch and bound algorithm WIP
            print()
        else:
            print("Solution is not reachable !")
    
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
        OS = platform.system()
        filename = input("Insert filename in /test : ")
        if (OS == "Windows"):
            path = f"test\\{filename}"
        elif (OS == "Linux" or OS == "Darwin"):
            path = f"test/{filename}"
        else:
            raise Exception("Program only supports Windows, Linux, and Mac OS")

        if os.path.isfile(path):
            f = open(path, "r")
            mat = [[int(n) for n in line.split(" ")] for line in f]
            self.setMatrix(mat)
        else:
            print("File not found !")

