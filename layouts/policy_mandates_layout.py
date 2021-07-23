import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

geo_map = dbc.Row([
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
                dbc.Row(
#                     dbc.Col("Where the actual map will go")
#                     html.Div(id='tableauViz', onload='initViz();')
                    html.Iframe(id='tableauViz')
                ),
            ], className='secondary-color')
        ])
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([    
                dbc.Row([
                    dbc.Col(html.H4('Metric Used In Map'), align='start'),
                ], className='card-modal-btn'),
            ], className='primary-color'),
            dbc.CardBody([
                dbc.Row(
                    dbc.Col("Extension of larger card")
                ),
            ], className='secondary-color')
        ]), width = "auto")
], className='wrapper card-visualization-layout')

policy_mandates_layout = html.Div([
    geo_map,
], className='container-visualization-layout')