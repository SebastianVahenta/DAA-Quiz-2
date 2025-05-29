
### What does this project do?

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

