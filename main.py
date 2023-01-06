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
    dbc.NavbarSimple(children=[
        dbc.NavItem(dbc.NavLink("Sydney", href="#")),
        dbc.NavItem(dbc.NavLink("Melbourne", href="#")),
        dbc.NavItem(dbc.NavLink("The Author", href="https://github.com/pippo-sci"))
    ],
        brand="*",
        brand_href="#",
        color="#4791C2",
        dark=True),
    html.Div(id='Parallax Image', className="parallax container-fluid", style={'text-align': 'center'}, children=[
        html.H1('HausApp', className= "text"), 
        html.Div(className="text-center align-middle text2", children=[
            html.B(["Living in Australia for a couple of months, I found isn't easy to look for a flatshare", 
                    html.Br(),"for couples as most search websites are oriented to singles.", html.Br(),
                    "If you are in the same position, I hope this dashboard help you."]
                    )
                ])
    ]),
    
    dbc.Container(id='Control Bar', className= "color5 container-fluid", children= [
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id='select_mode',
                    options=[{'label':'Single', 'value': 'single'},{'label':'Couples', 'value': 'couples'}],
                    className='dropdownsty', multi=False, value='single',searchable=False, placeholder="Select a mode",
                )]),
            dbc.Col([
                dcc.Dropdown(id='select_neigh',options=[{'label':n, 'value': n} for n in df.neigh],
                    className='dropdownsty', multi=False, searchable=False, placeholder="Select a neighborhood"
                )]),
            dbc.Col([
                dcc.Dropdown(id='select_metric',options=[{'label':n, 'value': n} for n in df.columns],
                    className='dropdownsty', multi=False, searchable=False, placeholder="Select a metric"
                )]),
        ], style={'height': '60px'}, justify='around'),
        dcc.Graph(id='map',figure={})
        ], fluid=True),
    
    dbc.Container([
        dbc.Row([
            dbc.Col(className="color3", children=[
                html.H4("Distribution"),
                dcc.Graph(id='dist',figure={})
            ]),
            dbc.Col(className="color2",children=[
                html.H4("Loremi ipsum")
            ]),
            dbc.Col(className="color5",children=[
                html.H4("Cheapest neighborhoods"),
                dcc.Graph(id='cheap',figure={})
            ])
        ]),
        dbc.Row([
            dbc.Col(className="color4",children=[
                html.H4("Some title"),
                html.Div("Some text, long or not, this is a placeholder")
            ]),
            dbc.Col(className="color6",children=[
                html.H4(className="color3")
                #dcc.Graph()
            ]),
            dbc.Col(className="color1",children=[
                html.H4("Most expensive neighborhoods"),
                dcc.Graph(id='expensive',figure={})
            ])
        ])
    ], fluid=True),
    html.Div(id='output_container', children =[])
], fluid=True)


# ----

@app.callback(
    [
        Output(component_id='output_container', component_property='children'), 
        Output(component_id='map', component_property='figure'),
        Output(component_id='dist', component_property='figure'),
        Output(component_id='cheap', component_property='figure'),
        Output(component_id='expensive', component_property='figure')
        ],
    [Input(component_id='select_mode', component_property='value')]
)
def update_graph(selected_option):
    container = 'Selected mode is {}'.format(selected_option)

    tt = df.copy()

    fig_map = px.choropleth_mapbox(tt, geojson= tt.geometry, locations= tt.index, color=tt['mean'],
                           mapbox_style="stamen-toner", hover_name = 'neigh', hover_data=['count'], 
                           opacity = 0.6, center= {'lat':-37.8097305,'lon':144.9039946})

    fig_dist = px.histogram(tt, x='mean', labels={'mean':'price', 'count':'Frequency'}).update_traces(marker_color = '#4791C2').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})                    

    fig_cheap = px.bar(tt.sort_values('mean').head(5)[['neigh','mean']], x= 'neigh', y= 'mean', labels={'mean':'price', 'neigh':'neighborhood'}).update_traces(marker_color = '#f2c924').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig_expensive = px.bar(tt.sort_values('mean', ascending=False).head(5)[['neigh','mean']], x= 'neigh', y= 'mean', labels={'mean':'price', 'neigh':'neighborhood'}).update_traces(marker_color = '#0E3248').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    return container, fig_map, fig_dist, fig_cheap, fig_expensive


if __name__ == '__main__':
    app.run_server(debug=True) 