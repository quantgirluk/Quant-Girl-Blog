import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from twopiece.scale import tpnorm
from scipy.stats import norm
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Two-Piece Normal Distribution \n $X \\sim TPNorm(\\mu, \\sigma_1, \\sigma_2)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

params = [(0.0, 1.0, 1.0), (0.0, 0.5, 2.), (0.0, 1.0, 2.0), (-1.0, 2., 1.)]
for (a, b, c) in params:
    rv = tpnorm(loc=a, sigma1=b, sigma2=c, kind=None)
    x = np.linspace(-7., 7., 1000)
    ax1.plot(x, rv.pdf(x), label=f"$\\mu={a},  b={b}$")
    x = np.linspace(-7., 7., 1000)
    ax2.plot(x, rv.cdf(x), label=f"$\\mu={a},  \\sigma_1={b}, \\sigma_2={c}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc="lower right", frameon=True, facecolor='white', framealpha=1, prop={'size': 8})
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('23_TwoPieceNormal')
plt.show()

fig = plt.figure(figsize=(10, 7))
sigma1 = 1.
sigma2 = 1.5
x = np.linspace(-4., 0., 200)
rv = norm(loc=0.0, scale=sigma1)
plt.plot(x, rv.pdf(x), label="Left Half", linestyle="dotted", color="blue", lw=1.5)

x = np.linspace(-4., 4., 1000)
rv = tpnorm(loc=0.0, sigma1=sigma1, sigma2=sigma2, kind=None)
plt.plot(x, rv.pdf(x), label="Two-Piece Normal", color="purple")
plt.fill_between(x, rv.pdf(x), color="purple", alpha=0.2)

rv = norm(loc=0.0, scale=sigma2)
x = np.linspace(0., 4., 200)
plt.plot(x, rv.pdf(x), label="Right Half", linestyle="dotted", color="hotpink", lw=1.5)
plt.legend(frameon=True, facecolor='white', framealpha=1)
plt.title("Two-Piece Normal Density \n $TPNorm(\mu = 0.0, \sigma_1=1.0, \sigma_2=1.5)$")
fig.savefig('23_TwoPieceNormal_Bonus')
plt.show()
