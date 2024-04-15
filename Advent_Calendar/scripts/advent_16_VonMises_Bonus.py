import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import vonmises

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

title: str = f"\n Von Mises Distribution \n $X \\sim VonMises(\\mu = \\frac{1}{2} \pi, \\kappa = 1)$"

loc = 0.5 * np.pi  # circular mean
kappa = 1  # concentration
number_of_samples = 5000
samples = vonmises(loc=loc, kappa=kappa).rvs(number_of_samples)

fig = plt.figure(figsize=(12, 6))
left = plt.subplot(121)
right = plt.subplot(122, projection='polar')

x = np.linspace(-np.pi, np.pi, 500)
vonmises_pdf = vonmises.pdf(loc, kappa, x)

left.plot(x, vonmises_pdf, label="Probability Density Function")
ticks = [0, 0.15, 0.3]
left.set_yticks(ticks)
number_of_bins = int(np.sqrt(number_of_samples))
left.hist(samples, density=True, bins=number_of_bins, label="Sample Histogram", color="deeppink", alpha=0.25)
left.set_xlim(-np.pi, np.pi)
left.set_title(r'Cartesian Plot', y=-0.18)
left.legend(loc="upper left", frameon=True, facecolor='white', framealpha=1)

right.plot(x, vonmises_pdf)
right.set_yticks(ticks)
right.hist(samples, density=True, bins=number_of_bins, color="deeppink", alpha=0.25)
right.set_title('Polar Plot', y=-0.18)

fig.suptitle(title)
plt.tight_layout()

fig.savefig('16_VonMises_Bonus')
plt.show()
