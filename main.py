from mazeworld import maze, agent, COLOR
from Astar import Astar
from BFS import BFS
from DFS import DFS

m = maze(30, 30)
m.CreateMaze(loopPercent=80, loadMaze='30x30_maze.csv')

searchPath, algorithmPath, forwardPath = Astar(m)

# searchAgent = agent(m, footprints=True, filled=True, color=COLOR.blue)
# algorithmAgent = agent(m, 1, 1, footprints=True, filled=True, color=COLOR.green, goal=(m.rows, m.cols))
# forwardAgent = agent(m, 30, 1, footprints=True, color=COLOR.dark)

# m.tracePath({searchAgent:searchPath}, delay=300)
# m.tracePath({algorithmAgent:algorithmPath}, delay=250)
# m.tracePath({forwardAgent:forwardPath}, delay=225)

# algorithmAgent = agent(m, 1, 1, footprints=True, filled=True, color=COLOR.green)
# searchAgent = agent(m, footprints=True, filled=True, color=COLOR.blue)
# forwardAgent = agent(m, 30, 1, footprints=True, color=COLOR.yellow)

m.run()