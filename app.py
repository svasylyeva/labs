import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing

x = np.array([1, 2, 3, 4, 5])
y = x * 2

# Building our Graphs
cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')
fig_map = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))
fig_map.update_layout(mapbox_style="open-street-map")


# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('Dashboard example'),

    html.Div('Example of html Container, MAP'),

    dcc.Graph(
        id='example-graph',
        figure=fig_map
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
