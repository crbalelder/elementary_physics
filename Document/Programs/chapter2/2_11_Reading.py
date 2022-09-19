
import numpy as np
import matplotlib.pyplot as plt

def select_data(data):
    t = data[:,0]; x = data[:,1]
    y = data[:,2]
    return t, x, y

def w_vs_t(t,x,y):
    fig, (ax1,ax2) = plt.subplots(2,1,figsize=(6,6))
    ax1.set_title('$t$ vs $x(t)$, $y(t)$')
    ax1.plot(t,x,'r')
    ax1.set_ylabel('$x(t)$')
    ax1.set_xlabel('$t$')
    ax2.plot(t,y,'b')
    ax2.set_ylabel('$y(t)$')
    ax2.set_xlabel('$t(s)$')
    fig.savefig('Document/img/chapter2/2-11/2_11_b.png')

def x_y_position(x,y):
    fig, axes = plt.subplots(1,1)
    axes.plot(x,y,'g')
    axes.set_title('$(x,y)$')
    axes.set_xlabel('$x$')
    axes.set_ylabel('$y$')
    fig.savefig('Document/img/chapter2/2-11/2_11_c.png')

if __name__=='__main__':
    data = np.loadtxt('Document/datasets/chapter2/trajectory.dat')
    t, x, y = select_data(data)
    w_vs_t(t,x,y)
    x_y_position(x,y)