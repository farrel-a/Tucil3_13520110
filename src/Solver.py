import os
import platform
from copy import deepcopy
import time

class Puzzle_15_Solver:
    def __init__(self):
        self._matrix = [
                        [1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16]
                        ]
        self._states = []
        self._searchLog = []
        self._startTime = 0.0
        self._stopTime = 0.0
    
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
    
    def _getIndexMatInput(self, mat, a):
        for i in range(4):
            for j in range(4):
                if (mat[i][j] == a):
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
    
    def _getAllLess(self, show = False):
        result = 0
        a = 1
        for i in range(4):
            for j in range(4):
                less = self._less(self._matrix[i][j])
                if show:
                    print(f"{a} = {less}")
                result += less
                a += 1
        return result
    
    def _getX(self):
        X = 0
        idx_16i, idx_16j = self._getIndex(16)
        if ((idx_16i == 0 or idx_16i == 2) and (idx_16j == 1 or idx_16j == 3)):
            X = 1
        elif ((idx_16i == 1 or idx_16i == 3) and (idx_16j == 0 or idx_16j == 2)):
            X = 1
        return X

    
    def _reachAble(self):
        all_less = self._getAllLess()
        X = self._getX()
        total = all_less + X
        # if even then reachable
        return total%2 == 0 

    def _gCost(self):
        a = 1
        cost = 0
        for i in range(4):
            for j in range(4):
                if (self._matrix[i][j] != 16 and self._matrix[i][j] != a):
                    cost += 1
                a += 1
        return cost
    
    def _isTarget(self):
        a = 1
        for i in range(4):
            for j in range(4):
                if (self._matrix[i][j] != a):
                    return False
                a += 1
        return True
    
    def _ableMoveUp(self):
        i, _ = self._getIndex(16)
        return True if i-1 >= 0 else False
    
    def _ableMoveDown(self):
        i, _ = self._getIndex(16)
        return True if i+1 <= 3 else False
    
    def _ableMoveRight(self):
        _, j = self._getIndex(16)
        return True if j+1 <= 3 else False

    def _ableMoveLeft(self):
        _, j = self._getIndex(16)
        return True if j-1 >= 0 else False
    
    def _moveUp(self):
        if (self._ableMoveUp):
            i, j = self._getIndex(16)
            temp = self._matrix[i-1][j]
            self._matrix[i-1][j] = 16
            self._matrix[i][j] = temp
        else:
            print("Unable to move up")

    def _moveDown(self):
        if (self._ableMoveDown):
            i, j = self._getIndex(16)
            temp = self._matrix[i+1][j]
            self._matrix[i+1][j] = 16
            self._matrix[i][j] = temp
        else:
            print("Unable to move down")

    def _moveLeft(self):
        if (self._ableMoveLeft):
            i, j = self._getIndex(16)
            temp = self._matrix[i][j-1]
            self._matrix[i][j-1] = 16
            self._matrix[i][j] = temp
        else:
            print("Unable to move left")

    def _moveRight(self):
        if (self._ableMoveRight):
            i, j = self._getIndex(16)
            temp = self._matrix[i][j+1]
            self._matrix[i][j+1] = 16
            self._matrix[i][j] = temp
        else:
            print("Unable to move right")
    
    def _displayStep(self):
        step = []
        self._searchLog.reverse()
        prev_i, prev_j = self._getIndexMatInput(self._searchLog[0], 16)
        step.append(deepcopy(self._searchLog[0]))
        for i in range(1, len(self._searchLog)):
            curr_i, curr_j = self._getIndexMatInput(self._searchLog[i], 16)
            if (abs(curr_i-prev_i) == 1 and abs(curr_j - prev_j) == 0):
                step.append(deepcopy(self._searchLog[i]))
            elif(abs(curr_i-prev_i) == 0 and abs(curr_j - prev_j) == 1):
                step.append(deepcopy(self._searchLog[i]))
            prev_i, prev_j = curr_i, curr_j
        self._searchLog.reverse()
        step.reverse()
        step_num = 1
        for mat in step:
            self._matrix = mat
            print(f"--Step {step_num}--")
            self.displayMatrix()
            print()
            step_num += 1     
    
    def solve(self):
        print("--Initial Matrix--")
        self.displayMatrix()
        print()
        print("i = Less(i)")
        print(f"Total Less (i) = {self._getAllLess(show = True)}")
        print(f"X = {self._getX()}")
        print(f"Sigma = {self._getAllLess()} + {self._getX()} = {self._getAllLess() + self._getX()}")
        print()
        if (self._reachAble()):
            print("--Initial Matrix--")
            self.displayMatrix()
            print()

            self._startTime = time.time()
            fCost = 0
            created_node = 1
            created_nodes = []
            prev_move = ""
            while(not(self._isTarget())):
                if (self._ableMoveUp() and prev_move != "down"):
                    self._moveUp()
                    gCost = self._gCost()
                    cCost = fCost + 1 + gCost
                    created_node+=1
                    created_nodes.append(created_node)
                    mat = deepcopy(self._matrix)
                    self._states.append([created_node, mat, cCost, fCost+1, "up"])
                    self._states.sort(key = lambda x : x[2])
                    self._moveDown()

                if (self._ableMoveDown() and prev_move != "up"):
                    self._moveDown()
                    gCost = self._gCost()
                    cCost = fCost + 1 + gCost
                    created_node+=1
                    created_nodes.append(created_node)
                    mat = deepcopy(self._matrix)
                    self._states.append([created_node, mat, cCost, fCost+1, "down"])
                    self._states.sort(key = lambda x : x[2])
                    self._moveUp()
                
                if (self._ableMoveLeft() and prev_move != "right"):
                    self._moveLeft()
                    gCost = self._gCost()
                    cCost = fCost + 1 + gCost
                    created_node+=1
                    created_nodes.append(created_node)
                    mat = deepcopy(self._matrix)
                    self._states.append([created_node, mat, cCost, fCost+1, "left"])
                    self._states.sort(key = lambda x : x[2])
                    self._moveRight()

                if (self._ableMoveRight() and prev_move != "left"):
                    self._moveRight()
                    gCost = self._gCost()
                    cCost = fCost + 1 + gCost
                    created_node+=1
                    created_nodes.append(created_node)
                    mat = deepcopy(self._matrix)
                    self._states.append([created_node, mat, cCost, fCost+1, "right"])
                    self._states.sort(key = lambda x : x[2])
                    self._moveLeft()

                # print(self._states)
                cmd_arr = self._states[0]
                fCost = cmd_arr[3]
                prev_move = cmd_arr[4]
                self._states.pop(0)
                self._matrix = deepcopy(cmd_arr[1])
                self._searchLog.append(deepcopy(cmd_arr[1]))

            self._stopTime = time.time()
            self._displayStep()
            print(f"Created node = {created_node}")
            print(f"Time elapsed {self._stopTime - self._startTime:.8f} s")

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

