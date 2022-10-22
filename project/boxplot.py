#!/usr/bin/env python3.6.7
# -*- coding: UTF-8 -*-
"""
Author: Patrick

Date: 2021/6/22 0:52

Docs: 
    
"""
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output

df = pd.read_csv('data/use.csv')
# fig = px.box(df, x='year', y='f1')
# fig2 = px.box(df, x='year', y='f2')
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

df['density'] = df['a4']*1.0/df['a1']

import dash
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis',
        options=[
            {'value': 'density', 'label': 'pop density'},
            {'value': 'f1', 'label': 'F1'},
            {'value': 'f2', 'label': 'F2'},
            {'value': 'IMPI', 'label': 'IMPI'},
        ],
        value='density',
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="box-plot"),
])

if __name__ == '__main__':
    app = dash.Dash()
    app.layout = layout

    app.run_server()
