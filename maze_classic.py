# Your task in Project 1 is to add a function to the Maze.py program to count steps
# what is needed to reach the end point from the starting point?

import time

class Maze:

    MOVE = (
        (-1, 0),  # UP
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    )

    def solve(self, maze):
        # Initialize the maze by adding an array
        self.MAZE = maze
        # Create a size of maze (y -> row, x -> col)
        self.SIZE = (len(maze), len(maze[0]))
        # Create a finish point
        self.FINISH = (self.SIZE[0] - 1, self.SIZE[1] - 1)
        # Create a path (array 2 d that filled with zero)
        self.PATH = [[0 for i in range(self.SIZE[1])] for i in range(self.SIZE[0])]
        # Set the starting point
        self.PATH[0][0] = 1
        # Initialize steps counter (to count how many steps to reach the finish point)
        self.steps = 1
        # Display how the maze look
        print("Maze")
        Maze.display(maze)
        # Run the maze (this function using recursive to find the solution)
        if self._run_(0, 0):
            print(f"Solution (Total Steps: {self.steps})")
            Maze.display(self.PATH)
        else:
            print("Solution does not exist")
    
    # Helper static function to display 2D array
    @staticmethod
    def display(matrix):
        for r in matrix:
            for c in r:
                print("." if c else "#", end=" ")
            print()
        print()

    # Private recursive function for solving the maze
    def _run_(self, row, col):
        # If the current position is the finish point
        if (row, col) == self.FINISH:
            return True
        
        # Display the path using delay 1 second
        time.sleep(0.5)
        Maze.display(self.PATH)

        # Looping through the MOVE tuple and using recursive to find the solution
        for move_row, move_col in Maze.MOVE:
            # Create a new row and col based on value from Maze.MOVE
            new_row = row + move_row #1
            new_col = col + move_col 
            # Check if the new row and col is valid
            if self._is_valid_(new_row, new_col):
                # Change the value of the new row and col to 1
                self.PATH[new_row][new_col] = 1
                # Increment the steps counter
                self.steps += 1  
                # Using recursive to find the solution
                if self._run_(new_row, new_col):
                    #Return True if the solution is found
                    return True
                # Backtracking (if the solution is not found)
                self.PATH[new_row][new_col] = 0
                # Decrement the steps counter when backtracking
                self.steps -= 1 
        
        
        return False

    # Private function to check the validity of a move
    def _is_valid_(self, row, col):
        if row < 0 or col < 0 or row >= self.SIZE[0] or col >= self.SIZE[1]:
            return False
        if self.MAZE[row][col] == 0:
            return False
        if self.PATH[row][col] == 1:
            return False
        return True


# Driver program to test Maze class
if __name__ == "__main__":
    # Define a object from Maze class
    solver = Maze()

    # Example 1
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    solver.solve(maze)
    print()

    # Example 2
    maze = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 1]]
    solver.solve(maze)
    print()

    # Example 3
    maze = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1]]
    solver.solve(maze)
    print()

    # Example 4
    maze = [[1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]]
    solver.solve(maze)