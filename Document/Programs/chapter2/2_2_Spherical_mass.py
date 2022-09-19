import numpy as np

def mass(rho,r):
    return (4*np.pi/3)*(rho)*(r**3)

def run():
    rho = 8000
    print(f'The sphere of steel with density {rho} kg/m3')
    radius = np.array([1e-003,1,10])
    for r in radius:
        print(f'The sphere with {r} m of radius has {mass(rho,r)} kg')

if __name__=='__main__':
    run()