from dash.dependencies import Input, Output, State

from app import app

# add callback for 
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'value')])

# def display_page(pathname):
#     return html.Div([
#         html.H3('You are on page {}'.format(pathname))
#     ])

# callback for location shown in navbar
# app.callback(
#     Output('navbar-display-location', 'children'),
#     Input('app')
# )

# callback for card tabs in our journey page
def tab_content(active_tab):
    return 'Current tab: {}'.format(active_tab)
app.callback(
    Output('our-journey-card-content', 'children'),
    [Input('our-journey-card-tabs', 'active_tab')]
)(tab_content)

# modal callback for geospatial map for visualizations view
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

app.callback(
    Output('modal-geo', 'is_open'),
    [Input('open-modal-geo', 'n_clicks'), 
    Input('close-modal-geo', 'n_clicks')],
    [State('modal-geo', 'is_open')],
)(toggle_modal)

# add callback for toggling the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)(toggle_navbar_collapse)