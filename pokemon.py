import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

pyo.init_notebook_mode()

pokemon = pd.read_csv('../DataAnalysis/data/pokemon.csv')
x_values = pokemon['Type 1']
y_values = pokemon['HP']
data = [go.Scatter(x=x_values, y=y_values, mode='markers', marker = dict(
    size=10, 
    color='rgb(3,9,9)', 
    symbol='hexagon2', 
    line={'width':1}
))]

layout = go.Layout(
    title = 'Pokemon Type and HP Correlation',
    xaxis = dict(title = 'Type'),
    yaxis = dict(title='Health Points'),
    hovermode = 'closest'
)

fig = go.Figure(data=data, layout = layout)

pyo.iplot(fig)
