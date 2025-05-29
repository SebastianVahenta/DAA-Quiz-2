import heapq

def dijkstra_maze_solver(maze, start, end):
    """
    Solves the maze using Dijkstra's algorithm with weighted terrain.
    '1' = cost 1, 'M' = cost 5, 'W' = cost 10, '0' = wall (impassable)
    """

    def get_neighbours_with_weights(maze, i, j, visited):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        cost_map = {'1': 1, 'M': 5, 'W': 10}
        neighbours = []

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
                mid_i, mid_j = (i + ni) // 2, (j + nj) // 2
                terrain = maze[mid_i][mid_j]
                if terrain in cost_map and (ni, nj) not in visited:
                    neighbours.append(((ni, nj), cost_map[terrain]))
        return neighbours

    visited = set()
    distance = {tuple(start): 0}
    prev_nodes = {}

    heap = [(0, tuple(start))]

    while heap:
        current_cost, current = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current == tuple(end):
            break

        for (ni, nj), edge_cost in get_neighbours_with_weights(maze, current[0], current[1], visited):
            new_cost = current_cost + edge_cost
            if (ni, nj) not in distance or new_cost < distance[(ni, nj)]:
                distance[(ni, nj)] = new_cost
                prev_nodes[(ni, nj)] = current
                heapq.heappush(heap, (new_cost, (ni, nj)))

    # Reconstruct path
    path = []
    current = tuple(end)
    while current != tuple(start):
        path.append(current)
        current = prev_nodes.get(current)
        if current is None:
            print("❌ No path found.")
            return
    path.append(tuple(start))
    path.reverse()

    for i in range(len(path)):
        maze[path[i][0]][path[i][1]] = '2'
        if i < len(path) - 1:
            mid_i = (path[i][0] + path[i + 1][0]) // 2
            mid_j = (path[i][1] + path[i + 1][1]) // 2
            maze[mid_i][mid_j] = '2'
