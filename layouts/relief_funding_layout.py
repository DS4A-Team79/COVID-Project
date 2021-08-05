import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from layouts.tableau_line_graph import tableau_line_graph

relief_funding_visualization_colors = {
    'background': '#2A4083',
    'text': '#836D2A'
}

# dataframes, one for each visualization
per_state_funding_2020_df = pd.read_csv('data/per_state_funding_2020.csv', index_col=False)
per_capita_funding_2020_df = pd.read_csv('data/per_capita_funding_2020.csv', index_col=False)
per_state_funding_2021_df = pd.read_csv('data/per_state_funding_2021.csv', index_col=False)
per_capita_funding_2021_df = pd.read_csv('data/per_capita_funding_2021.csv', index_col=False)

# creating a bar chart for each dataframe
per_state_fig_2020 = px.bar(per_state_funding_2020_df, x="State", y="Total Funds for 2020 (in billions)", barmode="group")
per_capita_fig_2020 = px.bar(per_capita_funding_2020_df, x="State", y="Funds Per Person (2020)", barmode="group")
per_state_fig_2021 = px.bar(per_state_funding_2021_df, x="State", y="Total Funds for 2021 (in billions)", barmode="group")
per_capita_fig_2021 = px.bar(per_capita_funding_2021_df, x="State", y="Funds Per Person (2021)", barmode="group")
                             
#configuring how each figure looks
per_state_fig_2020.update_layout(
    plot_bgcolor=relief_funding_visualization_colors['background'],
    paper_bgcolor=relief_funding_visualization_colors['background'],
    font_color=relief_funding_visualization_colors['text']
)

per_capita_fig_2020.update_layout(
    plot_bgcolor=relief_funding_visualization_colors['background'],
    paper_bgcolor=relief_funding_visualization_colors['background'],
    font_color=relief_funding_visualization_colors['text']
)

per_state_fig_2021.update_layout(
    plot_bgcolor=relief_funding_visualization_colors['background'],
    paper_bgcolor=relief_funding_visualization_colors['background'],
    font_color=relief_funding_visualization_colors['text']
)

per_capita_fig_2021.update_layout(
    plot_bgcolor=relief_funding_visualization_colors['background'],
    paper_bgcolor=relief_funding_visualization_colors['background'],
    font_color=relief_funding_visualization_colors['text']
)
    
# dropdown menus for each year, as one space is dedicated to 2020 and the other for 2021
dropdown_2020 = dcc.Dropdown(
    id='dropdown_2020',
    options=[
        {'label': 'Relief per State', 'value': 'rps'},
        {'label': 'Relief per Capita', 'value': 'rpc'},
    ],
    value='rps',
    searchable=False,
    clearable=False,
    style={'color': '#2A4083'}
)

dropdown_2021 = dcc.Dropdown(
    id='dropdown_2021',
    options=[
        {'label': 'Relief per State', 'value': 'rps'},
        {'label': 'Relief per Capita', 'value': 'rpc'},
    ],
    value='rps',
    searchable=False,
    clearable=False,
    style={'color': '#2A4083'}
)

graph_title_2020 = html.H3(
    id='graph_title_2020',
    children='',
    style={
        'textAlign': 'center',
        'color': relief_funding_visualization_colors['text'],
        'background-color': relief_funding_visualization_colors['background']
    }
)

graph_title_2021 = html.H3(
    id='graph_title_2021',
    children='',
    style={
        'textAlign': 'center',
        'color': relief_funding_visualization_colors['text'],
        'background-color': relief_funding_visualization_colors['background']
    }
)

geo_map = dbc.Row([
    tableau_line_graph,
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([    
                dbc.Row([
                    dbc.Col(html.H4('Geospatial Map'), align='start'),
                    dbc.Col(dbc.Button('?', id='open-modal-relief-geomap', n_clicks=0, color='info'), width=1, align='end')
                ], className='card-modal-btn'),
            ], className='primary-color'),
            dbc.CardBody([
                dbc.Modal([
                    dbc.ModalHeader(html.B('Relief Funding Geospatial Map Modal'),),
                    dbc.ModalBody([
                        html.P('Some Text'),
                        html.P('Some more text'),
                    ]),
                    dbc.ModalFooter(dbc.Button('Close', id='close-modal-relief-geomap', className='sm-auto', n_clicks=0),)
                ], id='modal-relief-geomap', is_open=False),
                html.Div(id='tableauReliefFundingMap'),
            ], className='secondary-color')
        ]), xs=12, sm=12, md=12, lg=12, xl=8
    ),
#     dbc.Col(
#          dbc.Card([
#             dbc.CardHeader([    
#                 dbc.Row([
#                     dbc.Col(html.H4('Metric Used In Map'), align='start'),
#                 ], className='card-modal-btn'),
#             ], className='primary-color'),
#             dbc.CardBody([
#                 dbc.Row(
#                     dbc.Col("Extension of larger card")
#                 ),
#             ], className='secondary-color')
#         ]), width = "auto")
], className='wrapper card-visualization-layout')

findings_row = dbc.Row([
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H4('Funding in 2020'), width='auto', align='center')
                ], justify='center')
            ], className='primary-color'),
            dbc.CardBody([
                graph_title_2020,
                dcc.Graph(id='fundings_graph_2020'),
                dropdown_2020,
            ], className='secondary-color')
        ]), xs=12, sm=12, md=12, lg=6, xl=6
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H4('Funding in 2021'), width='auto', align='center'),
                ], justify='center')
            ], className='primary-color'),
            dbc.CardBody([
                graph_title_2021,
                dcc.Graph(id='fundings_graph_2021'),
                dropdown_2021,
            ], className='secondary-color')
        ]), xs=12, sm=12, md=12, lg=6, xl=6
    ),
#     dbc.Col(
#         dbc.Card([
#             dbc.CardHeader([
#                 dbc.Row([
#                     dbc.Col(html.H4('Finding 3'), width='auto', align='center'), 
#                 ], justify='center')
#             ], className='primary-color'),
#             dbc.CardBody([
#                 'Load Visualization Here!',
#             ], className='secondary-color')
#         ])
#     ),
], className='wrapper', align='around')  


relief_funding_layout = html.Div([
    geo_map,
    findings_row,
], className='container-visualization-layout')