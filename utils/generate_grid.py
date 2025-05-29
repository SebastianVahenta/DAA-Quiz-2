def generate_grid(n, m, maze):
    """
    This function creates a grid of size m x n, 
    where m and n are odd numbers, and fills it with 0s and 1s. 
    
    '0' = wall
    '1' = walkable cell
    
    :param n: number of columns
    :param m: number of rows
    :param maze: unused, just for legacy compatibility
    :return: A 2D array of size m x n 
    """
    maze = [['0' for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i % 2 != 0 and j % 2 != 0:
                maze[i][j] = '1'  # path
            else:
                maze[i][j] = '0'  # wall

    return maze