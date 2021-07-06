from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from layouts.visualizations_layout import visualization_layout
from layouts.our_journey_layout import our_journey_layout
from layouts.about_us_layout import about_us_layout
import callbacks

#Navbar components
app_locations = [
    'Visualizations',
    'Model',
    'Our Journey',
    'About Us',
]

nav_dropdown_menu = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(app_locations[0], href='\\visualizations'),
        dbc.DropdownMenuItem(app_locations[1], href='\\models'),
        dbc.DropdownMenuItem(app_locations[2], href='\\our_journey'),
        dbc.DropdownMenuItem(app_locations[3], href='\\about_us'),
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
    outline=True,
    color="primary",
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
                        dbc.NavItem(button_github),
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
    color="dark",
    sticky="top",
)

# updating the navbar location element
@app.callback(
    Output('navbar-location', 'children'),
    [Input('url', 'pathname')]
)
def display_navbar_page(pathname):
    if pathname == '/visualizations':
        return app_locations[0]
#     elif pathname == '\model':
#         return model_layout
    elif pathname == '/our_journey':
        return app_locations[2]
    elif pathname == '/about_us':
        return app_locations[3]
    else:
        return 'IDK'

# main layout of the app, may change because of the dropdown menu
# don't modify this will nilly, implement any components first, then integrate it
# through this function
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
    if pathname == '/visualizations':
        return visualization_layout
#     elif pathname == '\model':
#         return model_layout
    elif pathname == '/our_journey':
        return our_journey_layout
    elif pathname == '/about_us':
        return about_us_layout
    else:
        return '404'
    # You could also return a 404 "URL not found" page here
    
if __name__ == '__main__':
    app.run_server(debug=True)