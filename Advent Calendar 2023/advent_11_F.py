import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import f
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n F Distribution \n $X \\sim F(d_1, d_2)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 3., 1000)
params = [(1., 1), (2.5, 1), (10, 100), (100, 100)]
for (alpha, beta) in params:
    rv = f(dfn=alpha, dfd=beta)
    ax1.plot(x, rv.pdf(x), label=f"$d_1={alpha},  d_2={beta}$")
    ax2.plot(x, rv.cdf(x), label=f"$d_1={alpha},  d_2={beta}$")

ax1.set_ylim((0,2.1))
ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white',  framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('11_F')
plt.show()
