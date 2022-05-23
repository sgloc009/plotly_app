from dash import html, dcc, callback, Output, Input
from datetime import datetime

datepicker = { "id": "select-date", "element": dcc.DatePickerSingle(
                id="select-date",
                date=datetime.today().date()
            )}
def render(app, data_store_id, date_store_id):
    
    @app.callback(Output(date_store_id, 'data'),
        Input(datepicker["id"], 'date'))
    def change_data(date):
        print(date)
        return date

    return [datepicker]