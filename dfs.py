# Function implementing Depth-First Search (DFS)
def dfs(maze, start, end):
    # Get the number of rows and columns in the maze
    rows, cols = len(maze), len(maze[0])
    
    # Initialize the frontier to store cells to explore along with their paths
    frontier = []
    frontier.append((start, []))  # Start cell and an empty path
    
    # Set to store explored cells to avoid revisiting them
    explored = set()

    # Loop until there are cells to explore
    while frontier:
        # Pop the current cell and its path from the frontier
        currcell, path = frontier.pop()
        
        # Check if the current cell is the end cell
        if currcell == end:
            return path + [currcell]  # Return the path to the end cell
        
        # Mark the current cell as explored
        explored.add(currcell)

        # Explore neighboring cells in LRUD (Left, Right, Up, Down) directions
        for d in 'LRUD':
            if d == 'R':
                childcell = (currcell[0], currcell[1] + 1)
            elif d == 'L':
                childcell = (currcell[0], currcell[1] - 1)
            elif d == 'U':
                childcell = (currcell[0] - 1, currcell[1])
            elif d == 'D':
                childcell = (currcell[0] + 1, currcell[1])

            # Check if the child cell is within the maze bounds, not a wall, and not explored
            if (
                0 <= childcell[0] < rows
                and 0 <= childcell[1] < cols
                and maze[childcell[0]][childcell[1]] != 'W'
                and childcell not in explored
            ):
                # Add the child cell and update path to the frontier
                frontier.append((childcell, path + [currcell]))

    return None  # Return None if no path is found

# Maze definition and start/end points
maze=[['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' ', 'W'], ['W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W'], ['W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]

start = (5, 1)
end = (5, 7)

# Find path using DFS and print the result
print("Path (DFS):", dfs(maze, start, end))
