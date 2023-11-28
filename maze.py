'''
Author: Mahendra Data - https://github.com/mahendradata
References: https://www.geeksforgeeks.org/rat-in-a-maze/
'''


class Maze:

    MOVE = (
        (-1, 0),  # UP
        (1, 0),  # Down
        (0, -1),  # Left
        (0, 1),  # Right
    )

    # Public function for solving the maze
    def solve(self, maze):
        self.MAZE = maze
        self.SIZE = (len(maze), len(maze[0]))
        self.FINISH = (self.SIZE[0]-1, self.SIZE[1]-1)

        self.PATH = [[0 for i in range(self.SIZE[1])] for i in range(self.SIZE[0])]
        self.PATH[0][0] = 1

        print("Maze")
        Maze.display(maze)

        if self.__run__(0, 0):
            print(f"Solution")
            Maze.display(self.PATH)
        else:
            print("Solution does not exist")

    # Helper function to display 2D array
    def display(matrix):
        for r in matrix:
            for c in r:
                print(c, end=" ")
            print()

    # Private recursive function for solving the maze
    def __run__(self, row, col):
        if (row, col) == self.FINISH:
            return True

        for move_row, move_col in Maze.MOVE:
            new_row = row + move_row
            new_col = col + move_col
            if self.__is_valid__(new_row, new_col):
                self.PATH[new_row][new_col] = 1
                if self.__run__(new_row, new_col):
                    return True
                self.PATH[new_row][new_col] = 0

        return False

    # Private function to check the validity of a move
    def __is_valid__(self, row, col):
        # If out of the maze's border
        if row < 0 or col < 0 or row >= self.SIZE[0] or col >= self.SIZE[1]:
            return False

        # If hit the maze's wall
        if self.MAZE[row][col] == 0:
            return False

        # If the path has been visited
        if self.PATH[row][col] == 1:
            return False

        return True  # If the move is valid
    

# Driver program to test Maze class
if __name__ == "__main__":
    solver = Maze()

    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    solver.solve(maze)
    print()

    maze = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 1]]
    solver.solve(maze)
    print()

    maze = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1]]
    solver.solve(maze)
    print()

    maze = [[1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]]
    solver.solve(maze)
