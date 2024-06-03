import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yfinance as yf

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
plt.style.use(quant_pastel)

plt.rc('font', family='sans-serif')
plt.rc('font', serif='Apple SD Gothic Neo')
# plt.rcParams.update({'font.size': 14})

#  Index Chart


# Create the figure and axes object
fig, ax = plt.subplots(figsize=(12., 7.5), dpi=100)

data_index = yf.download('^IXIC')
data_index['Close'].plot.area(alpha=0.25, ax=ax)

ax.set_xlabel('')
ax.set_ylabel(r'Points')

# Add in red line and rectangle on top
ax.plot([0.05, .95], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.6)
ax.add_patch(plt.Rectangle((0.05, .98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure,
                           clip_on=False, linewidth=0))

# Add in title and subtitle
ax.text(x=0.05, y=.93, s="Nasdaq Composite Index", transform=fig.transFigure, ha='left', fontsize=14, weight='bold',
        alpha=.9)
ax.text(x=0.05, y=.90, s="Historical Close Levels from 1971 to 2024", transform=fig.transFigure, ha='left', fontsize=12,
        alpha=.9)

# Set source text
ax.text(x=0.05, y=0.075, s="Source: Yahoo Finance", transform=fig.transFigure, ha='left', fontsize=10, alpha=.8)

# Adjust the margins around the plot area
plt.subplots_adjust(left=None, bottom=0.2, right=None, top=0.85, wspace=None, hspace=None)

# format the ticks only for years on the major ticks
years = mdates.YearLocator(5)  # every 5 year
years_fmt = mdates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=12, labelrotation=0)

ax.set_ylim(0, 18000)
ax.xaxis.grid()  # horizontal lines
ax.set_axisbelow(True)

ax.spines[['right', 'top']].set_visible(False)
ax.spines[['bottom']].set_visible(True)

props = dict(boxstyle='round, pad=1', facecolor='oldlace', edgecolor='cornsilk', alpha=0.95)

my_text = '\n'.join((r'The Nasdaq Composite is a stock market index that includes almost ',
                     r'all stocks listed on the Nasdaq stock exchange. Its composition',
                     r'is heavily weighted towards companies in the information',
                     r'technology sector. Along with the Dow Jones Industrial Average',
                     r'and S\&P 500, it is one of the 3 most-followed stock market',
                     r'indices in the United States. ',
                     r'On May 28, 2024 the index closed above the 17,000 points for the ',
                     r'first time in history. '
                     ))

ax.text(0.025, 0.9, my_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.tight_layout()
ax.figure.savefig("../charts/05_may_nasdaq", dpi=200)
plt.show()

# 5 Largest Components Nasdaq

tickers = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'META']
data = yf.download(tickers, start='2014-01-01', )
highs = [('Close', 'MSFT'),
         ('Close', 'AAPL'),
         ('Close', 'NVDA'),
         ('Close', 'AMZN'),
         ('Close', 'META'),
         ]

fig, ax = plt.subplots(figsize=(12., 7.5), dpi=100)
data[highs].plot(figsize=(12, 8), ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel(r'Price (\$)')

ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.xaxis.grid()
ax.set_axisbelow(True)

ax.spines[['top']].set_visible(False)
ax.spines[['right', 'bottom']].set_visible(True)

years = mdates.YearLocator(2)  # every 2 year
years_fmt = mdates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=12, labelrotation=0)

# Add in red line and rectangle on top
ax.plot([0.05, .95], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.6)
ax.add_patch(plt.Rectangle((0.05, .98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure,
                           clip_on=False, linewidth=0))

# Add in title and subtitle
ax.text(x=0.05, y=.93, s="Nasdaq Composite 5 Largest Components", transform=fig.transFigure, ha='left', fontsize=14,
        weight='bold', alpha=.9)
ax.text(x=0.05, y=.90, s="Historical Close Prices from 2014 to 2024", transform=fig.transFigure, ha='left', fontsize=12,
        alpha=.9)

# Set source text
ax.text(x=0.05, y=0.075, s="Source: Yahoo Finance", transform=fig.transFigure, ha='left', fontsize=10, alpha=.8)

# Adjust the margins around the plot area
plt.subplots_adjust(left=None, bottom=0.2, right=None, top=0.85, wspace=None, hspace=None)

plt.tight_layout()
ax.figure.savefig("../charts/05_may_nasdaq_largest_components", dpi=200)

plt.show()
