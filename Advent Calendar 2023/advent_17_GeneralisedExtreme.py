import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import genextreme
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Generalised Extreme Value Distribution \n $X \\sim GEV(\\xi, \\mu=0, \\sigma=1)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-4.0, 4.0, 1000)
params = [(0.0, 1.0, 0.75), (0.0, 1.0, 0.5), (0.0, 1.0, 0.0), (0.0, 1.0, -0.5), (0.0, 1.0, -0.75)]
for (a, b, c) in params:
    rv = genextreme(c=c, loc=a, scale=b)
    ax1.plot(x, rv.pdf(x), label=f"$\\xi={c}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\xi={c}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('17_GeneralisedExtremeValue')
plt.show()
