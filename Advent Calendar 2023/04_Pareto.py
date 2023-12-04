import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import pareto
import numpy as np

# noinspection DuplicatedCode
plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Pareto Distribution \n $X \\sim Pareto(x_m, \\alpha)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

params = [(0.5, 0.4), (1.0, 0.5), (2.0, 2.0), (2.0, 3.0)]
for (xm, b) in params:
    x1 = np.linspace(0.0, xm - 0.0001, 100)
    x2 = np.linspace(xm, 6., 500)
    rv = pareto(b=b, scale=xm, )
    x = x2
    ax1.plot(x, rv.pdf(x), label=f"$x_m={xm},  \\alpha={b}$")
    ax2.plot(x, rv.cdf(x), label=f"$x_m={xm},  \\alpha={b}$")
    c = ax1.get_lines()[-1].get_color()
    x = x1
    ax1.plot(xm, rv.pdf(xm), color=c, marker='o', markersize=3.5)
    ax1.plot(x, rv.pdf(x), color=c)
    ax2.plot(x, rv.cdf(x), color=c)

ax1.set_title('Probability Density Function', y=-0.18)
ax1.legend()
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('04_Pareto')
plt.show()
