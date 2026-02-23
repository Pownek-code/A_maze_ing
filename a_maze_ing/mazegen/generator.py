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
    if width < 9 or height < 7:
        print("Error: Maze dimensions too small to inject the '42' pattern.")
    else:
        forty_two = [
            (0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (2,3), (2,4),
            (4,0), (5,0), (6,0), (6,1), (4,2), (5,2), (6,2), (4,3), (4,4), (5,4), (6,4)
        ]
        start_x = (width - 7) // 2
        start_y = (height - 5) // 2
        for dx, dy in forty_two:
            target_x = start_x + dx
            target_y = start_y + dy
            grid[target_y][target_x] = "42"
    make_route(grid, 1, 1)
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
