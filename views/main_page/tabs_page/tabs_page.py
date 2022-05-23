from dash import dcc, html, dash_table
from dash.dependencies import Output, Input
from datasources import get_data
import pandas as pd


india_tab = dcc.Tab(label="India", value="india_tab")
us_tab = dcc.Tab(label="US", value="us_tab")

children_values = ["india_tab", "us_tab"]
children = [india_tab, us_tab]
tabs = {"id": "tabs", "element": dcc.Tabs(id="tabs", value=children_values[0], children=children)}
output_charts = {"id": "charts", "element": html.Div(id="charts", className="wrapper")}

india_tab_content = {"id": "input_tab_content", "element": html.Div([
                        html.H3("India Cases"),
                        dash_table.DataTable(columns=[{"name": i, "id": i} for i in get_data().columns if i!='country'], id='india-datatable')
                    ])}
us_tab_content = {"id": "us_tab_content", "element": html.Div([
                    html.H3("US Cases"),
                    dash_table.DataTable(columns=[{"name": i, "id": i} for i in get_data().columns if i!='country'], id='us-datatable')
                ])}


def render(app, data_store_id, date_store_id):
    @app.callback(Output(output_charts["id"], "children"),
                    Input(tabs["id"], "value"))
    def render_content(tab):
        if(tab == children_values[0]):
            return india_tab_content["element"]
        elif(tab == children_values[1]):
            return us_tab_content["element"]
    @app.callback(Output('india-datatable', 'data'),
        Input(data_store_id, 'data'))
    def update_data(data):
        print(data)
        data = pd.DataFrame(data)
        data = data[data["country"]=="India"]
        print(data)
        return data.to_dict(orient='records')
    
    @app.callback(Output('us-datatable', 'data'),
        Input(data_store_id, 'data'))
    def update_data(data):
        data = pd.DataFrame(data)
        data = data[data["country"]=="US"]
        print(data)
        return data.to_dict(orient='records')

    tab_wrapper = {"element": html.Div(tabs['element'], className='wrapper')}

    return [tab_wrapper, output_charts]