from dash.dependencies import ClientsideFunction, Input, Output, State

from layouts.our_journey_layout import early_stages_tab_content, data_collection_tab_content, eda_tab_content, results_tab_content
from layouts.relief_funding_layout import per_state_fig_2020, per_capita_fig_2020, per_state_fig_2021, per_capita_fig_2021

from main_dash import app

# callbacks for relief funding dash visualizations
def update_relief_funding(search_value):
    if not search_value == 'rps':
        return 
    return [o for o in options if search_value in o["label"]]
app.callback(
    Output("dropdown-2020", "options"),
    [Input("dropdown-2020", "search_value")],
)(update_relief_funding)



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

# modal callbacks for geospatial maps and visualizations in the visualizations view (one callback for each modal)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# for geo map modals showing the extra info we want it to show
app.callback(
    Output('modal-overview-geomap', 'is_open'),
    [Input('open-modal-overview-geomap', 'n_clicks'), 
    Input('close-modal-overview-geomap', 'n_clicks')],
    [State('modal-overview-geomap', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-relief-geomap', 'is_open'),
    [Input('open-modal-relief-geomap', 'n_clicks'), 
    Input('close-modal-relief-geomap', 'n_clicks')],
    [State('modal-relief-geomap', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-demographics-geomap', 'is_open'),
    [Input('open-modal-demographics-geomap', 'n_clicks'), 
    Input('close-modal-demographics-geomap', 'n_clicks')],
    [State('modal-demographics-geomap', 'is_open')],
)(toggle_modal)

app.callback(
    Output('modal-policy-geomap', 'is_open'),
    [Input('open-modal-policy-geomap', 'n_clicks'), 
    Input('close-modal-policy-geomap', 'n_clicks')],
    [State('modal-policy-geomap', 'is_open')],
)(toggle_modal)

# for other visualizations
# for the spinners in each layout
# def load_tableau_maps(pathname):
#     if pathname == '/policy_mandates':
#         app.clientside_callback(
#             ClientsideFunction(
#                 namespace='clientsidePolicyMandates',
#                 function_name='initPolicyMandatesMap',
#             ),
#             Output('tableauPolicyMandatesMap', 'children'),
#             [Input('url', 'pathname')]
#         )
#     else:
#         return 'idk';
    
# app.callback(
#     Output('loadingTableauPolicyMandatesMap', 'children'),
#     Input('url', 'pathname')
# )(load_tableau_maps)

# clientside callbacks responsible for calling the (java)scripts loading the tableau maps
# i chose to use clientside callbacks because everytime we change the view, we need different visualizations to load, causing a lot of overhead
app.clientside_callback(
    ClientsideFunction(
        namespace='clientsidePolicyMandates',
        function_name='initPolicyMandatesMap',
    ),
    Output('tableauPolicyMandatesMap', 'children'),
    [Input('url', 'pathname')]
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientsideReliefFunding',
        function_name='initReliefFundingMap',
    ),
    Output('tableauReliefFundingMap', 'children'),
    [Input('url', 'pathname')]
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientsideDemographics',
        function_name='initDemographicsMap',
    ),
    Output('tableauDemographicsMap', 'children'),
    [Input('url', 'pathname')]
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientsideOverview',
        function_name='initOverviewMap',
    ),
    Output('tableauOverviewMap', 'children'),
    [Input('url', 'pathname')]
)  

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