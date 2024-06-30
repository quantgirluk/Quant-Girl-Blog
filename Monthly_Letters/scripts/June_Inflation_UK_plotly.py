from datetime import datetime

import pandas as pd

colors = ['#000D6B', '#D82148', '#488FB1', '#99DDCC', '#480032', '#F9B208', '#D8D2CB', '#2EB086', '#05595B']
dta = pd.read_excel('../data/cpi_series_uk.xls', sheet_name='data',
                    skiprows=184, header=None, names=['Date', 'CPI'],
                    parse_dates=[0])

dta = dta.set_index('Date')
dta['Year'] = (pd.DatetimeIndex(dta.index)).year
dta['Decade'] = dta.Year // 10 * 10
dta['Mean'] = dta[['CPI', 'Decade']].groupby('Decade')['CPI'].transform("mean")

bins = sorted([datetime(1945, 6, 30), datetime(1951, 10, 1),
           datetime(1964, 10, 1), datetime(1970, 6, 1),
           datetime(1974, 3, 1), datetime(1979, 5, 1),
           datetime(1997, 5, 1), datetime(2010, 5, 1),
           datetime(2024, 5, 1)])

dta['Period'] = pd.cut(dta.index, bins, duplicates='drop')
dta['Mean_Period'] = dta[['CPI', 'Period']].groupby('Period')['CPI'].transform("mean")
labels = ['1989: 5.2', '1990-1999: 3.3', '2000-2009: 1.8', '2010-2019: 2.2', '2020-2023: 4.5']
dates = dta.index

inflation = dta['CPI']


import plotly.express as px


fig = px.line(x=dta.index, y=dta.CPI, title="Historical Consumer Price Index (CPI)")
fig.update_layout(xaxis_title="Date", yaxis_title="%")
# Show the plot. This will open a new window in your browser.
fig.show()