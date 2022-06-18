import numpy as np

def seconds(h):
    return 3600*h

if __name__ == '__main__':
    hours = np.array([1.5,12,24])
    for h in hours:
        print(f'{h} hours is equivalent {seconds(h)} seconds')