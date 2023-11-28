# Your task in Project 3 is to modify the Maze.py program resulting from Project 2 so that it can produce the shortest path.
# from collections import deque

from collections import deque 
import time

class Maze:
    MOVE = (
        (-1, 0),  # UP
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    )

    def solve(self, maze, start=(0, 0), finish=None):
        # Initialize the maze by adding an array
        self.MAZE = maze
        # Create a size of maze (y -> row, x -> col)
        self.SIZE = (len(maze), len(maze[0]))
        # Create a finish point
        self.FINISH = finish if finish is not None else(self.SIZE[0] - 1, self.SIZE[1] - 1)
        # Create a path (array 2 d that filled with zero)
        self.PATH = [[0 for i in range(self.SIZE[1])] for i in range(self.SIZE[0])]
        # Set the starting point
        start_row, start_col = start
        # Set the starting point
        self.PATH[start_row][start_col] = 1
        # Create deque to store object that following the line.
        queue = deque([(start, [])])
        # Crate set to store visited object
        visited = set()
        # Display how the maze look
        print("Maze")
        Maze.display(maze)

        # Looping through the queue
        while queue:
            # Get the current position and path
            (current, path) = queue.popleft()
            # Get the row and col from current position
            row, col = current

            # If the current position is the finish point
            # stop the program with return and print the route
            if current == self.FINISH:
                self._update_path_(path + [current])
                print(f"Solution (Total Steps: {self._steps_(path + [current])})")
                Maze.display(self.PATH)
                return
            
            # If the current position is not the finish point
            # add the current position to visited set
            # and looping through the MOVE tuple
            if current not in visited:
                visited.add(current)
                for move_row, move_col in Maze.MOVE:
                    new_row, new_col = row + move_row, col + move_col
                    new_position = (new_row, new_col)
                    if self._is_valid_(new_row, new_col) and new_position not in visited:
                        queue.append((new_position, path + [current]))

        print("No solution found")

    def _update_path_(self, path):
        self.PATH = [[0 for _ in range(self.SIZE[1])] for _ in range(self.SIZE[0])]
        for row, col in path:
            self.PATH[row][col] = 1
            # Display the path using delay 1 second
            time.sleep(1)
            Maze.display(self.PATH)

    def _steps_(self, path):
        return len(path)

    # Helper static function to display 2D array
    @staticmethod
    def display(matrix):
        for r in matrix:
            for c in r:
                print("." if c else "#", end=" ")
            print()
        print()

    # Private function to check the validity of a move
    def _is_valid_(self, row, col):
        if 0 <= row < self.SIZE[0] and 0 <= col < self.SIZE[1] and self.MAZE[row][col] == 1:
            return True
        return False


# Driver program to test Maze class
if __name__ == "__main__":
    # Define a object from Maze class
    solver = Maze()

    # Example 1
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    solver.solve(maze, start=(1, 1), finish=(2, 3))
    print()

    # Example 2
    maze = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 1]]
    solver.solve(maze, start=(0, 0), finish=(3, 3))
    print()

    # Example 3
    maze = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1]]
    solver.solve(maze, start=(0, 0), finish=(4, 4))
    print()

    # Example 4
    maze = [[1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]]
    solver.solve(maze, start=(3, 0), finish=(1, 4))