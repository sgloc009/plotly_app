from dash import dcc, Output, Input, html, no_update
import dash_bootstrap_components as dbc
from .tabs_page import render as tabs_render

def render(app, data_store_id, date_store_id):
    tabs_el = tabs_render(app, data_store_id, date_store_id)

    admin_tab = dcc.Tab([html.Div([
        dbc.Button("Sign off Data", id='sign-off-btn', color='primary', className='mb-3', n_clicks=0),
        dbc.Toast(
            [html.P("The data has been signed off")],
            id='sign-off-toast',
            header='Sign-off Success',
            icon='primary',
            dismissable=True,
            is_open=False
        )
    ])], id='sign-off-btn-wrapper')

    children_value = [ "covid_cases", "admin" ]

    main_page_tabs_el = {
        'id': 'main-dash', 
        'element': html.Div([dcc.Tabs(children=[
                dcc.Tab(label="Covid Cases", value="covid_cases"),
                dcc.Tab(label="Admin", value="admin")], 
                id="main-dash")
            ])
        }
    output_main_el = {
            'id': 'main-page-tab-output',
            'element': html.Div(id='main-page-tab-output')
        }

    @app.callback(Output("sign-off-toast", "is_open"),
                [Input("sign-off-btn", "n_clicks")])
    def show_toast(n):
        if n == 0:
            return no_update
        return True

    @app.callback(Output(output_main_el['id'], 'children'),
        Input(main_page_tabs_el['id'], 'value'))
    def select_main_page(child):
        print(child)
        print(tabs_el)
        if(child==children_value[0]):
            print([*map(lambda x:x["element"], tabs_el)])
            return [*map(lambda x:x["element"], tabs_el)]
        elif(child==children_value[1]):
            return admin_tab

    return [ main_page_tabs_el, output_main_el ]