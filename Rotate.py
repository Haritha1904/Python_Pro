import numpy as np

point = np.array([3,5])
theta = np.radians(90)

rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

new_point = rotation_matrix.dot(point)
print("Rotated point ",new_point)