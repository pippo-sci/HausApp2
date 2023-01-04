import pandas as pd
import geopandas as gpd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

#import plotly.graph_objs as go

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags = [{'name':'viewport', 'content': 'width=device-width'}])

df = gpd.read_file('melb.geojson')

app.layout = dbc.Container([
    dbc.NavbarSimple(className= "color4", children=[], brand="Initial",
        brand_href="#",
        color="primary",
        dark=True),
    html.Div(className="parallax container-fluid", children=[
        html.H1('HausApp', className= "text-center align-middle text"), 
        html.Div(className="text-center align-middle text2", children=[
            html.P("Living in Sydney for a couple of months, I found isn't easy look a flatshare"),
            html.P("for couples as most search websites are oriented to singles."),
            html.P("I hope this dashboard help you...despite is still a work in process")])
    ]),
    html.Div(className="color5", children=[
        html.Div(className= "row container-fluid align-middle clearfix", children= [
            dcc.Dropdown(id='select_year',
                options=[{'label':'1', 'value': 1},{'label':'2', 'value': 2}],
                multi=False,
                value=1,
                style={'width':'40%'})
        ])]),

    dcc.Graph(id='map',figure={}),

    dbc.Container([
        dbc.Row([
            dbc.Col(className="color3", children=[
                html.Div(""),
                dcc.Graph()
            ]),
            dbc.Col(className="color4",children=[
                html.Div(""),
                dcc.Graph()
            ]),
            dbc.Col(className="color2",children=[
                html.Div("Cheapest neighborhoods"),
                dcc.Graph()
            ])
        ]),
        dbc.Row([
            dbc.Col(className="color2",children=[
                html.Div(""),
                dcc.Graph()
            ]),
            dbc.Col(className="color1",children=[
                html.Div(className="color3",children=""),
                dcc.Graph()
            ]),
            dbc.Col(className="color3",children=[
                html.Div("Most expensive neighborhoods"),
                dcc.Graph()
            ])
        ])
    ]),
    html.Div(id='output_container', children =[])
])


# ----

@app.callback(
    [Output(component_id='output_container', component_property='children'), Output(component_id='map', component_property='figure')],
    [Input(component_id='select_year', component_property='value')]
)

def update_graph(selected_option):
    container = 'Selected year is {}'.format(selected_option)

    tt = df.copy()

    fig = px.choropleth_mapbox(tt, geojson= tt.geometry, locations= tt.index, color=tt['mean'],
                           mapbox_style="stamen-toner", hover_name = 'neigh', hover_data=['count'], opacity = 0.6, center= {'lat':-37.8097305,'lon':144.9039946})

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True) 