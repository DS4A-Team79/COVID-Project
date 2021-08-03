import dash
from dash.dependencies import ClientsideFunction, Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

external_scripts = [
    
    {'type': 'text/javascript', 'src': 'https://public.tableau.com/javascripts/api/tableau-2.min.js'},

]

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts, suppress_callback_exceptions=True)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts, suppress_callback_exceptions=True, title='Covid-19 Analysis', assets_folder='static', assets_url_path='static')