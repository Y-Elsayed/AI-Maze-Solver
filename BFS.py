from pyamaze import maze, agent, COLOR

def BFS(maze, start = None, goal = (1,1)):
    if start == None:
        start = (maze.rows, maze.cols)

    frontier = [start]
    explored = [start]

    bfsPath = {}
    searchPath = []

    while len(frontier) > 0:
        currentCell = frontier.pop(0)
        if currentCell == goal:
            break
        for d in 'ENSW':
            if maze.maze_map[currentCell][d] == True:
                if d == 'E':
                    childCell = (currentCell[0], currentCell[1] + 1)
                elif d == 'W':
                    childCell = (currentCell[0], currentCell[1] - 1)
                elif d == 'N':
                    childCell = (currentCell[0] - 1, currentCell[1])
                elif d == 'S':
                    childCell = (currentCell[0] + 1, currentCell[1])
                if childCell in explored:
                    continue

                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currentCell
                searchPath.append(childCell)
    
    forwardPath = {}
    fcell = goal
    while fcell != start:
        forwardPath[bfsPath[fcell]] = fcell
        fcell = bfsPath[fcell]
    return searchPath, bfsPath, forwardPath
