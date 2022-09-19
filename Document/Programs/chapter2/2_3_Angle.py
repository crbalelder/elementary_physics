import numpy as np

def point(angle):
    return np.arctan(angle[1]/angle[0])

def run():
    angles = np.array([[1,1],[-1,1],[-1,-1],[1,-1]])
    for angle in angles:
        print(f'The point {angle} has angle {point(angle)}')
    
if __name__=='__main__':
    run()