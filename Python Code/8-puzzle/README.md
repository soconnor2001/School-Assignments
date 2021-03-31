# 8-Puzzle Assignment

Create a new program to run A* on the 8-puzzle problem.
  8-puzzle is the puzzle where you have to slide squares around to try and complete the picture.
  For this assignment we will use numbers instead of images
Run the algorithm with the following start and goal state pairs. The ‘0’ character represents the blank tile.

## puzzle 1
Initial:2 8 3
        1 6 4
        7 0 5

Goal:   1 2 3
        8 6 4
        7 5 0

## puzzle 2
Initial:7 2 4
        5 0 6
        8 3 1

Goal:   0 1 2
        3 4 5
        6 7 8

For each pair of states, print the following:
    1) whether or not a solution was found
    2) the number of nodes expanded
    3) a list of the final path location
    4) the heuristic function used