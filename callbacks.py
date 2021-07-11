from dash.dependencies import Input, Output, State

from layouts.our_journey_layout import early_stages_tab_content, data_collection_tab_content, eda_tab_content, results_tab_content

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
    if active_tab == 'our-journey-tab1':
        return early_stages_tab_content
    if active_tab == 'our-journey-tab2':
        return data_collection_tab_content
    if active_tab == 'our-journey-tab3':
        return eda_tab_content
    if active_tab == 'our-journey-tab4':
        return results_tab_content
    else:
        return 'Error with loading content!'
    
app.callback(
    Output('our-journey-card-content', 'children'),
    [Input('our-journey-card-tabs', 'active_tab')]
)(tab_content)

# modal callbacks for geospatial map and visualizations in the visualizations view (one callback for each modal)
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

app.callback(
    Output('modal-visualization1', 'is_open'),
    [Input('open-modal-visualization1', 'n_clicks'), 
    Input('close-modal-visualization1', 'n_clicks')],
    [State('modal-visualization1', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-visualization2', 'is_open'),
    [Input('open-modal-visualization2', 'n_clicks'), 
    Input('close-modal-visualization2', 'n_clicks')],
    [State('modal-visualization2', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-visualization3', 'is_open'),
    [Input('open-modal-visualization3', 'n_clicks'), 
    Input('close-modal-visualization3', 'n_clicks')],
    [State('modal-visualization3', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-visualization4', 'is_open'),
    [Input('open-modal-visualization4', 'n_clicks'), 
    Input('close-modal-visualization4', 'n_clicks')],
    [State('modal-visualization4', 'is_open')],
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