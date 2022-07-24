import numpy as np

def unit_vector(angle):
    return np.cos(angle), np.sin(angle)

def run():
    angles = [0,np.pi/6,np.pi/3,np.pi/2,3*np.pi/2]
    for angle in angles:
        print(f'The unit vectors for {angle} radiants are {unit_vector(angle)}')

if __name__ == '__main__':
    run()