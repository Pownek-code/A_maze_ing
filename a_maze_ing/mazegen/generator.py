wall = "#"
path = " "
def init_grid(width: int, height: int):
    grid = []
    for i in range(height):
        grid.append([wall] * width)
    return grid