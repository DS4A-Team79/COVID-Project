import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

geo_map = dbc.Card([
    dbc.CardHeader([    
        dbc.Row([
            dbc.Col(html.H4('Geospatial Map')),
            dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='end')
        ], justify='between', className='card-modal-btn'),
    ]),
    dbc.CardBody([
        dbc.Modal([
            dbc.ModalHeader([
                'Info',
                dbc.Button('Close', id='close-modal-geo', className='sm-auto', n_clicks=0),
            ]),
            dbc.ModalBody([
                html.P('Some Text'),
                html.P('Some more text'),
            ]),
            dbc.ModalFooter("Some other text here"),
        ], id='modal-geo', is_open=False),
        dbc.Row(
            dbc.Col("Where the actual map will go")
        ),
    ])
],
#     className='card-visualization-layout'
    color='primary',
)

first_row_visualizations = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader([
            dbc.Row([
                dbc.Col(html.H4('Visualization 1'), width='auto', align='start'), 
                dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
            ], justify='between')
        ]),
        dbc.CardBody('Load Visualization Here!')
    ],
        color='primary'
    ),
    dbc.Card([
        dbc.CardHeader([
            dbc.Row([
                dbc.Col(html.H4('Visualization 2'), width='auto', align='start'),
                dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
            ] ,justify='between')
        ]),
        dbc.CardBody('Load Visualization Here!')
    ],
        color='primary'
    )
],
    className='wrapper card-visualization-layout'
)

second_row_visualizations = dbc.CardDeck([
    dbc.Card([
        dbc.CardHeader([
            dbc.Row([
                dbc.Col(html.H4('Visualization 3'), width='auto', align='start'), 
                dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info'), width=1, align='start', className='card-modal-btn'),
            ], justify='between')
        ]),
        dbc.CardBody('Load Visualization Here!')
    ],
#         className='card-layout-sm',
        color='primary',
    ),
    dbc.Card([
        dbc.CardHeader([
            dbc.Row([
                dbc.Col(html.H4('Visualization 4'), width='auto', align='start'),
                dbc.Col(dbc.Button('?', id='open-modal-geo', n_clicks=0, color='info',), width=1, align='start', className='card-modal-btn'),
            ], justify='between')
        ]),
        dbc.CardBody('Load Visualization Here!')
    ],
        className='child-card',
        color='primary',
    )
],
    className='wrapper card-visualization-layout'
)

visualization_layout = html.Div([
    geo_map,
    first_row_visualizations,
    second_row_visualizations,
], className='container-visualization-layout')