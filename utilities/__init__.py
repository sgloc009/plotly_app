"""
    Created by: Shubham Ganguly
    This module contains basic functionalities of the application.
"""

from dash import Output, Input
from datasources import get_data
from datetime import datetime

def utilities(app, data_store_id, date_store_id):
    @app.callback(Output(data_store_id, 'data'),
        Input(date_store_id, 'data'))
    def update_data(date):
        if(date):
            data = get_data()
            print(data)
            print(datetime.strptime(date, '%Y-%m-%d'))
            print(data['Date'].dtype)
            print(data[data['Date']==date].head())
            return data[data['Date']==date].to_dict(orient='records')
        else:
            return data.to_dict(orient='records')
