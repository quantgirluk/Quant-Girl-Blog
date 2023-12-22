import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from skrmt.ensemble.spectral_law import MarchenkoPasturDistribution

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Marchenko Pastur Distribution \n $X \\sim Marchenko-Pastur(\\lambda)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x_cdf = np.linspace(0, 3.5, 1000)
params = [0.1, 0.2, 0.5, 0.7]
sigma = 1.0
for ratio in params:
    rv = MarchenkoPasturDistribution(beta=1, ratio=ratio, sigma=sigma)

    lambda_min = (sigma ** 2) * (1. - np.sqrt(ratio)) ** 2
    lambda_max = (sigma ** 2) * (1. + np.sqrt(ratio)) ** 2
    x = np.linspace(lambda_min, lambda_max, 1000)
    ax1.plot(x, rv.pdf(x), label=f"$\\lambda={ratio}$")
    ax2.plot(x_cdf, rv.cdf(x_cdf), label=f"$\\lambda={ratio}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right', frameon=True, facecolor='white', framealpha=1)
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('22_MarchenkoPastur')
plt.show()
