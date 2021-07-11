import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Our Journey tab
# our_journey_jumbo = dbc.Jumbotron([
#     dbc.Container([
#         html.H1("Our Journey Content", className="display-3"),
#         html.P(
#             "We can explain here what we did throughout the course of this project",
#             className="lead",
#         ),
#     ],
#         fluid=True,
#     )
# ],
#     fluid=True,
# ),    

# use markdown for easier explaining in text and including code snippets
early_stages_tab_content = [
    dbc.Row([
        dbc.Col('Some block of text'),
        dbc.Col(html.Img(src='../assets/shocked_pikachu.jpg', className='img-resizing'), width=3)
    ])
]

data_collection_tab_content = [
    dbc.Row([
        dbc.Col(html.Img(src='../assets/shocked_pikachu.jpg', className='img-resizing'), width=3),
        dbc.Col('Some block of text'),
    ])
]

eda_tab_content = [
    dbc.Row([
        dbc.Col(html.Img(src='../assets/shocked_pikachu.jpg', className='img-resizing'), width=3),
        dbc.Col('Some block of text'),
    ])
]

results_tab_content = [
    dbc.Row([
        dbc.Col('Some block of text'),
        dbc.Col(html.Img(src='../assets/shocked_pikachu.jpg', className='img-resizing'), width=3)
    ])
]

our_journey_card_tabs = dbc.Card([
    dbc.CardHeader(
        dbc.Tabs([
            dbc.Tab(label='Early Stages', tab_id='our-journey-tab1', activeTabClassName='active-tab-our-journey', tabClassName='tab-our-journey', labelClassName='tab-label-our-journey',),
            dbc.Tab(label='Data Collection', tab_id='our-journey-tab2', activeTabClassName='active-tab-our-journey', tabClassName='tab-our-journey', labelClassName='tab-label-our-journey',),
            dbc.Tab(label='EDA (Exploratory Data Analysis)', tab_id='our-journey-tab3', activeTabClassName='active-tab-our-journey', tabClassName='tab-our-journey', labelClassName='tab-label-our-journey',),
            dbc.Tab(label='Results', tab_id='our-journey-tab4', activeTabClassName='active-tab-our-journey', tabClassName='tab-our-journey', labelClassName='tab-label-our-journey'),
        ],
            id='our-journey-card-tabs', card=True, active_tab='our-journey-tab1',
        ), className='primary-color'
    ),
    dbc.CardBody(html.Div(id='our-journey-card-content', className=''), className='secondary-color'),
])

our_journey_layout = html.Div([
    our_journey_card_tabs,
])