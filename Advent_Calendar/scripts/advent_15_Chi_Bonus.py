from aleatory.processes import BESProcess
bes = BESProcess(dim=3, initial=0)
mystyle = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"

fig = bes.draw(n=100, N=200, style=mystyle, colormap="PRGn",
         orientation='horizontal', figsize=(12, 6))

fig.savefig("15_Chi_Bonus")