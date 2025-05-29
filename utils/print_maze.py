def print_maze(maze):
    """
    Prints the maze using emojis:
    '0' = wall (🟥), '1' = path (🟨), 'M' = mud (🟫), 'W' = water (🟦), '2' = path taken (🟩)
    """
    maze_copy = [row[:] for row in maze]  # deep copy to avoid modifying the original

    for i in range(len(maze_copy)):
        for j in range(len(maze_copy[0])):
            if maze_copy[i][j] == '0':
                maze_copy[i][j] = '🟥'  # wall
            elif maze_copy[i][j] == '1':
                maze_copy[i][j] = '🟨'  # normal path
            elif maze_copy[i][j] == 'M':
                maze_copy[i][j] = '🟫'  # mud
            elif maze_copy[i][j] == 'W':
                maze_copy[i][j] = '🟦'  # water
            elif maze_copy[i][j] == '2':
                maze_copy[i][j] = '🟩'  # solved path

    print('\n'.join(''.join(row) for row in maze_copy))
    print()