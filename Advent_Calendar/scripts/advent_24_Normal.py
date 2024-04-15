import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.stats import norm
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Normal Distribution \n $X \\sim N(\\mu, \\sigma)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])
x = np.linspace(-7., 7., 1000)
params = [(0.0, 1.0), (0.0, 0.75), (0.0, 2.), (-1.0, 2.)]

for (a, b) in params:
    rv = norm(loc=a, scale=b)
    ax1.plot(x, rv.pdf(x), label=f"$\\mu={a},  \\sigma={b}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\mu={a},  \\sigma={b}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc="lower right", frameon=True, facecolor='white', framealpha=1, prop={'size': 8})
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('24_Normal')
plt.show()
