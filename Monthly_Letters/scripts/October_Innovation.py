import chart_studio.plotly as py
import pandas as pd
import plotly.express as px

data = pd.read_csv('../data/wipo_data.csv')
df = data.sort_values(by='GDP per capita (PPP$ logarithmic scale)')

fig = px.scatter(df, x='GDP per capita (PPP$ logarithmic scale)', y='GII score',
                 size='POP',
                 size_max=50,
                 color='STATUS',
                 height=800, width=1200,
                 hover_name='NAME',
                 color_discrete_sequence=px.colors.qualitative.Bold,
                 template='plotly_white',
                 title='Innovation relative to economic development <br>Global Innovation Index 2024')

PUBLISH = True
if PUBLISH:
    py.plot(fig, filename='October_2024_Innovation_Plotly', auto_open=True)
fig.show()
