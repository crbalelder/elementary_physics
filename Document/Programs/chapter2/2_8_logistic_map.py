import numpy as np
import matplotlib.pyplot as plt

def logistic(x,r):
    return (r*x)*(1-x)

def steps(n,r):
    x = np.zeros(n)
    x[0]=0.5 # Star point x(1)=0.5
    
    for k in range(n-1):
        x[k+1] = logistic(x[k],r)
    
    return x

def run():
    n=100; i = np.arange(n)
    x_1 = steps(n,1); x_2 = steps(n,2)
    x_3 = steps(n,3); x_4 = steps(n,4)

    fig, axes = plt.subplots(figsize=(10,8))
    axes.set_title('Logistic map')
    axes.set_xlabel('steps $(i)$')
    axes.set_ylabel('$x(i)$')
    axes.plot(i,x_1, label='r=1')
    axes.plot(i,x_2, label='r=2')
    axes.plot(i,x_3, label='r=3')
    axes.plot(i,x_4, label='r=4')
    axes.legend()
    fig.savefig('Document/img/chapter2/2-8/2_8_logistic_map.png')

if __name__=='__main__':
    run()