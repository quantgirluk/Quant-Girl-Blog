import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import chi2
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Chi Squared Distribution \n $X \\sim \chi^2 (k)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 11., 1000)
params = [1, 2, 3, 5, 10]
for k in params:
    rv = chi2(k)
    ax1.plot(x, rv.pdf(x), label=f"$k ={k}$")
    ax2.plot(x, rv.cdf(x), label=f"$k={k}$")

ax1.set_ylim((0, 0.55))
ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend( frameon=True, facecolor='white',  framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('12_ChiSquared')
plt.show()
