import random


#Randomized DFS maze generation Algorithm
def generate_maze(rows, cols):
    # Initialize the maze with walls
    maze = [['W' for _ in range(cols)] for _ in range(rows)]

    # get neighboring walls 
    def get_walls(row, col):
        neighbors = []
        if row > 1 and maze[row - 2][col] == 'W':
            neighbors.append((row - 2, col))
        if row < rows - 2 and maze[row + 2][col] == 'W':
            neighbors.append((row + 2, col))
        if col > 1 and maze[row][col - 2] == 'W':
            neighbors.append((row, col - 2))
        if col < cols - 2 and maze[row][col + 2] == 'W':
            neighbors.append((row, col + 2))
        return neighbors

    # Recursive DFS function
    def dfs(row, col):
        # Mark the current cell as part of the maze (visited)
        maze[row][col] = ' '

        # Add neighboring walls to the list
        neighbors = get_walls(row, col)

        # Shuffle the neighbors randomly
        random.shuffle(neighbors)

        for next_row, next_col in neighbors:
            #check if it is not visited
            if maze[next_row][next_col] == 'W':
                # Carve a path
                maze[(row + next_row) // 2][(col + next_col) // 2] = ' '
                dfs(next_row, next_col)

    # Choose a random starting point and mark it as part of the maze, should be odd
    start_row = random.randrange(1, rows - 1, 2)
    start_col = random.randrange(1, cols - 1, 2)
    # start_row = 1
    # start_col = 1

    # Run DFS from the starting point
    dfs(start_row, start_col)
    return maze

# Example usage:
rows = 25
cols = 25
maze = generate_maze(rows, cols)
new_maze = [[' ' for _ in range(cols)] for _ in range(rows)]


for i in range(rows):
    for j in range(cols):
        if (j < cols-2 and maze[i][j] == maze[i][j+1]== 'W') or (j > 1 and maze[i][j] == maze[i][j-1]== 'W'):
            new_maze[i][j] = '-'
        elif (i < rows-2 and maze[i][j] == maze[i+1][j] == 'W') or (i > 1 and maze[i][j] == maze[i-1][j] == 'W'):
            new_maze[i][j] = '|'
        if j == 0 or j == cols-1:
            new_maze[i][j] = '|'
        if i == 0 or i == rows-1:
            new_maze[i][j] = '-'
            
new_maze[0][0] = new_maze[0][cols-1] = new_maze[rows-1][0] = new_maze[rows-1][cols-1] = '+'
# Print the generated maze
for row in new_maze:
    print(' '.join(row))
