# Using the maze generation and agents from the pyamaze
# to help in visualize the algorithm
# from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

def h(cell1, cell2):
    '''heuristic
    
    Uses the manhatten principle to calculate the estimate
    from cell1 to cell2

    Arguments:
        cell1 (tuple): The 1st cell.
        cell2 (tuple): The 2nd cell.
    '''
    x1, y1 = cell1
    x2, y2 = cell2

    return (abs(x1-x2) + abs(y1-y2))

def Astar(maze, startingCell=None, goalCell=(1,1)):
    '''A* Algorithm
    
    The search algorithm to be used in our maze search traversing.
    Uses the heuristic to be able to calculate the estimates towards
    the goal.

    Arguments:
        maze (): The maze.
    '''
    if startingCell == None:
        startingCell = (maze.rows, maze.cols)

    open = PriorityQueue()
    # (heuristic cost + g cost, heuristic cost, cell itself)
    open.put((h(startingCell, goalCell) + 0, h(startingCell, goalCell), startingCell))
    
    # The path that the algorithm traverses
    aPath = {}
    
    # The path that the algorithm has searched
    searchPath = [startingCell]

    # Calculates the inital scores to infinity and place the
    # g(startingCell) to 0 and calculates the heuristic for the
    # startingCell
    g_score = {cell: float('infinity') for cell in maze.grid}
    g_score[startingCell] = 0
    f_score = {cell: float('infinity') for cell in maze.grid}
    f_score[startingCell] = h(startingCell, goalCell)

    while not open.empty():
        currentCell = open.get()[2] # Gets the third element aka the cell itself
        searchPath.append(currentCell)
        if currentCell == goalCell:
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
    fcell = goalCell
    while fcell != startingCell:
        forwardPath[aPath[fcell]] = fcell
        fcell = aPath[fcell]
    
    return searchPath, aPath, forwardPath

# This block of code is to visualize the use of the
# A* algorithm

# if __name__ == '__main__':
#     m = maze(15,15)
#     m.CreateMaze(loopPercent=50, loadMaze="Astar_test2.csv")

#     searchPath, astarPath, forwardPath = Astar(m)

#     searchAgent = agent(m, footprints=True, filled=True, color=COLOR.blue)
#     astarAgent = agent(m, 1, 1, footprints=True, filled=True, color=COLOR.yellow, goal=(m.rows, m.cols))
#     forwardAgent = agent(m, footprints=True, color=COLOR.dark)

#     m.tracePath({searchAgent:searchPath}, delay=250)
#     m.tracePath({astarAgent:astarPath}, delay=200)
#     m.tracePath({forwardAgent:forwardPath}, delay=250)

#     m.run()