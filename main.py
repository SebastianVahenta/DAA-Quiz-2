import time

from utils.generate_grid import generate_grid
from utils.print_maze import print_maze
from utils.carve import carve
from utils.modify import modify
from algorithms.dijkstra_maze_solver import dijkstra_maze_solver

def main():

  m = 41
  n = 41
  maze = []

  maze = generate_grid(n, m, maze)
  carve(maze)
  modify(maze, m, n)

  maze_for_dijkstra = maze.copy()

  start_time_dijkstra = time.time()
  dijkstra_maze_solver(maze_for_dijkstra, [1, 1], [m-2, n-2])
  print("Execution time Dijkstra: %s seconds" % (time.time() - start_time_dijkstra))
  print_maze(maze_for_dijkstra)

if __name__ == "__main__":
  main()
