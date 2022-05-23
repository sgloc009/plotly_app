from .tabs_page import tabs, html, render as tabs_render
from .datepicker import render as datepicker_render
from dash import Output, Input, html



def render(app, data_store_id, date_store_id):
    datepicker_elements = datepicker_render(app, data_store_id, date_store_id)
    tabs_elements = tabs_render(app, data_store_id, date_store_id)
    return [{'id':'datepicker-label', 'element': html.Span("Pick a date:", 'datepicker-label')}, {'id': '', 'element': html.Br()}, *datepicker_elements, *tabs_elements]
    


