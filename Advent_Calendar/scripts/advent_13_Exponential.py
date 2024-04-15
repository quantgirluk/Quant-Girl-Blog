import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import expon
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Exponential Distribution \n $X \\sim Exp (\\lambda)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 5., 1000)
params = [0.5, 1., 1.5, 2., 10.]
for k in params:
    rv = expon(scale = 1/k)
    ax1.plot(x, rv.pdf(x), label=f"$\\lambda ={k}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\lambda ={k}$")

ax1.set_ylim((0, 0.55))
ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend( frameon=True, facecolor='white',  framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('13_Exponential')
plt.show()
