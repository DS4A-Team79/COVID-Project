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

# experiment with dbc.Markdown, should make it easier to have text, images, etc all in one card body

our_journey_card_tabs = dbc.Card([
    dbc.CardHeader(
        dbc.Tabs([
            dbc.Tab(label='Early Stages', tab_id='our-journey-tab1'),
            dbc.Tab(label='Data Collection', tab_id='our-journey-tab2'),
            dbc.Tab(label='EDA (Exploratory Data Analysis)', tab_id='our-journey-tab3'),
            dbc.Tab(label='Results', tab_id='our-journey-tab4'),
        ],
            id='our-journey-card-tabs', card=True, active_tab='our-journey-tab1'
        )
    ),
    dbc.CardBody(html.P(id='our-journey-card-content', className='')),
])

our_journey_layout = html.Div([
    our_journey_card_tabs,
    
])


