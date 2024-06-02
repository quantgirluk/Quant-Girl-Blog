import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yfinance as yf

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
plt.style.use(quant_pastel)

plt.rc('font', family='sans-serif')
plt.rc('font', serif='Apple SD Gothic Neo')
plt.rcParams.update({'font.size': 14})

data = yf.download('^IXIC')



ax = data['Close'].plot.area(figsize=(12, 6), alpha=0.25)

ax.set_title("Nasdaq Composite Index - Historical Close Levels\n", fontsize=16)
ax.set_xlabel('Date')
ax.set_ylabel(r'Points')

# Add in red line and rectangle on top
ax.plot([0.0, .98], [1., 1.], transform=ax.transAxes, clip_on=False, color='#E3120B', linewidth=.6)
ax.add_patch(plt.Rectangle((0.0,1.), 0.04, -0.02, facecolor='#E3120B', transform=ax.transAxes, clip_on=False, linewidth = 0))

# format the ticks only for years on the major ticks
years = mdates.YearLocator(5)   # every 5 year
years_fmt = mdates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

ax.set_ylim(0, 18000)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")

ax.xaxis.grid() # horizontal lines
ax.set_axisbelow(True)

ax.spines[['top']].set_visible(False)
ax.spines[['right', 'bottom']].set_visible(True)

# matplotlib.patch.Patch properties
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
ax.figure.savefig("../charts/05_may_nasdaq", dpi=300)
plt.show()


tickers = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'META']
data = yf.download(tickers, start='2014-01-01', )
highs = [('Close', 'MSFT'),
         ('Close', 'AAPL'),
         ('Close', 'NVDA'),
         ('Close', 'AMZN'),
         ('Close', 'META'),
         ]

ax = data[highs].plot(figsize=(12, 8))
ax.set_title(label="Nasdaq Composite Largest Components - Historical Close Prices", fontsize=16)
ax.set_xlabel('Date')
ax.set_ylabel(r'Price (\$)')

ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.xaxis.grid()
ax.set_axisbelow(True)

ax.spines[['top']].set_visible(False)
ax.spines[['right', 'bottom']].set_visible(True)

 # Add in red line and rectangle on top
ax.plot([0.0, .98], [1., 1.], transform=ax.transAxes, clip_on=False, color='#E3120B', linewidth=.6)
ax.add_patch(plt.Rectangle((0.0,1.), 0.04, -0.02, facecolor='#E3120B', transform=ax.transAxes, clip_on=False, linewidth = 0))


plt.tight_layout()
ax.figure.savefig("../charts/05_may_nasdaq_largest_components", dpi=300)

plt.show()
