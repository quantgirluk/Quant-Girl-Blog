import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import t
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Student's t Distribution \n $X \\sim t(\\nu)$"

fig = plt.figure(figsize=(10, 5), dpi=200)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

x = np.linspace(-6., 6., 500)
params = [0.5, 1.0, 4.0, 20.0]
for nu in params:
    rv = t(df=nu)
    ax1.plot(x, rv.pdf(x), label=f"$\\nu={nu}$")
    ax2.plot(x, rv.cdf(x), label=f"$\\nu={nu}$")

ax1.set_title(r'Probability Density Function', y=-0.18)
ax2.legend(loc='lower right')
ax2.set_title('Cumulative Distribution Function', y=-0.18)
fig.suptitle(title)
gs.tight_layout(fig)

fig.savefig('07_Student_t')
plt.show()
