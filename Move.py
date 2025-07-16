import numpy as np
path =[np.array([0,0])]
path.append(path[-1] + np.array([2,0]))
path.append(path[-1] + np.array([0,3]))
path.append(path[-1] + np.array([-1,0]))
for i , point in enumerate(path):
    print(f"Step {i} : {point}")