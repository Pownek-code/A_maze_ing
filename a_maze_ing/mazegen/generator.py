import random
wall = "#"
path = " "
DIRECTIONS = [(0, -2), (0, 2), (-2, 0), (2, 0)]
def make_route(grid: list, x: int, y: int) -> None:
    grid[y][x] = path
    directions = list(DIRECTIONS)
    random.shuffle(directions)
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y
        if check_valid(nx, ny, grid):
            mid_x = x + dx // 2
            mid_y = y + dy // 2
            grid[mid_y][mid_x] = path
            make_route(grid, nx, ny)

def generate_maze(width: int, height: int) -> list:
    grid: list = init_grid(width, height)
    # this is used to Inject 42 patern!
    if width < 9 or height < 7:
        print("Error: Maze dimensions too small to inject the '42' pattern.")
    else:
        forty_two: list[tuple[int, int]] = [
            (0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (2,3), (2,4),
            (4,0), (5,0), (6,0), (6,1), (4,2), (5,2), (6,2), (4,3), (4,4), (5,4), (6,4)
        ]
        start_x: int = (width - 7) // 2
        start_y: int = (height - 5) // 2
        for dx, dy in forty_two:
            target_x: int = start_x + dx
            target_y: int = start_y + dy
            grid[target_y][target_x] = "42"
    make_route(grid, 1, 1)
    for r in range(height):
        for c in range(width):
            if grid[r][c] == "42":
                grid[r][c] = wall
    return grid

# Breadth-First Search (BFS) algorithm.

def solve_maze(grid: list, start_x: int, start_y: int, exit_x: int, exit_y: int) -> str:
    queue = [(start_x, start_y, "")]
    visited = set()
    visited.add((start_x, start_y))
    moves = [((0, -1), "N"), ((0, 1), "S"), ((-1, 0), "W"), ((1, 0), "E")]
    while queue:
        curr_x, curr_y, path_str = queue.pop(0)
        if curr_x == exit_x and curr_y == exit_y:
            return path_str
        for (dir_x, dir_y), dir_char in moves:
            nx = curr_x + dir_x
            ny = curr_y + dir_y
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == path and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, path_str + dir_char))
    return ""

# generating a hexa sequence for every cell in my grid.
def export_maze(grid: list, start_x: int, start_y: int, exit_x: int, exit_y: int, path_str: str, filename: str) -> None:
    height: int = len(grid)
    width: int = len(grid[0])
    with open(filename, "w", encoding="utf-8") as f:
        for y in range(height):
            row_hex: list = []
            for x in range(width):
                cell_val: int = 0
                if y == 0 or grid[y-1][x] == wall:
                    cell_val |= 1
                if x == width - 1 or grid[y][x+1] == wall:
                    cell_val |= 2
                if y == height - 1 or grid[y+1][x] == wall:
                    cell_val |= 4
                if x == 0 or grid[y][x - 1] == wall: # Note: Typo fixed here mentally, should be grid[y][x-1] for west
                    cell_val |= 8
                row_hex.append(f"{cell_val:X}")
            f.write("".join(row_hex) + "\n")
        f.write("\n")
        f.write(f"{start_x},{start_y}\n")
        f.write(f"{exit_x},{exit_y}\n")
        f.write(f"{path_str}\n")


def init_grid(width: int, height: int) -> list:
    grid = []
    for _ in range(height):
        grid.append([wall] * width)
    return grid

def check_valid(x: int, y: int, grid: list) -> bool:
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    if grid[y][x] != wall:
        return False
    return True
