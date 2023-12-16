import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import vonmises
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Von Mises Distribution \n $X \\sim VonMises(\\mu, \\kappa)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-1.0 * np.pi, np.pi, 1000)
params = [(0.0, 0.5), (0.0, 1.0), (0.0, 2.0), (1.0, 1.)]
for (a, b) in params:
    rv = vonmises(loc=a, kappa=b)
    ax1.plot(x, rv.pdf(x), label=f"$\\mu={a},  \\kappa={b}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\mu={a},  \\kappa={b}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('16_VonMises')
plt.show()
