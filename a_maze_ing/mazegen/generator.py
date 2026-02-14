import random
wall = "#"
path = " "
DIRECTIONS = [(0, -2), (0, 2), (-2, 0), (2, 0)]
def make_route(grid: list, x: int, y: int) -> None:
    grid[y][x] = path
    directions = list(DIRECTIONS)
    random.shuffle(directions)
    # print(directions)
    # print(grid)


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
