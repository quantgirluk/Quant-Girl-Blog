import pandas as pd
import plotly.express as px

data = pd.read_csv('../data/wipo_data.csv')
# df = data
df = data.sort_values(by='GDP per capita (PPP$ logarithmic scale)')



# df['x'] = df['GDP per capita (PPP$ logarithmic scale)']
# df['y'] = df['GII score']
#
#
#
# import statsmodels.formula.api as smf
#
# model = smf.ols(formula='y ~ I(x**3 + x**2 + x)', data=df).fit()
# predicted = model.predict(df.x)
#
# from scipy.interpolate import CubicSpline
#
# d = df[['x', 'SPLINE']].drop_duplicates(['x'], keep='first')
#
#
# # cs = CubicSpline(d['x'], d['y'])
#
# import numpy as np
# xs = np.arange(7, 12, 0.1)

fig = px.scatter(df, x='GDP per capita (PPP$ logarithmic scale)', y='GII score',
                 size='POP',
                 size_max=50,
                 color='STATUS',
                 height=800, width=1200,
                 hover_name='NAME',
                 color_discrete_sequence=px.colors.qualitative.Bold,
                 template='plotly_white',
                 title='Innovation relative to economic development')

# fig = fig.add_scatter(x=d['x'],
#                 y=d['SPLINE'], name='Cubic Spline')

# fig.add_scatter(x=d.x, y=predicted, name="Fitted Polynomial")
# fig.add_scatter(x=xs, y=cs(xs), name="Cubic Spline Fitted Polynomial")

fig.show()
