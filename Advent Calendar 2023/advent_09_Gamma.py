import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import gamma
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Gamma Distribution \n $X \\sim \\Gamma(\\alpha, \\beta)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 12., 1000)
params = [(1.0, 0.5), (2.0, 2.0), (3.0, 2.0), (5., 1.)]
for (alpha, beta) in params:
    rv = gamma(a=alpha, scale=1/beta)
    ax1.plot(x, rv.pdf(x), label=f"$\\alpha={alpha},  \\beta={beta}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\alpha={alpha},  \\beta={beta}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right')
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('09_Gamma')
plt.show()
