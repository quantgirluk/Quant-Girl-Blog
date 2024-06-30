from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
style = quant_pastel

colors = ['#000D6B', '#D82148', '#488FB1', '#99DDCC', '#480032', '#F9B208', '#D8D2CB', '#2EB086', '#05595B']

dta = pd.read_excel('../data/cpi_series_uk.xls', sheet_name='data',
                    skiprows=184, header=None, names=['Date', 'CPI'],
                    parse_dates=[0])

dta = dta.set_index('Date')
dta['Year'] = pd.DatetimeIndex(dta.index).year
dta['Decade'] = dta.Year // 10 * 10
dta['Mean'] = dta[['CPI', 'Decade']].groupby('Decade')['CPI'].transform("mean")

bins = sorted([datetime(1945, 6, 30), datetime(1951, 10, 1),
               datetime(1964, 10, 1), datetime(1970, 6, 1),
               datetime(1974, 3, 1), datetime(1979, 5, 1),
               datetime(1997, 5, 1), datetime(2010, 5, 1),
               datetime(2024, 8, 1)])

dta['Period'] = pd.cut(dta.index, bins, duplicates='drop')
dta['Mean_Period'] = dta[['CPI', 'Period']].groupby('Period')['CPI'].transform("mean")
dates = dta.index

with plt.style.context(style):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    for i, period in enumerate(dta.Period.unique()):
        subpop = dta[dta.Period == period]
        c = 'royalblue' if (i % 2 == 0) else 'red'
        if i == 0:
            party = 'Conservative'
        elif i == 1:
            party = 'Labour'
        else:
            party = None
        ax.plot(subpop.index, subpop.CPI, '-', color=c)
        ax.plot(subpop.index, subpop.Mean_Period, linestyle='dotted', color=c, drawstyle='steps-post')
        ax.fill_between(subpop.index, subpop.Mean_Period, color=c, alpha=0.1, label=party)
        ax.fill_between(subpop.index, subpop.Mean_Period, subpop.CPI, color=c, alpha=0.2)

    xpos = datetime(1992, 9, 1)
    ypos = 9.6
    after = dates[dates >= xpos]
    ax.text(xpos, ypos, 'Start of Inflation Targeting', horizontalalignment='left', fontsize=8)
    ax.annotate('', xy=(xpos, 0), xytext=(xpos, ypos - 0.5), color='green',
                arrowprops=dict(arrowstyle='-', edgecolor='green', ls='solid', relpos=(0, 0)), fontsize=8)
    ax.plot(xpos, ypos - 0.5, marker="o", color='green')
    ax.fill_between(after, [3] * len(after), [1] * len(after), color='green', alpha=0.1, label='1-3%')

    ax.set_ylim(-1, 13)
    ax.spines[['top', 'left', 'right']].set_visible(False)
    plt.legend(loc='upper right', ncol=3, fontsize='8')
    plt.grid(axis='both', color='0.95')

    # Add in red line and rectangle on top
    ax.plot([0.05, .95], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.6)
    ax.add_patch(plt.Rectangle((0.05, .98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure,
                               clip_on=False, linewidth=0))

    # Add in title and subtitle
    ax.text(x=0.05, y=.93, s="Consumer Price Index (CPI)", transform=fig.transFigure, ha='left', fontsize=12,
            weight='bold',
            alpha=.9)
    ax.text(x=0.05, y=.90, s=r"Historical Monthly Time Series 1989 to 2024", transform=fig.transFigure, ha='left',
            fontsize=10,
            alpha=.9)

    # Set source text
    ax.text(x=0.05, y=0.05, s="Note: Dotted lines are averages\nSource: Office for National Statistics", fontsize=10,
            ha="left", alpha=.8,
            transform=fig.transFigure)
    ax.text(x=0.9, y=0.05, s="@Quant_Girl", ha="right",
            transform=fig.transFigure,
            fontdict={'fontsize': 10, 'fontweight': 'bold', 'family': 'sans-serif', 'fontname': 'PT Serif Caption',
                      'color': 'black',
                      })

    # Adjust the margins around the plot area
    plt.subplots_adjust(left=None, bottom=0.15, right=None, top=0.85, wspace=None, hspace=None)

    # plt.savefig(r"Figures/2023_CPI_Gov.png")
    plt.show()

# ----------------------------------------------------------------

dta = pd.read_csv('../data/bank_rate_history_boe.csv',
                  # skiprows=184,
                  header=1,
                  names=['Date', 'Rate'],
                  # infer_datetime_format = True,
                  parse_dates=[0])

dta = dta[dta.Date >= datetime(1989, 1, 1)].set_index('Date')
rates = dta['Rate']

dta['Year'] = pd.DatetimeIndex(dta.index).year
dta['Decade'] = dta.Year // 10 * 10
dta['Mean'] = dta[['Rate', 'Decade']].groupby('Decade')['Rate'].transform("mean")

bins = sorted([datetime(1989, 1, 1),
               datetime(1997, 5, 1), datetime(2010, 5, 1),
               datetime(2024, 8, 1)
               ])

dta['Period'] = pd.cut(dta.index, bins, duplicates='drop')
dta['Mean_Period'] = dta[['Rate', 'Period']].groupby('Period')['Rate'].transform("mean")

with plt.style.context(style):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax.set_ylim(-2, 18)
    for i, period in enumerate(dta.Period.unique()):
        subpop = dta[dta.Period == period]
        c = 'royalblue' if (i % 2 == 0) else 'red'
        if i == 0:
            party = 'Conservative'
        elif i == 1:
            party = 'Labour'
        else:
            party = None
        ax.plot(subpop.index, subpop.Rate, '-', color=c, drawstyle='steps-post')
        ax.plot(subpop.index, subpop.Mean_Period, linestyle='dotted', color=c, drawstyle='steps-post')
        ax.fill_between(subpop.index, subpop.Mean_Period, color=c, alpha=0.1, label=party)
        ax.fill_between(subpop.index, subpop.Mean_Period, subpop.Rate, color=c, alpha=0.2, step="post")

    dates = dta.index
    xpos = datetime(1992, 9, 1)
    ypos = 15
    after = dates[dates >= xpos]
    ax.text(xpos, ypos, 'Start of Inflation Targeting', horizontalalignment='left', fontsize=8)
    ax.annotate('', xy=(xpos, 0), xytext=(xpos, ypos - 0.5), color='green',
                arrowprops=dict(arrowstyle='-', edgecolor='green', ls='solid', relpos=(0, 0)), fontsize=8)
    ax.plot(xpos, ypos - 0.5, marker="o", color='green')

    ax.spines[['top', 'left', 'right']].set_visible(False)

    # Add in red line and rectangle on top
    ax.plot([0.05, .95], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.6)
    ax.add_patch(plt.Rectangle((0.05, .98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure,
                               clip_on=False, linewidth=0))

    # Add in title and subtitle
    ax.text(x=0.05, y=.93, s="Bank of England Rate", transform=fig.transFigure, ha='left', fontsize=12, weight='bold',
            alpha=.9)
    ax.text(x=0.05, y=.90, s="Historical Time Series 1989 to 2024", transform=fig.transFigure, ha='left',
            fontsize=10,
            alpha=.9)
    # Set source text
    ax.text(x=0.05, y=0.05, s="Note: Dotted lines are averages\nSource: Bank of England.", fontsize=10, ha="left",
            alpha=.8,
            transform=fig.transFigure)
    ax.text(x=0.9, y=0.05, s="@Quant_Girl", ha="right",
            transform=fig.transFigure,
            fontdict={'fontsize': 10, 'fontweight': 'bold', 'family': 'sans-serif', 'fontname': 'PT Serif Caption',
                      'color': 'black',
                      })

    # Adjust the margins around the plot area
    plt.subplots_adjust(left=None, bottom=0.15, right=None, top=0.85, wspace=None, hspace=None)

    plt.legend(loc='upper right', ncol=1, fontsize='8')
    plt.grid(axis='both', color='0.95')
    # plt.savefig(r"Figures/2023_Rate_Gov.png")
    plt.show()
