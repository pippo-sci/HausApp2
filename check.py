import pandas as pd
import dash
import dash_core_components as dcc
import dash_hatml_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

app = dash.Dash(__name__)

df = pd.read_csv('melb.csv')

app.layout = html.Div([
    html.H1('HausApp', style= {'text-align':'center'}),
    dcc.Dropdown(id='select_year',
     options=[{'label':'', 'value': }],
     multi=False,
     value=,
     style={'width':'40%'}),
    html.Div(id='output_container', children =[]),
    html.Br(),
    htmldcc.Graph(id='map',figure={})


])


# ----

@app.callback(
    [Output(component_id='output-container', component_property='children'), Output(component_id='map', component_property='figure')],
    [Input(component_id='select_year', component_property='value')]
)

def update_graph(selected_option):
    container = 'Selected year is {}'.format(selected_option)

    dff = df.copy()

    fig = px.choropleth

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True) 