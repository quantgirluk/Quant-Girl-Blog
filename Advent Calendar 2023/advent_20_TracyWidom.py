import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from skrmt.ensemble.spectral_law import TracyWidomDistribution

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Tracy-Widom Distribution \n $X \\sim TW\\beta$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-5.0, 5.0, 1000)
params = [1, 2, 4]
for beta in params:
    rv = TracyWidomDistribution(beta=beta)
    ax1.plot(x, rv.pdf(x), label=f"$\\beta={beta}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\beta={beta}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('20_TracyWidom')
plt.show()
