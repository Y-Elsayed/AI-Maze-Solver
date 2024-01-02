
def bfs(maze,start,end):
    #number of the rows and columns
    rows, cols = len(maze), len(maze[0])
    #frontier is a list of the cells that needs to be explored
    frontier = []
    #it starts with the initial cell [start] and an empty path
    frontier.append((start, []))
    #explored is a set of visited cells 
    explored=set()
    #executes as long as there are cells in the list
    while frontier:
        currcell,path=frontier.pop(0)
        if currcell== end:
             return path + [currcell]
        
        explored.add(currcell)

        for d in 'LRUD':
                if d =='R':
                    childcell=(currcell[0],currcell[1]+1)
                elif d == 'L':
                    childcell=(currcell[0],currcell[1]-1)
                elif d == 'U':
                    childcell=(currcell[0]-1,currcell[1])
                elif d == 'D':
                    childcell=(currcell[0]+1,currcell[1])
            #ensures that the cell is in the range of rows, columns, not equal w and not explored
                if 0 <= childcell[0] < rows and 0 <= childcell[1] < cols and maze[childcell[0]][childcell[1]] != 'W' and childcell not in explored:
                    frontier.append((childcell, path + [currcell]))
    return None 



maze=[['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' ', 'W'], ['W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W'], ['W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
start=(5,1)
end= (5,7)

print("Shortest Path:",bfs(maze, start, end))
