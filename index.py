from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from layouts.overview_layout import overview_layout
from layouts.relief_funding_layout import relief_funding_layout
from layouts.demographics_layout import demographics_layout
from layouts.policy_mandates_layout import policy_mandates_layout
from layouts.our_journey_layout import our_journey_layout
from layouts.about_us_layout import about_us_layout
import callbacks

#Navbar components for all sections of the app
app_locations = [
    'Home',
    'The Problem',
    'Model',
    'Relief Funding',
    'Demographics',
    'Policy Mandates',
    'Our Journey',
    'About Us',
]

nav_dropdown_menu = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(app_locations[0], href='\\'),
        dbc.DropdownMenuItem(app_locations[1], href='\\overview'),
        dbc.DropdownMenuItem(app_locations[2], href='\\model'),
        dbc.DropdownMenuItem(app_locations[3], href='\\relief_funding'),
        dbc.DropdownMenuItem(app_locations[4], href='\\demographics'),
        dbc.DropdownMenuItem(app_locations[5], href='\\policy_mandates'),
        dbc.DropdownMenuItem(app_locations[6], href='\\our_journey'),
        dbc.DropdownMenuItem(app_locations[7], href='\\about_us'),
    ],
#     direction="left",
    right=True,
    nav=True,
    in_navbar=True,
    label="Navigate To...",
    id='dropdown-navbar',
    style={"text-transform": "none"},
)

button_github = dbc.Button(
    "Github Repo",
    outline=False,
#     color="primary",
    className='secondary-color',
    href="https://github.com/DS4A-Team79/COVID-Project",
    id="github-link",
    style={"text-transform": "none"},
)

# Navbar/header
header = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Img(
                    id="logo",
                    # put whatever image we want here, our group/project name, etc
                    # src=app.get_asset_url("dash-logo-new.png"),
                    height="30px",
                ),
                md="auto",
            ),
            dbc.Col([
#                 html.Div([
                dbc.NavbarBrand("Team 79 DS4A"),
#                     html.P("in progress"),
#                 ],
#                     id="app-title",
#                 )
            ],
                className="ml-2",
                md=True,
                align="center",
            ),
        ],
            no_gutters=True,
            align="center",
        ),
        dbc.Row([
            dbc.Col([
                dbc.NavbarBrand('{}', id='navbar-location')
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav([
                        dbc.NavItem(nav_dropdown_menu),
                        dbc.NavItem(button_github, className='invert-colors'),
                    ],
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
#                 md=2,
            ),
        ],
            justify="between",
            no_gutters=True,
            align="center",
        ),
    ],
        fluid=True,
    ),
    dark=True,
    color="#2260DD",
    sticky="top",
)

# for the index/home page, the first view
index_layout = html.Div([
    dbc.Jumbotron([
        dbc.Container([
            html.H1("Home Page", className="display-3"),
            html.P(
                "Whatever we want on the home page, if we want one at all. We can just talk about what our project is, but I'm thinking a home page isn't necessary",
                className="lead",
            ),
        ],
            fluid=True,
        )
    ],
        fluid=True,
    ),    
])


# updating the navbar location element
@app.callback(
    Output('navbar-location', 'children'),
    [Input('url', 'pathname')]
)
def display_navbar_page(pathname):
    if pathname == '/':
        return app_locations[0]
    if pathname == '/overview':
        return app_locations[1]
#     elif pathname == '\model':
#         return app_locations[2] 
    elif pathname == '/relief_funding':
        return app_locations[3]
    elif pathname == '/demographics':
        return app_locations[4]
    elif pathname == '/policy_mandates':
        return app_locations[5]
    elif pathname == '/our_journey':
        return app_locations[6]
    elif pathname == '/about_us':
        return app_locations[7]
    else:
        return 'IDK'

# main layout of the app, may change because of the dropdown menu
# don't modify this will nilly, implement any components first, then integrate it
# into this part
app.layout = html.Div([
    header,
    dcc.Location(id='url', refresh=False),
    dbc.Container(id='page-content', fluid=True, className='container-page-content'),
])

# Update the layout of the app
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)

def display_page(pathname):
    if pathname == '/':
        return index_layout
    if pathname == '/overview':
        return overview_layout
#     elif pathname == '\model':
#         return model_layout 
    elif pathname == '/relief_funding':
        return relief_funding_layout
    elif pathname == '/demographics':
        return demographics_layout
    elif pathname == '/policy_mandates':
        return policy_mandates_layout
    elif pathname == '/our_journey':
        return our_journey_layout
    elif pathname == '/about_us':
        return about_us_layout
    else:
        return '404'
    # You could also return a 404 "URL not found" page here
    
if __name__ == '__main__':
    app.run_server(debug=True)