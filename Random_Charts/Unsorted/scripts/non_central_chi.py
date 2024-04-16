import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from aleatory.stats import ncx
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Non-central Chi Distribution \n $X \\sim \chi (k, \\lambda=2)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 7., 100)
params = [1, 2, 5, 10]
for k in params:
    # rv = chi(k)
    rv = ncx(df=k, nc=2.0)
    ax1.plot(x, rv.pdf(x), label=f"$k ={k}$")
    ax2.plot(x, rv.cdf(x), label=f"$k={k}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc="lower right", frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('../figures/non_central_chi_01')
plt.show()

title: str = f"\n Non-central Chi Distribution \n $X \\sim \chi (k=2, \\lambda)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(0., 8., 100)
params = [1, 2, 3, 5]
for nc in params:
    rv = ncx(df=2.0, nc=nc)
    ax1.plot(x, rv.pdf(x), label=f"$\\lambda ={nc}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\lambda={nc}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc="lower right", frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('../figures/non_central_chi_02')
plt.show()
