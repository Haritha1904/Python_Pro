import numpy as np
position = np.array([0,0])

def move_robot(position,direction, step =1):
    if direction == 'up':
        return position + np.array([0, step])
    elif direction == 'down':
        return position + np.array([0, -step])
    elif direction == 'left':
        return position + np.array([-step, 0])
    elif direction == 'right':
        return position + np.array([step, 0])
    else:
        return position
commands = ['right', 'up', 'up', 'left']

for i, cmd in enumerate(commands):
    position = move_robot(position, cmd)
    print(f"Step {i+1}: Position = {position}")