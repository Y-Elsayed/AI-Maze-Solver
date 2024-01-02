# <p align='center'>MazeWorld</p>
# Project Setup and Execution

## Running the Program

To run the program, follow these steps:

1. Launch the project by executing the `main.py` file located in the `SRC` directory:

    ```bash
    SRC/python main.py
    ```

2. In the `main.py` file, customize the visualization of algorithms by uncommenting the corresponding line (Line 9):

    - To visualize A* algorithm:
        ```python
        #searchPath, algorithmPath, forwardPath = Astar(m)
        ```

    - To visualize BFS algorithm:
        ```python
        #searchPath, algorithmPath, forwardPath = BFS(m)
        ```

    - To visualize DFS algorithm:
        ```python
        #searchPath, algorithmPath, forwardPath = DFS(m)
        ```

   Explore different algorithms by uncommenting the desired line and executing the `main.py` file.