import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import cauchy
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Cauchy Distribution \n $X \\sim Cauchy(x_0, \\gamma)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-6., 6., 500)
params = [(0.0, 0.5), (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0)]
for (a, b) in params:
    rv = cauchy(loc=a, scale=b)
    ax1.plot(x, rv.pdf(x), label=f"$x_0={a},  \\gamma={b}$")
    ax2.plot(x, rv.cdf(x), label=f"$x_0={a},  \\gamma={b}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax1.legend()
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('03_Cauchy')
plt.show()
