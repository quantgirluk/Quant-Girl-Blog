import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from scipy.stats import hypergeom

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

x = np.arange(0, 60, 1)
title = f"Hypergeometric Distribution \n $X \\sim Hypergeometric(N, K, n)$"

fig = plt.figure(figsize=(10, 5), dpi=150)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

params = [(50, 100), (60, 200), (70, 300)]

for (n, N) in params:
    rv = hypergeom(700, n, N)
    ax1.vlines(x, 0, rv.pmf(x), colors='grey', linestyles='--', lw=1, alpha=0.5)

for (n, N) in params:
    rv = hypergeom(700, n, N)
    ax1.plot(x, rv.pmf(x), marker='o', linestyle='', label=f"$N=700, K={n}, n={N}$")
    c = ax1.get_lines()[-1].get_color()
    ax2.plot(x, rv.cdf(x), drawstyle='steps-post',
             color=c,
             lw=1, linestyle='--')
    ax2.plot(x, rv.cdf(x), marker='o', linestyle='')

ax1.legend()
ax1.set_title('Probability Mass Function', y=-0.18)
ax2.set_title('Cumulative Distribution Function', y=-0.18)

fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('08_Hypergeometric')
plt.show()
