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
    grid = init_grid(width, height)
    # TODO: Inject 42 Stencil
    make_route(grid, 0, 0)
    return grid



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
