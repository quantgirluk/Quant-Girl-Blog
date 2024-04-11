import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import binom
import numpy as np

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

n = 20
p = 0.3
rv = binom(n=n, p=p)
x = np.arange(0, n + 1, 1)
title = f"\n Binomial Distribution \n $X \\sim Bin(n={n}, p={p})$"

fig = plt.figure(figsize=(10, 5), dpi=150)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

ax1.vlines(x, 0, rv.pmf(x), colors='grey', linestyles='--', lw=1)
ax1.plot(x, rv.pmf(x), marker='o', linestyle='', color='deepskyblue')

plt.plot(x, rv.cdf(x), drawstyle='steps-post',
         color='grey', lw=1, linestyle='--')
ax2.plot(x, rv.cdf(x), color='hotpink', marker='o', linestyle='')

ax1.set_title('Probability Mass Function', y=-0.18)
ax2.set_title('Cumulative Distribution Function', y=-0.18)

fig.suptitle(title)
gs.tight_layout(fig)

# fig.savefig('01_Binomial')
plt.show()
