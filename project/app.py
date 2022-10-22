#!/usr/bin/env python3.6.7
# -*- coding: UTF-8 -*-
"""
Author: Patrick

Date: 2021/6/22 1:09

Docs: 
    
"""
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

from depoverty import layout as dplayout
from boxplot import layout as bxlayout

px.set_mapbox_access_token(
    "pk.eyJ1IjoicGF0cmlja3BybyIsImEiOiJja3E2cWZ5OXAwMHcwMm5zM3NoNTYwcnV5In0.KvBQYukBha-vWqMJp2isqw")

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 2rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "10rem 10rem",
}

sidebar = html.Div(
    [
        html.H4("Poverty", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Rehabilitate", href="/rehabilitate", active="exact"),
                dbc.NavLink("Distribution", href="/distribution", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div(
    [
        dcc.Location(id="url"), sidebar, content,
    ]
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return
    elif pathname == "/rehabilitate":
        return dplayout
    elif pathname == "/distribution":
        return bxlayout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


df_data = pd.read_csv('data/use.csv')
df_data['density'] = df_data['a4']*1.0/df_data['a1']


@app.callback(
    Output("box-plot", "figure"),
    Input("y-axis", "value"))
def generate_chart(y):
    fig = px.box(df_data, x='year', y=y)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
