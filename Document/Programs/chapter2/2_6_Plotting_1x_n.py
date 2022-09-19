import numpy as np
import matplotlib.pyplot as plt

def f(x,n):
    return 1/x**(n)

def run():
    x = np.linspace(-2,2,1000)
    fig, axes = plt.subplots(figsize=(5,5))
    axes.set_title('$1/x^{n}$')
    axes.plot(x,f(x,1),'r', label='$1/x$')
    axes.plot(x,f(x,2),'b', label='$1/x^2$')
    axes.plot(x,f(x,3),'g', label='$1/x^3$')
    axes.set_ylim([-10,10])
    axes.set_xlim([-2,2])
    axes.legend()
    fig.savefig('Document/img/chapter2/2-6/2_6_plot_xs.png')

if __name__=='__main__':
    run()
