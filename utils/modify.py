import random

def modify(maze, m, n):
    for _ in range(100):
        x = random.randint(1, n - 2)
        y = random.randint(1, m - 2)
        if maze[x][y] == '1':
            maze[x][y] = random.choices(['1', 'M', 'W'], weights=[0.6, 0.3, 0.1])[0]