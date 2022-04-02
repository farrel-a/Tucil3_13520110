# Tugas Kecil 3 IF2211 Strategi Algoritma Penyelesaian Persoalan 15-Puzzle dengan Algoritma Branch and Bound

## 13520110 - Farrel Ahmad

<br>

## Introduction
A program that is used to find solution of 15 puzzle problem and also determines whether a given 15 puzzle matrix is solvable. The program uses branch and bound approach algorithm to find the solution. The cost C(i) of node i is determined by the sum of F(i) cost and G(i) cost.  C(i) = F(i) + G(i). F(i) cost is the current depth of tree node i from starting node to node i and G cost is the approximate cost from current node i to goal node. The G(i) cost is interpeted as how many matrix element that are not correctly placed compared to the goal matrix state.

<br>

## How to Run
1. Clone the program
```sh
$ git clone https://github.com/farrel-a/Tucil3_13520110.git
```

2. Go to clone directory
```sh
$ cd Tucil3_13520110
```

3. Go to src
```sh
$ cd src
```

4. Run the program
```sh
$ python main.py
```

5. Input the matrix, there are three types of input. Manual user input, test file input from txt file in `/test` and random generated matrix input.

<br>

## Program Example

![](https://i.ibb.co/d5LFhVz/testc.png)
![](https://i.ibb.co/tzyShm2/testc2.png)