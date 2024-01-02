from pyamaze import maze, agent, COLOR
from Astar import Astar
from BFS import BFS
from DFS import DFS

m = maze(15,15)
m.CreateMaze(3, 5, loopPercent=100, loadMaze='maze2.csv')

searchPath, algorithmPath, forwardPath = DFS(m, goal=(3,5))

searchAgent = agent(m, footprints=True, filled=True, color=COLOR.blue)
algorithmAgent = agent(m, 3, 5, footprints=True, filled=True, color=COLOR.yellow, goal=(m.rows, m.cols))
forwardAgent = agent(m, footprints=True, color=COLOR.dark)

m.tracePath({searchAgent:searchPath}, delay=50)
m.tracePath({algorithmAgent:algorithmPath}, delay=100)
m.tracePath({forwardAgent:forwardPath}, delay=100)

m.run()