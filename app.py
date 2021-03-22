import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing
cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')

# Building our Graphs
cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')
fig1 = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
fig1.update_layout(mapbox_style="open-street-map")


# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('Dashboard of Svitlana'),

    html.Div('Example of map'),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
