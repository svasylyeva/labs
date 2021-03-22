import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing
cities = pd.read_csv('https://raw.githubusercontent.com/hflabs/city/master/city.csv')

# Building our Graphs

map_center = go.layout.mapbox.Center(lat=capital['geo_lat'].values[0], lon=capital['geo_lon'].values[0])
fig_map = go.Figure(go.Scattermapbox(lat=cities['geo_lat'], lon=cities['geo_lon']))

fig_map.update_layout(mapbox_style="open-street-map",
                  mapbox=dict(center=map_center, zoom=2))

# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('Dashboard of Svitlana'),

    html.Div('Example of map'),

    dcc.Graph(
        id='example-graph',
        figure=fig_map
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
