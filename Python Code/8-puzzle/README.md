# 8-Puzzle Assignment

This was for my intro into AI class. I was supposed to reate a program to run the A* search algorithm on an 8-puzzle.
8-puzzle is the puzzle where you have to slide squares around to try and complete the picture.
For this assignment we used numbers instead of images.
I ran the algorithm with the following start and goal state pairs. The ‘0’ character represents the blank tile.

## puzzle 1
Initial:

> 2 8 3  
> 1 6 4  
> 7 0 5  


Goal:   

> 1 2 3  
> 8 6 4  
> 7 5 0  

## puzzle 2
Initial:

> 7 2 4  
> 5 0 6  
> 8 3 1  

Goal:  

> 0 1 2  
> 3 4 5  
> 6 7 8  


For each pair of states, print the following:
    1) whether or not a solution was found
    2) the number of nodes expanded
    3) a list of the final path location
    4) the heuristic function used
