import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from layouts.tableau_line_graph import tableau_line_graph

geo_map = dbc.Row([
    tableau_line_graph,
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([    
                dbc.Row([
                    dbc.Col(html.H4('Geospatial Map'), align='start'),
                    dbc.Col(dbc.Button('?', id='open-modal-policy-geomap', n_clicks=0, color='info'), width=1, align='end')
                ], className='card-modal-btn'),
            ], className='primary-color'),
            dbc.CardBody([
                dbc.Modal([
                    dbc.ModalHeader(html.B('Policy Mandates GeoSpatial Map Modal'),),
                    dbc.ModalBody([
                        html.P('Some Text'),
                        html.P('Some more text'),
                    ]),
                    dbc.ModalFooter(dbc.Button('Close', id='close-modal-policy-geomap', className='sm-auto', n_clicks=0),)
                ], id='modal-policy-geomap', is_open=False),
#                 html.Div(id='tableauPolicyMandatesMap'),
                dbc.Container(id='tableauPolicyMandatesMap', fluid=True)
            ], className='secondary-color')
        ])
    ),
#     dbc.Col(
#         dbc.Card([
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
], className='card-visualization-layout')

findings_row = dbc.Row([
    dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.Img(src='../assets/bans_per_county_seaborn.png', className='img-resizing', style={'width':'100%'})
            ], className='secondary-color')
        ]), xs=12, sm=12, md=12, lg=6, xl=6
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.Img(src='../assets/bans_per_county.png', className='img-resizing', style={'width':'100%'})
            ], className='secondary-color')
        ]), xs=12, sm=12, md=12, lg=6, xl=6
    ),
], align='around')  

policy_mandates_layout = html.Div([
    geo_map,
    findings_row,
], className='container-visualization-layout')