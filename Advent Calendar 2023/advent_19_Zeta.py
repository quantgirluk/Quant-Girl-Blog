import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from scipy.stats import zipf

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")


title = f"Zeta Distribution \n $X \sim \\zeta(s)$"

fig = plt.figure(figsize=(10, 5), dpi=150)
gs = GridSpec(1, 4, wspace=0.5)
ax1 = fig.add_subplot(gs[:2])
ax2 = fig.add_subplot(gs[2:])

params = [2, 3, 4, 5]
x = np.arange(1, 10, 1)
for s in params:
    rv = zipf(s)
    ax1.vlines(x, 0, rv.pmf(x), colors='grey', linestyles='--', lw=1, alpha=0.5)
    # ax1.plot(x, rv.pmf(x), marker='o', linestyle='', label=f"$s={s}$")



for s in params:
    rv = zipf(s)
    x = np.arange(1, 10, 1)
    ax1.plot(x, rv.pmf(x), marker='o', linestyle='', label=f"$s={s}$")
    x = np.arange(0, 10, 1)
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

fig.savefig('19_Zeta')
plt.show()
