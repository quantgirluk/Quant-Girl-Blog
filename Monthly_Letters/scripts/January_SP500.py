import chart_studio.plotly as py
import numpy as np
import plotly.express as px
import yfinance as yf

# Get the data
# data_weekly = yf.download('^SPX', interval='1wk')
data_weekly = yf.download('^N225', interval='1wk')

# Calculate returns
kind = 'standard'
df = data_weekly
if kind == 'standard':
    column = 'Returns'
    df.loc[:, column] = 100 * (df['Adj Close'] - df['Adj Close'].shift(1)) / df['Adj Close']

elif kind == 'log':
    column = 'Log-Returns'
    df.loc[:, column] = np.log(df['Adj Close']) - np.log(df['Adj Close'].shift(1))

# Add the year and decade columns and drop the nas
df = df.reset_index()
df['year'] = df['Date'].dt.year
df['Decade'] = [int(np.floor(year / 10) * 10) for year in np.array(df["year"])]
df = df.dropna()

# Plot
fig = px.box(data_frame=df, x='Decade', y='Returns', labels={'Returns': "Returns (%)"},
             color='Decade',
             hover_data={'Date': True, 'Returns': ':.2f', 'High': ':.2f', 'Decade': False},
             notched=True, color_discrete_sequence=px.colors.qualitative.Bold
             )
fig.update_layout(
    # title='S&P500 Historical Weekly Returns',
    title='Nikkei225 Historical Weekly Returns',
    autosize=False,
    width=1000,
    height=600,
    yaxis=dict(autorange=True,
               showgrid=True,
               zeroline=True,
               dtick=5,
               gridwidth=1,
               zerolinecolor='rgb(255, 255, 255)',
               zerolinewidth=2,
               ),
    margin=dict(l=40,
                r=30,
                b=80,
                t=100,
                ),
    showlegend=False
)
fig.update_layout(template="plotly_white")

PUBLISH = True
if PUBLISH:
    # py.plot(fig, filename='Jan_2024_SP500_Plotly', auto_open=True)
    py.plot(fig, filename='Feb_2024_Nikkei225_Plotly', auto_open=True)
fig.show()
