from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

def h(cell1, cell2):
    '''heuristic
    
    Uses the manhatten principle to calculate the estimate
    from cell1 to cell2

    Arguments:
        cell1 (tuple): The 1st cell. Which will be the cell the agent is
                       standing on.
        cell2 (tuple): The 2nd cell. Which is the cell the agent is trying
                       to reach.
    '''
    x1, y1 = cell1
    x2, y2 = cell2

    return (abs(x1-x2) + abs(y1-y2))

def Astar(maze, start=None, goal=(1,1)):
    '''A* Algorithm
    
    The search algorithm to be used in our maze search traversing.
    Uses the heuristic to be able to calculate the estimates towards
    the goal.

    Arguments:
        maze (class): The maze class from the pyamaze maze module.
        startingCell (tuple): A tuple of the starting cell for the algorithm to
                              start from. Defaults to the bottom right of the maze.
        goalCell (tuple): A tuple of the goal cell for the algorithm to reach. Defaults
                          to the top left of the maze.
    '''
    if start == None:
        start = (maze.rows, maze.cols)

    open = PriorityQueue()
    # (heuristic cost + g cost, heuristic cost, cell itself)
    open.put((h(start, goal) + 0, h(start, goal), start))
    
    # The path that the algorithm traverses
    aPath = {}
    
    # The path that the algorithm has searched
    searchPath = [start]

    # Calculates the inital scores to infinity and place the
    # g(startingCell) to 0 and calculates the heuristic for the
    # startingCell
    g_score = {cell: float('infinity') for cell in maze.grid}
    g_score[start] = 0
    f_score = {cell: float('infinity') for cell in maze.grid}
    f_score[start] = h(start, goal)

    while not open.empty():
        currentCell = open.get()[2] # Gets the third element aka the cell itself
        searchPath.append(currentCell)
        if currentCell == goal:
            # If the goal is found exit the loop
            break

        for d in 'NSEW':
            if maze.maze_map[currentCell][d] == True:
                if d == 'E':
                    childCell = (currentCell[0], currentCell[1] + 1)
                if d == 'W':
                    childCell = (currentCell[0], currentCell[1] - 1)
                if d == 'N':
                    childCell = (currentCell[0] - 1, currentCell[1])
                if d == 'S':
                    childCell = (currentCell[0] + 1, currentCell[1])
                
                temp_g_score = g_score[currentCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score

                    open.put((temp_f_score, h(childCell, (1,1)), childCell))
                    aPath[childCell] = currentCell
    
    # After reaching to the goal we traverse back to the starting point
    # to figure out the optimal path to be taken
    forwardPath = {}
    fcell = goal
    while fcell != start:
        forwardPath[aPath[fcell]] = fcell
        fcell = aPath[fcell]
    
    return searchPath, aPath, forwardPath
