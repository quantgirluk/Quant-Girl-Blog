import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from scipy.stats import beta
import numpy as np

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")


def plot_zoibeta(parameters, title=None, **kwargs):
    title = title if title else f"\n Zero-One Inflated Beta Distribution \n $X \\sim ZOIBeta(\\alpha, \\gamma, \\mu, " \
                                f"\\sigma)$ "

    fig = plt.figure(figsize=(10, 5), *kwargs)
    gs = GridSpec(1, 4, wspace=0.5)
    ax1 = fig.add_subplot(gs[:2])
    ax2 = fig.add_subplot(gs[2:])
    x = np.linspace(0, 0.999, 500)

    for (alpha, gamma, mu, phi) in parameters:
        pi0 = alpha * (1.0 - gamma)
        pi1 = alpha * gamma
        a = mu * phi
        b = (1 - mu) * phi
        rv = beta(a, b)

        ax1.plot(x, (1 - pi0 - pi1) * rv.pdf(x), label=f"$\\alpha={alpha},  \\gamma={gamma}, \\mu={mu}, \\phi={phi}$")
        ax1.scatter([0, 1], [pi0, pi1])
        ax2.plot(x, pi0 + (1 - pi0 - pi1) * rv.cdf(x),
                 label=f"$\\alpha={alpha},  \\gamma={gamma}, \\mu={mu}, \\phi={phi}$")
        ax2.scatter([0, 1], [pi0, 1.0])
        ax1.legend()

    ax1.set_title('Mixed Continuous-Discrete\n Probability Density Function', y=-0.25)
    ax2.set_title('Mixed Continuous-Discrete\n Cumulative Distribution Function', y=-0.25)

    fig.suptitle(title)
    gs.tight_layout(fig)

    plt.show()

    return fig


def main():
    zoi_beta_params = [(0.9, 0.1, 0.3, 5), (0.9, 0.5, 0.5, 0.5), (0.4, 0.2, 0.7, 5), (0.2, 0.8, 0.7, 5)]
    figure = plot_zoibeta(zoi_beta_params, dpi=200)
    figure.savefig('21_ZOIBeta')


if __name__ == "__main__":
    main()
