import random
import sys

# Architectural Safety Net: CPython's default recursion limit is 1000 frames. 
# Large mazes will exceed this call stack depth during DFS.
sys.setrecursionlimit(10000)

class MazeGenerator:
    # Class-level constants (Allocated once in the class object's __dict__)
    DIRECTIONS = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    SOLVER_MOVES = [((0, -1), "N"), ((0, 1), "S"), ((-1, 0), "W"), ((1, 0), "E")]

    def __init__(self, width: int, height: int):
        # Instance attributes (Allocated in the instance's specific __dict__)
        self.width = width
        self.height = height
        self.wall = "#"
        self.path = " "
        self.grid = self._init_grid()

    def _init_grid(self) -> list:
        grid = []
        for _ in range(self.height):
            grid.append([self.wall] * self.width)
        return grid

    def _check_valid(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        if self.grid[y][x] != self.wall:
            return False
        return True

    def _make_route(self, x: int, y: int) -> None:
        self.grid[y][x] = self.path
        directions = list(self.DIRECTIONS)
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if self._check_valid(nx, ny):
                mid_x = x + dx // 2
                mid_y = y + dy // 2
                self.grid[mid_y][mid_x] = self.path
                self._make_route(nx, ny)

    def generate_maze(self) -> list:
        if self.width < 9 or self.height < 7:
            print("Error: Maze dimensions too small to inject the '42' pattern.")
        else:
            forty_two = [
                (0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (2,3), (2,4),
                (4,0), (5,0), (6,0), (6,1), (4,2), (5,2), (6,2), (4,3), (4,4), (5,4), (6,4)
            ]
            start_x = (self.width - 7) // 2
            start_y = (self.height - 5) // 2
            for dx, dy in forty_two:
                self.grid[start_y + dy][start_x + dx] = "42"

        self._make_route(1, 1)

        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == "42":
                    self.grid[r][c] = self.wall
        return self.grid

    def solve_maze(self, start_x: int, start_y: int, exit_x: int, exit_y: int) -> str:
        queue = [(start_x, start_y, "")]
        visited = set()
        visited.add((start_x, start_y))
        
        while queue:
            curr_x, curr_y, path_str = queue.pop(0)
            if curr_x == exit_x and curr_y == exit_y:
                return path_str
            
            for (dir_x, dir_y), dir_char in self.SOLVER_MOVES:
                nx = curr_x + dir_x
                ny = curr_y + dir_y
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if self.grid[ny][nx] == self.path and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, path_str + dir_char))
        return ""

    def export_maze(self, start_x: int, start_y: int, exit_x: int, exit_y: int, path_str: str, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            for y in range(self.height):
                row_hex = []
                for x in range(self.width):
                    cell_val = 0
                    if y == 0 or self.grid[y-1][x] == self.wall:
                        cell_val |= 1
                    if x == self.width - 1 or self.grid[y][x+1] == self.wall:
                        cell_val |= 2
                    if y == self.height - 1 or self.grid[y+1][x] == self.wall:
                        cell_val |= 4
                    if x == 0 or self.grid[y][x-1] == self.wall:
                        cell_val |= 8
                    row_hex.append(f"{cell_val:X}")
                f.write("".join(row_hex) + "\n")
            f.write("\n")
            f.write(f"{start_x},{start_y}\n")
            f.write(f"{exit_x},{exit_y}\n")
            f.write(f"{path_str}\n")