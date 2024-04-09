import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
plt.style.use(quant_pastel)

palette = px.colors.qualitative.Bold
colors = [(a / 255, b / 255, c / 255) for (a, b, c) in [eval(p[4:-1]) for p in palette]]
colors_transparent1 = [(a / 255, b / 255, c / 255, 0.7) for (a, b, c) in [eval(p[4:-1]) for p in palette]]
colors_transparent2 = [(a / 255, b / 255, c / 255, 0.15) for (a, b, c) in [eval(p[4:-1]) for p in palette]]

data = yf.download('^SPX', interval='1wk')

kind = 'standard'
df = data
if kind == 'standard':
    column = 'Returns'
    df.loc[:, column] = 100 * (df['Adj Close'] - df['Adj Close'].shift(1)) / df['Adj Close']
elif kind == 'log':
    column = 'Log-Returns'
    df.loc[:, column] = np.log(df['Adj Close']) - np.log(df['Adj Close'].shift(1))

df = df.reset_index()
df['year'] = df['Date'].dt.year
df['Decade'] = [int(np.floor(year / 10) * 10) for year in np.array(df["year"])]
df = df.dropna()


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6), dpi=100)
box = df.boxplot(by='Decade', column='Returns', ax=ax, return_type='dict', patch_artist=True, notch=True)

for patch, flier, median, color in zip(box['Returns']['boxes'],
                                       box['Returns']['fliers'],
                                       box['Returns']['medians'],
                                       colors_transparent1):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

box = df.boxplot(by='Decade', column='Returns', ax=ax,
                 return_type='dict', patch_artist=True, notch=True,
                 boxprops={'fill': None}
                 )

for patch, flier, median, color, colort2 in zip(box['Returns']['boxes'],
                                                box['Returns']['fliers'],
                                                box['Returns']['medians'],
                                                colors, colors_transparent2):
    patch.set_edgecolor(color)
    patch.set_linewidth(1.5)
    median.set_color(color)
    median.set_linewidth(1.5)
    flier.set_markerfacecolor(colort2)
    flier.set_markeredgecolor(color)

w = box['Returns']['whiskers']
for (a, b), c in zip(zip(w[0::2], w[1::2]), colors):
    a.set_color(c)
    b.set_color(c)
    a.set_linewidth(1.25)
    b.set_linewidth(1.25)

caps = box['Returns']['caps']
for (a, b), c in zip(zip(caps[0::2], caps[1::2]), colors):
    a.set_color(c)
    b.set_color(c)
    a.set_linewidth(1.5)
    b.set_linewidth(1.5)

ax.grid(visible=False, axis='x')

ax.set_title('S\&P500 Historical Weekly Returns')
ax.set_xlabel('Decade')
ax.set_ylabel('Returns (\%)')
plt.suptitle('')
fig.savefig("./charts/01_january_sp500", dpi=300)
plt.show()
