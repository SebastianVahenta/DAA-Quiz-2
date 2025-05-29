
# DAA Quiz 2 – Maze Maker & Solver
## Group Member
| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Sebastian Vahenta Setjo | 5025231294 | DAA - G |
| Bayu Nismara Nagatama | 5025231152 | DAA - G |
| Izzudin Ali Akbari | 5025231313 | DAA - H |

This project uses DFS and Dijkstra to generate and solve a maze using python in an easy way, to generate the maze we follow the following steps:

- Generate a matrix full of 0's which represents obtacles
- Generate a grid in the matrix with 1's which representes paths that the algorithm will be able to follow
- Using DFS we "carve" the maze generating paths between spaces in the grid which, seen from a graph approach, the spaces in the grid are nodes, the objective is to connect this nodes.

For the solution part, we use Dijksta

#### Dijkstra

Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph. Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.

The algorithm uses a greedy approach in the sense that we find the next best solution hoping that the end result is the best solution for the whole problem. 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- Have python installed in your computer

- Install with pip the following: random, numpy and time.

- Clone the repo
   ```sh
    git clone https://github.com/SebastianVahenta/DAA-Quiz-2.git
   ```
- The entry point of the code is main.py


🧩 Project Design and Algorithm Analysis
🛠️ Project Design
Objective:
Implement a maze generation and solving system using Dijkstra’s algorithm that supports weighted terrain, with visual output of both the unsolved and solved maze, along with execution time.

Key Features:

Maze generation with clear wall ('0') and path ('1') structure.

Carving algorithm to ensure connectivity.

Terrain assignment:

'1': Normal path (cost 1)

'M': Mud (cost 5)

'W': Water (cost 10)

Pathfinding using Dijkstra’s algorithm (self-contained).

Visual display with emojis for easy interpretation.

Displays maze before and after solving.

Shows execution time of the solver.

🧠 Algorithm Analysis: Dijkstra's Algorithm
Type: Graph traversal / shortest path (uniform-cost search)

Used for:
Finding the lowest-cost path from start to end in a grid with variable-cost tiles.

Complexity:

Time Complexity: O(E log V) when using a priority queue (heapq)

Space Complexity: O(V) for storing distances, previous nodes, and the visited set

Advantages:

Guaranteed to find the optimal (lowest-cost) path

Works with non-negative edge weights (perfect for terrain)

Drawbacks:

Slower than A* if heuristic guidance is useful

Explores more nodes than necessary in large open grids

💾 Source Code Summary
main.py
Handles maze generation, shows unsolved maze, runs Dijkstra, shows solution and timing.

python
Salin
Edit
def main():
    m = 41
    n = 41
    maze = generate_grid(n, m, [])
    carve(maze)
    modify(maze, m, n)

    print("🧱 Maze before solving:\n")
    print_maze(maze)

    maze_for_dijkstra = [row[:] for row in maze]

    start_time_dijkstra = time.time()
    dijkstra_maze_solver(maze_for_dijkstra, [1, 1], [m-2, n-2])
    elapsed_time = time.time() - start_time_dijkstra

    print("\n✅ Maze after solving with Dijkstra:")
    print(f"Execution time: {elapsed_time:.4f} seconds\n")
    print_maze(maze_for_dijkstra)
generate_grid.py (NumPy-free)
Generates an odd-dimensioned grid of walls and paths.

python
Salin
Edit
def generate_grid(n, m, maze):
    maze = [['0' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            maze[i][j] = '1' if i % 2 != 0 and j % 2 != 0 else '0'
    return maze
carve.py
Carves paths using randomized DFS between '1' cells.

modify.py
Assigns weighted terrain randomly to existing '1' paths.

python
Salin
Edit
def modify(maze, m, n):
    for _ in range(100):
        x = random.randint(1, n - 2)
        y = random.randint(1, m - 2)
        if maze[x][y] == '1':
            maze[x][y] = random.choices(['1', 'M', 'W'], weights=[0.6, 0.3, 0.1])[0]
dijkstra_maze_solver.py (Self-contained)
Uses heapq to find the lowest-cost path using terrain weights.

✅ No external file dependencies!

print_maze.py
Displays walls, path, and terrain with clear emojis:

Tile	Meaning	Emoji
'0'	Wall	🟥
'1'	Normal	🟨
'M'	Mud	🟫
'W'	Water	🟦
'2'	Path	🟩

🧪 Sample Output
python-repl
Salin
Edit
🧱 Maze before solving:

🟥🟥🟥🟥🟥...
🟥🟨🟫🟨🟥...
🟥🟦🟥🟨🟥...
...

✅ Maze after solving with Dijkstra:
Execution time: 0.0153 seconds

🟥🟥🟥🟥🟥...
🟥🟩🟩🟫🟥...
🟥🟦🟥🟩🟥...
...
📊 Analysis and Insights
The maze is correctly solved with Dijkstra, preferring the cheapest paths.

The algorithm avoids 'W' and 'M' if '1' is available.

Execution time remains under ~0.05s for 41×41 mazes, even with terrain.

Printing the maze before and after gives visual clarity on pathfinding.

✅ Conclusion
This project demonstrates:

Robust use of Dijkstra’s algorithm for real-world-like terrain.

Clean maze generation and solving.

Clear output and performance tracking.

All implemented using only Python’s standard library (no NumPy or external tools).
