import re

# assignment:
# given a grid of ones and zeros in gridFile.txt,
#   perform a Breadth First search and a Depth first search of the grid,
#   put the path of each given search algorithm in a file, pathBFS and path DFS respectively.
# Input the start and goal space for the search in the console



# Code I was given for the assignment

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
    # print('Exiting outputGrid')


# code I worked with a small group of students

class Node:
    def __init__(self, val, par):
        self.value = val
        self.parent = par

    def __repr__(self):
        return "value: "+str(self.value)

    def __eq__(self, other):
        if other == None:
            return False
        return self.value == other.value

    def getNeighbors(self, location, grid):  # only up down left right
        r = location[0]
        c = location[1]
        neighbors = []

        # check up
        if validSpace(grid, r-1, c):
            neighbors.append(Node([r-1, c], self))

        # check down
        if validSpace(grid, r+1, c):
            neighbors.append(Node([r+1, c], self))

        # check left
        if validSpace(grid, r, c+1):
            neighbors.append(Node([r, c+1], self))

        # check right
        if validSpace(grid, r, c-1):
            neighbors.append(Node([r, c-1], self))

        return neighbors

    def expandNode(self, grid, closedList, openList):
        neighbors = self.getNeighbors(self.value, grid)
        for node in neighbors:
            # print('here')
            if not(node in openList or node in closedList):
                openList.append(node)
        closedList.append(self)
        # print("open",openList)
        # print("closed",closedList)


def validSpace(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        if grid[row][col] == 0:
            return True
    return False


# code I worked on alone

def setPath(current, path):
    while current != None:
        path.append(current)
        current = current.parent

def uninformedSearch(grid, start, goal, method):
    # method can be BFS or DFS
    BFS = (method == "BFS")

    if not validSpace(grid,goal[0],goal[1]):
        return None

    current = Node(start, None)
    openList = []
    closedList = []

    current.expandNode(grid, closedList, openList)

    while current.value != goal and len(openList) > 0:
        if BFS:
            current = openList.pop(0)
        else:
            current = openList.pop()
        current.expandNode(grid, closedList, openList)
        # print(openList)
        # print(current)
    if current.value != goal:
        return None
    path = []

    setPath(current, path)

    return path


def getInputs(grid):
    startStr = input("Please enter a initial state (row, col): ")
    startLoc = [(int)(x.strip()) for x in re.split("\(|\)|,",startStr) if x.strip() != '']

    while not validSpace(grid,startLoc[0],startLoc[1]):
        startStr = input("That initial state entered is invalid.\nPlease enter a valid initial state (row, col): ")
        startLoc = [(int)(x.strip()) for x in re.split("\(|\)|,", startStr) if x.strip() != '']

    goalStr = input("Please enter a goal state (row, col): ")
    goalLoc = [(int)(x.strip()) for x in re.split("\(|\)|,", goalStr) if x.strip() != '']

    while not validSpace(grid, goalLoc[0], goalLoc[1]):
        goalStr = input("That goal state entered is invalid.\nPlease enter a valid goal state (row, col): ")
        goalLoc = [(int)(x.strip()) for x in re.split("\(|\)|,", goalStr) if x.strip() != '']

    return startLoc, goalLoc


def main():
    file = "gridFile.txt"
    grid = readGrid(file)

    # Test Values:
    # start = [1, 1]
    # goal = [4, 1]

    start, goal = getInputs(grid)

    # BFS search
    path = uninformedSearch(grid, start, goal, 'BFS')

    # convert path of node to path of Locations
    pathLoc = [node.value for node in path]
    outputGrid(grid, start, goal, pathLoc, "pathBFS.txt")


    # DFS search
    grid = readGrid(file)
    path = uninformedSearch(grid, start, goal, 'DFS')

    # convert path of node to path of Locations
    pathLoc = [node.value for node in path]
    outputGrid(grid, start, goal, pathLoc, "pathDFS.txt")

    print("pathBFS.txt and pathDFS.txt have been updated")
    input("Press Enter to Close")


if __name__ == "__main__":
    main()
