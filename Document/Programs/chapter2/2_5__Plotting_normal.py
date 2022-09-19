import numpy as np
import matplotlib.pyplot as plt


def normal(x,mu,sigma):
    return (1/np.square(2*np.pi*(sigma**2)))*np.exp(-((x-mu)**2)/(2*(sigma**2)))

def run_b(x):
    fig, axes =plt.subplots()
    axes.plot(x,normal(x,0,1), label='$\mu=0,\sigma=1$')
    axes.legend()
    fig.savefig('Document/img/chapter2/2-5/2_5_plot_a.png')

def run_c(x):
    fig, axes = plt.subplots(1,1)
    axes.plot(x, normal(x,0,2), 'r', label='$\mu=0,\sigma=2$')
    axes.plot(x, normal(x,0,0.5), 'b', label='$\mu=0,\sigma=0.5$')
    axes.legend()
    fig.savefig('Document/img/chapter2/2-5/2_5_plot_b.png')

def run_d(x):
    fig, (ax1,ax2,ax3) = plt.subplots(3,1)
    ax1.plot(x, normal(x,0,1), 'r', label='$\mu=0,\sigma=1$')
    ax1.legend(loc='upper left')
    ax2.plot(x, normal(x,1,1), 'g', label='$\mu=1,\sigma=1$')
    ax2.legend(loc='upper left')
    ax3.plot(x, normal(x,2,1), 'b', label='$\mu=2,\sigma=1$')
    ax3.legend()
    plt.tight_layout()
    fig.savefig('Document/img/chapter2/2-5/2_5_plot_c.png')

if __name__=='__main__':
    x = np.linspace(-5,5,100)
    run_b(x)
    run_c(x)
    run_d(x)