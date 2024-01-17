import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from aleatory.stats import ncx
import numpy as np
from matplotlib.cm import get_cmap

name = "tab20"
cmap = get_cmap(name)  #
colors = cmap.colors  #

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Non-central Chi Distribution \n $X \\sim \chi_k (\\lambda)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])
ax1.set_prop_cycle(color=colors)
ax2.set_prop_cycle(color=colors)

x = np.linspace(0., 9., 100)

for nc in [0.0, 3.0, 6.0]:
    for k in [1.0, 2.0]:
        rv = ncx(df=k, nc=nc)
        ax1.plot(x, rv.pdf(x), label=f"$\\lambda ={nc}, k = {k}$")
        ax2.plot(x, rv.cdf(x), label=f"$\\lambda ={nc}, k = {k}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc="lower right", frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('non_central_chi_colors')
plt.show()
