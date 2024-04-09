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

data = yf.download('GC=F', interval='1wk')

plt.figure(figsize=(12, 6))
data['Close'].plot(color='blue', title="Gold\n Historical Index Close Value")
plt.show()
