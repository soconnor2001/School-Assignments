import nqueens  # <- given library to do stuff related to the nqueens puzzle
import random
import math


# assignment:
# use the simulated annealing algorithm to solve to n-quens puzzle. Use a heurisic function that measures the number of
#   attacking queens as a cost function
#
# n-queens puzzle:
# given a board of n by n squares, place n queens (from chess) so that none can attack each other
#
# run the algorithm using the following values:
#     T_threshold = .9, decayRate = .000001,
#     T_threshold = .75, decayRate = .0000001,
#     T_threshold = .5, decayRate = .00000001
#
# do 10 trials for each value combination using a 4x4 grid.
#     then repeat that for an 8x8 grid and a 16x16 grid.
#
# print the initial and final board of each trial along with the initial and final h-value
#

#Code I did with a small group of students

# make scheduling func
def schedule(T, decayRate):
    return T * decayRate


# SA func
def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    T = 100
    current = initBoard
    current.h = nqueens.numAttackingQueens(current)
    #currentCost search loop
    while T >= T_Threshold and current.h != 0:
        T = schedule(T, decayRate)
        successors = nqueens.getSuccessorStates(current)
        for state in successors:
            state.h = nqueens.numAttackingQueens(state)
        nextState = random.choice(successors)
        deltaE = current.h - nextState.h
        if deltaE > 0:
            current = nextState
        else:
            thresh = math.pow(math.e, deltaE/T)
            if random.random() < thresh:
                current = nextState
    return current


# Code I did alone

def printHeader(title, symbol):
    border = ''
    for i in range(0, 40):
        border += symbol
    print(border)
    print(title)
    print(border)


def outputRun(num):
    print("Run", num)
    print("Initial Board: ")


def main():
    numOfTrials = 10

    for boardSize in [4, 8, 16]:

        printHeader("Board Size: "+str(boardSize), "*")

        for decayRate, T_threshold in [(.9, .000001), (.75, .0000001), (.5, .00000001)]:

            printHeader("Decay Rate: "+str(decayRate)+" T Threshold: "+str(T_threshold), "#")
            hValSum = 0

            for runNum in range(numOfTrials):
                initialBoard = nqueens.Board(boardSize)
                initialBoard.rand()
                print("Run", runNum)

                print("Initial Board: ")
                initialBoard.printBoard()
                print("Initial h-value:", nqueens.numAttackingQueens(initialBoard))

                finalBoard = simulatedAnnealing(initialBoard, decayRate, T_threshold)

                print("Final Board: ")
                finalBoard.printBoard()
                print("Final h-value:", finalBoard.h)
                print()

                hValSum += finalBoard.h

            hAvg = hValSum/10.0
            print("Average h-value:", hAvg)
            print()
    input("Press Enter to Close")

if __name__ == "__main__":
    main()
