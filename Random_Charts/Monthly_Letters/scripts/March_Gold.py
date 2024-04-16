import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
plt.style.use(quant_pastel)
plt.rcParams["figure.figsize"] = (10, 7)
plt.rcParams["figure.dpi"] = 100
plt.rc('font', family='sans-serif')
plt.rc('font', serif='Apple SD Gothic Neo')
plt.rcParams.update({'font.size': 12})

data = yf.download('CC=F GC=F')
data['High'].plot(title="Cocoa (CC) and Gold (GC)\n Futures Historical High Value")
plt.savefig("./charts/03_march_gold_cocoa", dpi=300)
plt.show()