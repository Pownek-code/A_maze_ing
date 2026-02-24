import sys
from src.config import parse_config
from mazegen.generator import MazeGenerator

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config.txt>")
        sys.exit(1)
    config_path = sys.argv[1]
    config = parse_config(config_path)
    print("Initializing Maze Generator...")
    maze = MazeGenerator(config["WIDTH"], config["HEIGHT"])
    print("Carving the spanning tree...")
    maze.generate_maze()
    start_x, start_y = config["ENTRY"]
    exit_x, exit_y = config["EXIT"]
    print("Executing Breadth-First Search...")
    solution_path = maze.solve_maze(start_x, start_y, exit_x, exit_y)
    if not solution_path:
        print("Warning: No valid path found between Entry and Exit.")
    output_file = config["OUTPUT_FILE"]
    print(f"Exporting raw hexadecimal bitmasks to {output_file}...")
    maze.export_maze(start_x, start_y, exit_x, exit_y, solution_path, output_file)
    print("Success: Process complete.")

if __name__ == "__main__":
    main()