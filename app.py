# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
# from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
# import json

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = JupyterDash(__name__, external_stylesheets=external_stylesheets)
# suppress_callback_exceptions=True
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
    
    
# Extra code, might help in the future
    
# Build App
# app = JupyterDash(__name__)
# app.layout = html.Div([
#     html.H1("JupyterDash Demo"),
#     dcc.Graph(id='graph'),
#     html.Label([
#         "colorscale",
#         dcc.Dropdown(
#             id='colorscale-dropdown', clearable=False,
#             value='plasma', options=[
#                 {'label': c, 'value': c}
#                 for c in px.colors.named_colorscales()
#             ])
#     ]),
# ])
# Define callback to update graph
# @app.callback(
#     Output('graph', 'figure'),
#     [Input("colorscale-dropdown", "value")]
# )
# def update_figure(colorscale):
#     return px.scatter(
#         df, x="total_bill", y="tip", color="size",
#         color_continuous_scale=colorscale,
#         render_mode="webgl", title="Tips"
#     )