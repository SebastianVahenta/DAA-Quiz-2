from utils.generate_grid import generate_grid
from utils.print_maze import print_maze
from utils.carve import carve
from utils.modify import modify
from algorithms.dijkstra_maze_solver import dijkstra_maze_solver

def main():

  m = 21
  n = 21
  maze = []

  maze = generate_grid(n, m, maze)
  carve(maze)
  modify(maze, m, n)
  
  print("The maze:")
  print_maze(maze)

  maze_for_dijkstra = maze.copy()

  print("Solved maze with Dijkstra:")
  dijkstra_maze_solver(maze_for_dijkstra, [1, 1], [m-2, n-2])
  print_maze(maze_for_dijkstra)

if __name__ == "__main__":
  main()