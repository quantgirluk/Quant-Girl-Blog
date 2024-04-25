import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

def plot_bessel_functions(alphas, xrange, modified=False, my_title=None, return_fig=False, **fig_kw):
    x = np.linspace(xrange[0], xrange[1], 500)
    fig, ax = plt.subplots(1, 1, **fig_kw)
    for v in alphas:
        if modified:
            ax.plot(x, sp.iv(v, x), lw=1.5)
            my_legends = ['$I_{' + str(n) + '}(x)$' for n in alphas]
        else:
            ax.plot(x, sp.jv(v, x), lw=1.5)
            my_legends = ['$J_{' + str(n) + '}(x)$' for n in alphas]
    ax.legend(my_legends)
    if my_title:
        plot_title = my_title
    elif modified:
        plot_title = 'Modified Bessel Functions of 1st Order'
    else:
        plot_title = 'Bessel Functions of 1st Order'
    plt.title(plot_title)

    if return_fig:
        plt.show()
        return fig
    else:
        plt.show()



fig = plot_bessel_functions(alphas=[-5, -3,  0,  3, 5], xrange=[-10, 10], return_fig=True)
fig.savefig('../figures/bessel_functions.png')

fig = plot_bessel_functions(alphas=[-5, -3,  0,  3, 5], xrange=[-10, 10], modified=True, return_fig=True)
fig.savefig('../figures/bessel_functions_modified.png')