# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc

# # from app import app
# # from dash.dependencies import Input, Output, State

# geospatial_map_help = dbc.Modal([
#     dbc.ModalHeader([
#         'Info',
#         dbc.Button(
#             'Close',
#             id='close-geospatial-scroll',
#             className='sm-auto',
#             n_clicks=0,
#         ),
#     ]),
#     dbc.ModalBody([
#         html.P('Some Text'),
#         html.P('Some more text'),
#     ]),
#     dbc.ModalFooter("Some other text here"),
# ],
#     id='modal-geospatial-scroll',
#     scrollable=True,
#     is_open=False,
# )

# geospatial_map = dbc.Container([
#     html.H4('Geospatial Map'),
#     dbc.Button('?', id='open-geospatial-scroll', n_clicks=0),
#     geospatial_map_help,
# ])

# # Visualization Layout
# visualization_layout = html.Div([
#     dbc.Jumbotron([
#         dbc.Container([
#             html.H1("Visualization Content", className="display-3"),
#             html.P(
#                 "The contents here will be determined by the option selected in the navbar",
#                 className="lead",
#             ),
#         ],
#             fluid=True,
#         )
#     ],
#         fluid=True,
#     ),
# #     html.Div(id='visualization_display'),
#     geospatial_map,
# ])




# # Our Journey tab
# our_journey_layout = html.Div([
#     dbc.Jumbotron([
#         dbc.Container([
#             html.H1("Our Journey Content", className="display-3"),
#             html.P(
#                 "We can explain here what we did throughout the course of this project",
#                 className="lead",
#             ),
#         ],
#             fluid=True,
#         )
#     ],
#         fluid=True,
#     ),    
# ])


# # About us tab
# about_us_layout = html.Div([
#     dbc.Jumbotron([
#         dbc.Container([
#             html.H1("About Us Content", className="display-3"),
#             html.P(
#                 "I'm thinking a simple carousel with a section for each person or even just an album/collection of cards briefly describing each of us",
#                 className="lead",
#             ),
#         ],
#             fluid=True,
#         )
#     ],
#         fluid=True,
#     ),    
# ])

# # def toggle_modal(n1, n2, is_open):
# #     if n1 or n2:
# #         return not is_open
# #     return is_open

# # app.callback(
# #     Output('modal-geospatial-scroll', 'is_open'),
# #     [Input('open-geospatial-scroll', 'n_clicks'), Input('close-geospatial-scroll', 'n_clicks')],
# #     [State('modal-geospatial-scroll', 'is_open')],
# # )(toggle_modal)


# # html.Img(
# #             src='https://dash-gallery.plotly.host/dash-world-cell-towers/assets/times-circle-solid.svg',
# #             alt='Exit Icon',
# #         ),

# # html.Img(
# #             src='https://dash-gallery.plotly.host/dash-world-cell-towers/assets/question-circle-solid.svg',
# #             alt='Exit Icon',
# #         ),