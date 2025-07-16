import numpy as np

robot_pos = np.array([2, 2])
obstacles = [np.array([2, 4]), np.array([4, 2])]

def lidar_scan(angle_deg):
    angle_rad = np.radians(angle_deg)
    direction = np.array([np.cos(angle_rad), np.sin(angle_rad)])
    
    for d in range(1, 5):
        probe = np.round(robot_pos + d * direction).astype(int)
        if any(np.array_equal(probe, obs) for obs in obstacles):
            return d
    return None  # Now correctly outside the loop

for angle in [0, 90, 180, 270]:
    print(f"Angle {angle}° → Distance: {lidar_scan(angle)}")
