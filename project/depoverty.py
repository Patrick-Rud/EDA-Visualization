#!/usr/bin/env python3.6.7
# -*- coding: UTF-8 -*-
"""
Author: Patrick

Date: 2021/6/21 22:13

Docs: 
    
"""
import plotly.express as px
import pandas as pd
import json

px.set_mapbox_access_token(
    "pk.eyJ1IjoicGF0cmlja3BybyIsImEiOiJja3E2cWZ5OXAwMHcwMm5zM3NoNTYwcnV5In0.KvBQYukBha-vWqMJp2isqw")

df = pd.read_csv('poverty/accurate/use.csv')
with open('poverty/accurate/poverty.json', 'r', encoding='utf-8') as f:
    gj = json.load(f)

# fig = px.scatter_geo(df, 'latitude', 'longitude', locations='county', color='year')
fig = px.scatter_mapbox(df, 'latitude', 'longitude', color='year', animation_frame='year', animation_group='county',
                        range_color=[2016, 2020], zoom=1)
fig2 = px.scatter_mapbox(df, 'latitude', 'longitude', color='year', zoom=2)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=fig2)),
                    dbc.Col(dcc.Graph(figure=fig))
                ],
                # style={
                #     'height': '600px'
                # }
            ),
        ],
        # style={
        #     'background-color': '#ededef',  # 设置背景颜色
        #     'max-width': '1200px',  # 为Container部件设置最大宽度
        #     'border-radius': '12px',
        #     'height': '600px',
        #     'columnCount': 2,
        #     'text-align': 'center',
        #     'margin': 'auto',
        #     'position': 'absolute',
        #     'top': 0,
        #     'left': 0,
        #     'right': 0,
        #     'bottom': 0
        # }
    )

])


if __name__ == '__main__':
    app = dash.Dash()
    app.layout = layout

    app.run_server()
