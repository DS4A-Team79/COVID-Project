import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

geo_map = dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader([    
                    dbc.Row([
                        dbc.Col(html.H4('Geospatial Map of COVID-19 By State'), align='start'),
                        dbc.Col(dbc.Button('?', id='open-modal-overview-geomap', n_clicks=0, color='info'), width=1, align='end')
                    ], className='card-modal-btn'),
                ], className='primary-color'),
                dbc.CardBody([
                    dbc.Modal([
                        dbc.ModalHeader(html.B('GeoSpatial Map Modal'),),
                        dbc.ModalBody([
                            html.P('Some Text'),
                            html.P('Some more text'),
                        ]),
                        dbc.ModalFooter(dbc.Button('Close', id='close-modal-overview-geomap', className='sm-auto', n_clicks=0),)
                    ], id='modal-overview-geomap', is_open=False),
                    html.Div(id='tableauOverviewMap')    
                ], className='secondary-color')
            ]), width=True)
    ,
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
                       
overview_layout = html.Div([
    geo_map,
#     side_geo_map,
    findings_row,
#     first_row_visualizations,
#     second_row_visualizations,
], className='container-visualization-layout')



### ignore this
# first_row_visualizations = dbc.CardDeck([
#     dbc.Card([
#         dbc.CardHeader([
#             dbc.Row([
#                 dbc.Col(html.H4('Visualization 1'), width='auto', align='start'), 
#                 dbc.Col(dbc.Button('?', id='open-modal-visualization1', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#             ], justify='between')
#         ], className='primary-color'),
#         dbc.CardBody([
#             'Load Visualization Here!',
#             dbc.Modal([
#                 dbc.ModalHeader('Visualization 1 Modal'),
#                 dbc.ModalBody([
#                     html.P('Some Text'),
#                     html.P('Some more text'),
#                 ]),
#                 dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization1', className='sm-auto', n_clicks=0),),
#             ], id='modal-visualization1', is_open=False),
#         ], className='secondary-color')
#     ],
# #         color='primary'
# #         className='primary-color',
#     ),
#     dbc.Card([
#         dbc.CardHeader([
#             dbc.Row([
#                 dbc.Col(html.H4('Visualization 2'), width='auto', align='start'),
#                 dbc.Col(dbc.Button('?', id='open-modal-visualization2', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#             ] ,justify='between')
#         ], className='primary-color'),
#         dbc.CardBody([
#             'Load Visualization Here!',
#             dbc.Modal([
#                 dbc.ModalHeader('Visualization 2 Info',),
#                 dbc.ModalBody([
#                     html.P('Some Text'),
#                     html.P('Some more text'),
#                 ]),
#                 dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization2', className='sm-auto', n_clicks=0),),
#             ], id='modal-visualization2', is_open=False),
#         ], className='secondary-color')
#     ],
# #         color='primary'
# #         className='primary-color',
#     )
# ],
#     className='wrapper card-visualization-layout'
# )

# second_row_visualizations = dbc.CardDeck([
#     dbc.Card([
#         dbc.CardHeader([
#             dbc.Row([
#                 dbc.Col(html.H4('Visualization 3'), width='auto', align='start'), 
#                 dbc.Col(dbc.Button('?', id='open-modal-visualization3', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#             ], justify='between')
#         ], className='primary-color'),
#         dbc.CardBody([
#             'Load Visualization Here!',
#             dbc.Modal([
#                 dbc.ModalHeader('Visualization 3 Info',),
#                 dbc.ModalBody([
#                     html.P('Some Text'),
#                     html.P('Some more text'),
#                 ]),
#                 dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization3', className='sm-auto', n_clicks=0),),
#             ], id='modal-visualization3', is_open=False),
#         ], className='secondary-color')
#     ],
# #         className='primary-color',
# #         color='primary',
#     ),
#     dbc.Card([
#         dbc.CardHeader([
#             dbc.Row([
#                 dbc.Col(html.H4('Visualization 4'), width='auto', align='start'),
#                 dbc.Col(dbc.Button('?', id='open-modal-visualization4', n_clicks=0, color='info',), width=1, align='start', className='card-modal-btn'),
#             ], justify='between')
#         ], className='primary-color'),
#         dbc.CardBody([
#             'Load Visualization Here!',
#             dbc.Modal([
#                 dbc.ModalHeader('Visualization 4 Info',),
#                 dbc.ModalBody([
#                     html.P('Some Text'),
#                     html.P('Some more text'),
#                 ]),
#                 dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization4', className='sm-auto', n_clicks=0),),
#             ], id='modal-visualization4', is_open=False),
#         ], className='secondary-color')
#     ],
# #         className='primary-color',
# #         color='primary',
#     )
# ],
#     className='wrapper card-visualization-layout'
# )
###

### Below is another format I'm testing out, need to see what our viualizations will look like though
###

# geo_map2 = dbc.Card([
#     dbc.CardHeader([    
#         dbc.Row([
#             dbc.Col(html.H4('Geospatial Map'), align='start'),
#             dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='end')
#         ], className='card-modal-btn'),
#     ], className='primary-color'),
#     dbc.CardBody([
#         dbc.Modal([
#             dbc.ModalHeader(html.B('GeoSpatial Map Modal'),),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-geo', className='sm-auto', n_clicks=0),)
#         ], id='modal-geo', is_open=False),
#         dbc.Row(
#             dbc.Col("Where the actual map will go")
#         ),
#     ], className='secondary-color')
# ])

# side_geo_map = dbc.Card([
#     dbc.CardHeader([    
#         dbc.Row([
#             dbc.Col(html.H4('Geospatial Map'), align='start'),
#             dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='end')
#         ], className='card-modal-btn'),
#     ], className='primary-color'),
#     dbc.CardBody([
#         dbc.Modal([
#             dbc.ModalHeader(html.B('GeoSpatial Map Modal'),),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-geo', className='sm-auto', n_clicks=0),)
#         ], id='modal-geo', is_open=False),
#         dbc.Row(
#             dbc.Col("Extension of larger card")
#         ),
#     ], className='secondary-color')
# ])

# visualization1 = dbc.Card([
#     dbc.CardHeader([
#         dbc.Row([
#             dbc.Col(html.H4('Visualization 1'), width='auto', align='start'), 
#             dbc.Col(dbc.Button('?', id='open-modal-visualization1', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#         ], justify='between')
#     ], className='primary-color'),
#     dbc.CardBody([
#         'Load Visualization Here!',
#         dbc.Modal([
#             dbc.ModalHeader('Visualization 1 Modal'),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization1', className='sm-auto', n_clicks=0),),
#         ], id='modal-visualization1', is_open=False),
#     ], className='secondary-color')
# ], inverse=True, className='card-visualization-layout')

# visualization2 = dbc.Card([
#     dbc.CardHeader([
#         dbc.Row([
#             dbc.Col(html.H4('Visualization 2'), width='auto', align='start'),
#             dbc.Col(dbc.Button('?', id='open-modal-visualization2', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#         ] ,justify='between')
#     ], className='primary-color'),
#     dbc.CardBody([
#         'Load Visualization Here!',
#         dbc.Modal([
#             dbc.ModalHeader('Visualization 2 Info',),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization2', className='sm-auto', n_clicks=0),),
#         ], id='modal-visualization2', is_open=False),
#     ], className='secondary-color')
# ], inverse=True, className='card-visualization-layout')

# visualization3 = dbc.Card([
#     dbc.CardHeader([
#         dbc.Row([
#             dbc.Col(html.H4('Visualization 3'), width='auto', align='start'), 
#             dbc.Col(dbc.Button('?', id='open-modal-visualization3', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
#         ], justify='between')
#     ], className='primary-color'),
#     dbc.CardBody([
#         'Load Visualization Here!',
#         dbc.Modal([
#             dbc.ModalHeader('Visualization 3 Info',),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization3', className='sm-auto', n_clicks=0),),
#         ], id='modal-visualization3', is_open=False),
#     ], className='secondary-color')
# ], inverse=True, className='card-visualization-layout')

# visualization4 = dbc.Card([
#     dbc.CardHeader([
#         dbc.Row([
#             dbc.Col(html.H4('Visualization 4'), width='auto', align='start'),
#             dbc.Col(dbc.Button('?', id='open-modal-visualization4', n_clicks=0, color='info',), width=1, align='start', className='card-modal-btn'),
#         ], justify='between')
#     ], className='primary-color'),
#     dbc.CardBody([
#         'Load Visualization Here!',
#         dbc.Modal([
#             dbc.ModalHeader('Visualization 4 Info',),
#             dbc.ModalBody([
#                 html.P('Some Text'),
#                 html.P('Some more text'),
#             ]),
#             dbc.ModalFooter(dbc.Button('Close', id='close-modal-visualization4', className='sm-auto', n_clicks=0),),
#         ], id='modal-visualization4', is_open=False),
#     ], className='secondary-color')
# ], inverse=True, className='card-visualization-layout')

# top_row = dbc.Row([
#     dbc.Col(geo_map2, width=8),
#     dbc.Col(side_geo_map)
# ])

# card_cols = dbc.CardColumns([
#     visualization1,
#     visualization2,
#     visualization3,
#     visualization4,
#     visualization1,
#     visualization2,
#     visualization3,
#     visualization4,
# ])


# # top row is dedicated to the main visualization (like a geospatial map) and the cols are w.e we have
# visualization_layout = html.Div([
#     top_row,
#     card_cols,
# ], className='container-visualization-layout')