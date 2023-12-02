import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import beta
import numpy as np

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": "New Century Schoolbook",
})

params = [(0.5, 0.5), (2.0, 0.5), (2.0, 2.0), (2.0, 5.0)]


x = np.linspace(0, 1, 100)
title = f"\n Beta Distribution \n $X \\sim Beta(\\alpha, \\beta)$"
fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])


for (a, b) in params:
    rv = beta(a, b)
    ax1.plot(x, rv.pdf(x), label=f"$\\alpha={a},  \\beta={b}$")
    ax2.plot(x, rv.cdf(x),  label=f"$\\alpha={a},  \\beta={b}$")

ax1.set_title('Probability Density Function', y=-0.18)
ax1.legend()
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('02_Beta')
plt.show()
