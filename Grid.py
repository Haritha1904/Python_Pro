import numpy as np
grid = np.zeros((5,5))
obstacles = [(1,1),(2,2),(3,1)]
for ox, oy in obstacles:
    grid[oy][ox] = -1
position = np.array([0,0])
goal = np.array([4,4])
def is_valid(pos):
    x,y = pos
    return 0 <= x < 5 and 0 <= y < 5 and grid[y][x] != -1
moves = [np.array([1,0]),np.array([0,1])]
path = [position.copy()]
while not np.array_equal(position,goal):
    for move in moves :
        next_pos = position + move
        if is_valid(next_pos):
            position = next_pos
            path.append(position.copy())
            break
print("Path taken: ")
for p in path:
    print(p)