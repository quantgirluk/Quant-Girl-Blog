import yfinance as yf
import plotly.express as px
import chart_studio.plotly as py

data = yf.download('^VIX')
data['Color'] = 'Red'

fig = px.line(data, x=data.index, y='Close',
              title='CBOE Volatility Index (^VIX)',
              color_discrete_sequence=['blue'],
              )

# This styles the line
fig.update_traces(line=dict(width=1.25))
# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=False
        ),
        type="date"
    )
)

fig.update_layout(yaxis1=dict(showgrid=True))
fig.update_layout(template="plotly_white")

# Footnotes
fig.add_annotation(xref='paper', x=0, yref='paper', y=-0.1,
                   text="Source: Yahoo Finance", showarrow=False, font_size=10
                   )

fig.add_annotation(xref='paper', x=0, yref='paper', y=-0.15,
                   text="Daily Time Series: ^VIX",
                   showarrow=False, font_size=10
                   )

fig.add_annotation(xref='paper', x=1, yref='paper', y=-0.1,
                   text="@Quant_Girl", showarrow=False,
                   font=dict(size=12, color='maroon', family='PT Serif Caption')
                   )
PUBLISH = False
if PUBLISH:
    py.plot(fig, filename='August_2024_VIX', auto_open=True)

import plotly

# plotly.offline.plot(fig, filename='../charts/08_august_2024_vix.html')
fig.show()
