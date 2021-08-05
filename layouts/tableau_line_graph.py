import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

tableau_line_graph = dbc.Col([
    dbc.Card([
        dbc.CardHeader([    
            dbc.Row([
                dbc.Col(html.H4('COVID-19 By Month'), align='start'),
            ], className='card-modal-btn'),
        ], className='primary-color'),
        dbc.CardBody([
            html.Div(id='tableauLineGraph')
        ], className='secondary-color')
    ])
], xs=12, sm=12, md=12, lg=12, xl=4)