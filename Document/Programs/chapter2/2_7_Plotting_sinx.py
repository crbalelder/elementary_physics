import numpy as np
import matplotlib.pyplot as plt

def g(x,n):
    return np.sin(x)/x**n

def run():
    x = np.linspace(-5,5,500)
    fig, axes = plt.subplots(figsize=(5,5))
    axes.set_title('$\sin{x} / x^{n}$')
    axes.plot(x,g(x,1), label='$\sin{(x)}/x$')
    axes.plot(x,g(x,2), label='$\sin{(x)}/x^{2}$')
    axes.plot(x,g(x,3), label='$\sin{(x)}/x^{3}$')
    axes.legend()
    axes.set_xlim([-5,5])
    axes.set_ylim([-5,5])
    fig.savefig('Document/img/chapter2/2-7/2_7_plot_sinx.png')

if __name__=='__main__':
    run()