import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import lognorm
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Lognormal Distribution \n $X \\sim LogNormal(\\mu, \\sigma^2)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 3., 1000)
params = [(0.0, 0.25), (0.0, 0.5), (0.0, 1.0), (0.5, 0.5)]
for (alpha, beta) in params:
    rv = lognorm(loc=alpha, s=beta)
    ax1.plot(x, rv.pdf(x), label=f"$\\mu={alpha},  \\sigma={beta}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\mu={alpha},  \\sigma={beta}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('14_Lognormal')
plt.show()
