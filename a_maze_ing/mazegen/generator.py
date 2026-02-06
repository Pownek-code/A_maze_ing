import random
wall = "#"
path = " "
def make_route(grid: list, x: int, y: int):
    grid[y][x] = path
    print(grid)


def init_grid(width: int, height: int) -> list:
    grid = []
    for i in range(height):
        grid.append([wall] * width)
    # if check_valid(width, height, grid) == True:
    #     result = make_route(grid, width, height)
    # else:
    #     result = grid.clear()
    print(len(grid[0]))
    return grid

def check_valid(x: int, y: int, grid: list) -> bool:
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    if grid[y][x] != wall:
        return False
    return True

print(check_valid(5, 4, init_grid(4, 5)))