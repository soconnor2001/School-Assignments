import heapq


# assignment:
# Create a new program to run A* on the 8-puzzle problem.
#   8-puzzle is the puzzle where you have to slide squares around to try and complete the picture.
#   For this assignment we will use numbers instead of images
# Run the algorithm with the following start and goal state pairs. The ‘0’ character represents the blank tile.
#
# puzzle 1
# Initial:2 8 3
#         1 6 4
#         7 0 5
#
# Goal:   1 2 3
#         8 6 4
#         7 5 0
#
# puzzle 2
# Initial:7 2 4
#         5 0 6
#         8 3 1
#
# Goal:   0 1 2
#         3 4 5
#         6 7 8
#
# For each pair of states, print the following:
#     1) whether or not a solution was found
#     2) the number of nodes expanded
#     3) a list of the final path location
#     4) the heuristic function used



#Code I was given for the assignment

# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    # print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    # print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path, pathfile):
    # print('In outputGrid')
    filenameStr = pathfile

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()


# Code I wrote alone

class Node:
    def __init__(self, grid, parent, goal):
        self.grid = grid.copy()
        self.parent = parent
        self.h = self.getHeuristicCost(goal)
        self.g = self.getPathCost()
        self.f = self.h+self.g

    def __repr__(self):
        output = ""
        for row in self.grid:
            output += " "+str(row)+"\n"
        return output

    def __eq__(self, other):
        if other == None:
            return False
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] != other.grid[row][col]:
                    return False
        return True

    def __lt__(self, other):
        return self.f < other.f

    def getRowCol(self, num):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == num:
                    return row, col
        return None, None

    def getHeuristicCost(self, goal):
        totalDist = 0
        misplaced = 9
        for goalRow in range(len(goal)):
            for goalCol in range(len(goal[0])):
                num = goal[goalRow][goalCol]
                row, col = self.getRowCol(num)
                #print(num, goalRow, goalCol , row, col)
                dist = abs(col - goalCol) + abs(row - goalRow)
                if dist == 0:
                    misplaced -= 1
                totalDist = totalDist + dist
        return totalDist + misplaced

    def getPathCost(self):
        if self.parent == None:
            return 1
        return self.parent.g + 1

    def validMove(self, row, col):
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            return True
        return False

    def copyGrid(self):
        newGrid = []
        for row in self.grid:
            newRow = []
            for num in row:
                newRow.append(num)
            newGrid.append(newRow)
        return newGrid

    def getNeighbors(self, goal):
        row, col = self.getRowCol(0)
        neighbors = []

        # check if tile above 0 can be moved into 0 space
        if self.validMove(row-1, col):

            newGrid = self.copyGrid()
            newGrid[row][col] = newGrid[row-1][col]
            newGrid[row-1][col] = 0
            newNode = Node(newGrid, self, goal)
            neighbors.append(newNode)

        # check if tile below 0 can be moved into 0 space
        if self.validMove(row+1, col):
            newGrid = self.copyGrid()
            newGrid[row][col] = newGrid[row+1][col]
            newGrid[row+1][col] = 0
            newNode = Node(newGrid, self, goal)
            neighbors.append(newNode)

        # check if tile left 0 can be moved into 0 space
        if self.validMove(row, col-1):
            newGrid = self.copyGrid()
            newGrid[row][col] = newGrid[row][col-1]
            newGrid[row][col-1] = 0
            newNode = Node(newGrid, self, goal)
            neighbors.append(newNode)

        # check if tile right 0 can be moved into 0 space
        if self.validMove(row, col+1):
            newGrid = self.copyGrid()
            newGrid[row][col] = newGrid[row][col+1]
            newGrid[row][col+1] = 0
            newNode = Node(newGrid, self, goal)
            neighbors.append(newNode)

        return neighbors

    def expandNode(self, closedList, openList, goal):
        expandedStates = 0
        neighbors = self.getNeighbors(goal)
        for node in neighbors:
            # print('here')
            if node not in openList and node not in closedList:
                heapq.heappush(openList, node)
                expandedStates += 1
        closedList.append(self)
        return expandedStates


def getPath(current):
    path = []
    while current != None:
        path.insert(0, current)
        current = current.parent
    return path


def informedSearch(start, goal,):
    # method can be BFS or DFS
    # BFS = (method == "BFS")

    current = Node(start, None,  goal)

    openList = []
    closedList = []

    expandedStates = current.expandNode( closedList, openList, goal)

    while len(openList) > 0 and current.grid != goal:
        current = heapq.heappop(openList)
        newStates = current.expandNode(closedList, openList, goal)
        expandedStates += newStates
        # print(current)
    path = []
    if current.grid != goal:
       solFound = "No"
    else:
        solFound = "Yes"
        path = getPath(current)

    return path, expandedStates, solFound


def outputInfo(solFound, expandedStates, path, functionUsed):
    print("1) Solution found:", solFound)
    print("2) Number of States Expanded:", expandedStates)
    if path == []:
        print("3) Final Path Locations: None")
    else:
        print("3) Final Path Locations:")
        for node in path:
            print(node)
    print("4) Heuristic function used:", functionUsed)


def getInputs(directory):
    startFile = directory+"\\initial.txt"
    goalFile = directory+"\\goal.txt"
    start = readGrid(startFile)
    goal = readGrid(goalFile)
    return start, goal


def main():

    # puzzle 1
    print("Puzzle 1:")
    # getInputs(directory) take a folder in the same folder as this program called directory and takes the
    #     initial and goal states from initial.txt and goal.txt which are in that fold
    
    start, goal = getInputs("puzzle1")

    # a* search
    path, expandedStates, solFound = informedSearch(start, goal)
    outputInfo(solFound, expandedStates, path, "Manhattan Distance and Misplaced Tiles")


    #puzzle 2
    print("Puzzle 2:")
    start, goal = getInputs("puzzle2")


    path, expandedStates, solFound = informedSearch(start, goal)
    outputInfo(solFound, expandedStates, path, "Manhattan Distance and Misplaced Tiles")

    input("Press Enter to Close")

if __name__ == "__main__":
    main()
