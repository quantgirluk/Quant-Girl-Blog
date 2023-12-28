import matplotlib.pyplot as plt
from aleatory.processes import BrownianMotion

plt.style.use("https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")

process = BrownianMotion(T=10)
fig = process.draw(n=200, N=200, envelope=True, colormap="Greens",
                   title="Merry Christmas!", figsize=(10, 7))

fig.savefig('24_Normal_Bonus')
plt.show()
