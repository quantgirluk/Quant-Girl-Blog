# Author: @Quant_Girl
# Title: Bitcoin Weakly Movement
# Type: Line Chart + Vertical Bar Chart

import datetime as dt
import chart_studio.plotly as py
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
from plotly.subplots import make_subplots

start = dt.datetime(2019, 12, 30)

btc = yf.download('BTC-USD', start=start, interval="1wk")
btc = btc.assign(returns=btc['Close'].pct_change(1))
btc = btc.assign(returns_sign=np.sign(btc["returns"]))
colors = {-1.0: "rgba(255,0,0, 0.75)", 1.0: "rgba(0,153,76, 0.75)"}

# Create figure
fig = make_subplots(specs=[[{"secondary_y": True}]],
                    )
# Add traces
fig.add_trace(
    go.Bar(x=btc.index, y=btc.returns, marker=dict(color=btc.returns_sign.map(colors)),
           name="Bitcoin weakly % change"),
    secondary_y=False)

fig.add_trace(
    go.Scatter(x=btc.index, y=btc.Close, mode='lines', line_color='rgba(0, 102 , 204, 1.0)',
               name="BTC/USD DOLLAR"),
    secondary_y=True)

# Figure title and labels
fig.update_layout(title_text="Bitcoin Weakly Movement", height=600, width=1000)
fig.update_xaxes(title_text="")
fig.update_yaxes(title_text="<b></b>USD", secondary_y=True)
fig.update_yaxes(title_text="<b></b>Percent", secondary_y=False)

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
            visible=True
        ),
        type="date"
    )
)

fig.update_layout(dict(yaxis2={'anchor': 'x', 'overlaying': 'y', 'side': 'left', 'range': [0, 80000],
                               'domain': [0, 1], 'position': 0.5},
                       yaxis={'anchor': 'x', 'range': [-0.5, 0.5],
                              'domain': [0.0, 1.0],
                              'side': 'right'}))
fig.update_layout(yaxis1=dict(showgrid=True))
fig.update_layout(template="plotly_white")
fig.update_layout(showlegend=False)

# Footnotes
fig.add_annotation(xref='paper', x=0, yref='paper', y=-0.4,
                   text="Source: Yahoo Finance", showarrow=False, font_size=10
                   )

fig.add_annotation(xref='paper', x=0, yref='paper', y=-0.45,
                   text="Weekly Time Series: BTC-USD",
                   showarrow=False, font_size=10
                   )

fig.add_annotation(xref='paper', x=1, yref='paper', y=-0.4,
                   text="@Quant_Girl", showarrow=False,
                   font=dict(size=12, color='#a70684', family='PT Serif Caption')
                   )

PUBLISH = False
if PUBLISH:
    py.plot(fig, filename='April2024_Bitcoin_Plotly', auto_open=True)

fig.show()
