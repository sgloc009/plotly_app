from dash import Dash, html, dcc
from datasources import get_data
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
from utilities import utilities
import views


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
data_store_id = "data-store"
date_store_id = "date-value"


app.layout = html.Div([*map(lambda x:x['element'], views.render(app, data_store_id, date_store_id)),
                        dcc.Store(id=date_store_id), 
                        dcc.Store(id=data_store_id)
                    ], className='wrapper')
utilities(app, data_store_id, date_store_id)

if(__name__ == '__main__'):
    app.run_server(debug=True)