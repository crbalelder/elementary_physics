import numpy as np

def dice(n):
    x_1 = np.random.randint(1,6,n)
    x_2 = np.random.randint(1,6,n)
    return x_1 + x_2

def average(z,n):
    return (1/n)*sum(z)

def standard_deviation(z,Z):
    i=0; DZ=0
    while i!=n:
        DZ+=(z[i]-Z)**2
        i+=1

    return (1/(n-1))*DZ

if __name__=='__main__':
    n=100
    z = dice(n)
    Z = average(z,n)
    x = standard_deviation(z,Z)
    print(f'The average for {n} times is {Z} and the standard deviation is {x}')

