import sqlite3
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output, callback

# 引入CSS樣式表，易於開發Dash的互動式網頁，是Plotly的官方開源庫
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

connection = sqlite3.connect("data/gapminder.db")
df = pd.read_sql("SELECT * FROM plotting;", con=connection)
connection.close()

# 設計layout
app.layout = html.Div([
    html.H2(children= "Gapminder Clone 1800-2023", 
            style={'padding': '10px 0px 0px 5px'}
    ),
    html.Div([
        dcc.Dropdown( #下拉選單
        df['continent'].unique(), # options
        'asia', # value (which one is selected by default)
        id='dropdown-continent', 
    )], style={'fontSize': '20px', 'width': '25%', 'padding': '10px 15px 20px 5px'} # 上 右 下 左
    ),
    html.Div([
        dcc.Graph( #散佈圖
            id='graph-with-hover-interaction', 
            clickData={'points': [{'customdata': 'Taiwan'}]} # 預設選擇的國家
    )], style={'width': '49%', 'display': 'inline-block',  'verticalAlign': 'top', 'padding': '5px'}
    ),
    html.Div([ #折線圖
        dcc.Graph(id='lex-of-country'), 
        dcc.Graph(id='gdp-of-country')

    ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '5px'}
    ),
    html.Div([
        dcc.Slider( #滑桿
            df['dt_year'].min(),
            df['dt_year'].max(),
            # step=None,
            value=df['dt_year'].max(),
            marks={
                str(year): {
                    'label': str(year),
                    'style': {'fontSize': '15px'}
                } for i, year in enumerate(df['dt_year'].unique()) if i % 20 == 0
            },
            id='year-slider'
    )], style={'padding': '20px 0px 0px 5px'} # 上 右 下 左
    )
])

# 更新散佈圖
@callback(
    Output('graph-with-hover-interaction', 'figure'), #散佈圖
    Input('dropdown-continent', 'value'), #下拉選單
    Input('year-slider', 'value')) #滑桿
def update_graph(continent_value, year_value):
    dff = df[(df['dt_year'] == year_value) & (df['continent'] == continent_value)]
    fig = px.scatter(
        dff, x="gdp_per_capita", y="life_expectancy",
        size="population", color="country_name", 
        hover_name="country_name", size_max=100, 
        range_x=[500, 120000], range_y=[20, 100], log_x=True
    )
    for i, trace_name in enumerate(fig.data):
        fig.data[i].customdata = dff[dff["country_name"] == trace_name.name]["country_name"]
    fig.update_layout(margin={'l': 0, 'b': 55, 't': 50, 'r': 20}, 
                      hovermode='closest', 
                      showlegend=False, 
                      title=f'<span style="font-size:20px"><b>Gapminder Data for {continent_value.title()} in {year_value}</b></span>')
    return fig

# 畫折線圖-gdp_per_capita
def create_gdp_graph(dff, title):
    fig = px.scatter(dff, x='dt_year', y='gdp_per_capita',)
    fig.update_traces(mode='lines+markers') 
    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=title)
    fig.update_layout(height=225, margin={'l': 0, 'b': 0, 'r': 10, 't': 20})
    return fig
# 更新折線圖-gdp_per_capita
@callback(
    Output('gdp-of-country', 'figure'), #折線圖
    Input('graph-with-hover-interaction', 'clickData')) #散佈圖
def update_gdp(clickData):
    if clickData is None:
        raise dash.exceptions.PreventUpdate  # 不做任何更新
    country = clickData['points'][0]['customdata']
    dff = df[df['country_name'] == country]
    title = f' <span style="font-size:20px"><b>GDP for {country} (1800-2023)</b></span>'
    return create_gdp_graph(dff, title)


# 畫折線圖-life_expectancy
def create_lex_graph(dff, title):
    fig = px.scatter(dff, x='dt_year', y='life_expectancy',)
    fig.update_traces(mode='lines+markers')
    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=title)
    fig.update_layout(height=225, margin={'l': 0, 'b': 50, 'r': 10, 't': 20})
    return fig
# 更新折線圖-life_expectancy
@callback(
    Output('lex-of-country', 'figure'), #折線圖
    Input('graph-with-hover-interaction', 'clickData')) #散佈圖
def update_gdp(clickData):
    if clickData is None:
        raise dash.exceptions.PreventUpdate  # 不做任何更新
    country = clickData['points'][0]['customdata']
    dff = df[df['country_name'] == country]
    title = f' <span style="font-size:20px"><b>Life Expectancy for {country} (1800-2023)</b></span>'
    return create_lex_graph(dff, title)

if __name__ == '__main__':
    app.run(debug=True)