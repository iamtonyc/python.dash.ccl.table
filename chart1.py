import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]
# py.iplot(data, filename='simple_candlestick')
IFrame('http://stackoverflow.org', width=700, height=350)