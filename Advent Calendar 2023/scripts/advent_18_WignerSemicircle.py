import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import semicircular
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Wigner Semicircle Distribution \n $X \\sim Wigner(R)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-2.0, 2.0, 1000)
params = [0.5, 1.0, 1.5, 2.0]
for R in params:
    rv = semicircular(scale=R)
    ax1.plot(x, rv.pdf(x), label=f"$R={R}$")
    ax2.plot(x, rv.cdf(x), label=f"$R={R}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('18_WignerSemicircle')
plt.show()
