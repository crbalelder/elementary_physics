import numpy as np
import matplotlib.pyplot as plt

def acceleration(v,x,k,C):
    return -k*x - C*v

def acceleration_2(v,x,k,C): # Part 3
    return k*np.sin(x) - C*v

def plot(function,name):
    k=10; C=5; delta=0.01; n=100
    x = np.zeros(n); v = np.zeros(n)
    a = np.zeros(n); t = np.zeros(n)
    x[0]=0; v[0]=1

    for i in range(n-1):
        a[i] = function(v[i],x[i],k,C)
        x[i+1] = x[i] + v[i]*delta
        v[i+1] = v[i] + a[i]*delta
        t[i+1] = t[i] + delta
    
    fig, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(10,8))
    ax1.plot(t,x, 'r')
    ax1.set_ylabel('$x(t)$')
    ax2.plot(t,v, 'b')
    ax2.set_ylabel('$v(t)$')
    ax3.plot(t,a, 'g')
    ax3.set_ylabel('$a(t)$')
    ax3.set_xlabel('$x(t)$')
    plt.tight_layout()
    fig.savefig('Document/img/chapter2/2-9/' + name)

if __name__=='__main__':
    plot(acceleration,'2_9_accele_a.png')
    plot(acceleration_2,'2_9_accele_b.png')