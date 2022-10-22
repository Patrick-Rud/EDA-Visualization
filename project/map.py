#!/usr/bin/env python3.6.7
# -*- coding: UTF-8 -*-
"""
Author: Patrick

Date: 2021/5/30 14:42

Docs: 
    
"""
import plotly.express as px
import pandas as pd
import json

px.set_mapbox_access_token(
    "pk.eyJ1IjoicGF0cmlja3BybyIsImEiOiJja3E2cWZ5OXAwMHcwMm5zM3NoNTYwcnV5In0.KvBQYukBha-vWqMJp2isqw")

df = pd.read_csv('data/mapuse.csv')
with open('total.json', 'r', encoding='utf-8') as f:
    gj = json.load(f)

df['density'] = df['a4'] * 1.0 / df['a1']

print('data loaded.')

fig = px.choropleth_mapbox(df, gj, locations='county', featureidkey="properties.name", color='density', zoom=2,
                           center={"lat": 38.47, "lon": 106.27}, range_color=(df['density'].min(), df['density'].max()),
                           mapbox_style="carto-positron",
                           animation_frame="year", animation_group="county")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    # dbc.Container(
    #     [
    #         dcc.Graph(fig)
    #     ],
    #     style={
    #         'max-width': '1000px',  # 为Container部件设置最大宽度
    #         'height': '600px',
    #         'margin': 'auto',
    #     }
    # )
    dcc.Graph(figure=fig)
])
app.run_server(use_reloader=False)
