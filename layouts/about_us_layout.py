import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# keep an eye on the facultyai dash bootstrap components repo for the update of the carousel component

# About us tab
about_us_layout = html.Div([
    dbc.Jumbotron([
        dbc.Container([
            html.H1("About Us Content", className="display-3"),
            html.P(
                "I'm thinking a simple carousel with a section for each person or even just an album/collection of cards briefly describing each of us",
                className="lead",
            ),
        ],
            fluid=True,
        )
    ],
        fluid=True,
    ),    
])