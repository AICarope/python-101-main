# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

import random

# Initialize the maze
def init_maze(width, height):
    maze = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append('u')  # 'u' represents unvisited blocks
        maze.append(line)
    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Generate the maze using Prim's algorithm
def generate_maze(width, height):
    maze = init_maze(width, height)
    
    starting_height = random.randint(1, height - 2)
    starting_width = random.randint(1, width - 2)
    
    maze[starting_height][starting_width] = 'c'  # 'c' represents cells
    
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])
    
    while walls:
        rand_wall = walls[random.randint(0, len(walls) - 1)]
        if rand_wall[1] != 0 and maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 'c':
            s_cells = surrounding_cells(rand_wall, maze)
            if s_cells < 2:
                maze[rand_wall[0]][rand_wall[1]] = 'c'
                if rand_wall[0] != 0 and maze[rand_wall[0] - 1][rand_wall[1]] != 'c':
                    maze[rand_wall[0] - 1][rand_wall[1]] = 'w'  # 'w' represents walls
                    if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                        walls.append([rand_wall[0] - 1, rand_wall[1]])
                # Add the other surrounding walls and cells here
        delete_wall(rand_wall, walls)

    print_maze(maze)

# Function to count surrounding cells
def surrounding_cells(rand_wall, maze):
    # Implement the logic to count surrounding cells
    pass

# Function to delete a processed wall from the walls list
def delete_wall(rand_wall, walls):
    for wall in walls:
        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
            walls.remove(wall)

# Generating a maze with dimensions 10x10
generate_maze(10, 10)