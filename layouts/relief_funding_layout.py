import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
# from app import analytical_df

# use this to drop w.e i don't need to save memory
# analytical_df = analytical_df.drop([], axis=1)

# fig_2 = px.bar(analytical_df, x='')

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),

#     html.Div(children='Dash: A web application framework for Python.', style={
#         'textAlign': 'center',
#         'color': colors['text']
#     }),

#     dcc.Graph(
#         id='example-graph-2',
#         figure=fig
#     )
# ])

geo_map = dbc.Row([
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

findings_row = dbc.Row([
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H4('Finding 1'), width='auto', align='start')
                ], justify='between')
            ], className='primary-color'),
            dbc.CardBody([
                'Load Visualization Here!',
            ], className='secondary-color')
        ])
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H4('Finding 2'), width='auto', align='start'),
                ], justify='between')
            ], className='primary-color'),
            dbc.CardBody([
                'Load Visualization Here!',
            ], className='secondary-color')
        ])
    ),
    dbc.Col(
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H4('Finding 3'), width='auto', align='start'), 
                ], justify='between')
            ], className='primary-color'),
            dbc.CardBody([
                'Load Visualization Here!',
            ], className='secondary-color')
        ])
    ),
], className='wrapper')  


relief_funding_layout = html.Div([
    geo_map,
    findings_row,
], className='container-visualization-layout')