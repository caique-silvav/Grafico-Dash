from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div(
    className="main-container",
    children=[
        html.H1("População Mundial ao Longo do Tempo", className="app-title"),
        html.Div(
            dcc.Dropdown(
                id='dropdown-selection',
                options=[{'label': country, 'value': country} for country in df.country.unique()],
                value='Canada',
                clearable=False,
                className="country-dropdown",
                style={'width': '100%', 'maxWidth': '550px'}
            ),
            className="controls"
        ),
        dcc.Graph(id='graph-content', config={'displayModeBar': False}),
        html.Footer("© 2025 • Visualização interativa com Dash & Plotly", className="footer")
    ]
)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    fig = px.line(
        dff, x='year', y='pop',
        title=f"Evolução da População: {value}",
        labels={'pop': 'População', 'year': 'Ano'},
        line_shape='spline'
    )
    fig.update_layout(
        font_family="Segoe UI, system-ui, sans-serif",
        title_font_size=20,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.2)'),
        hovermode="x unified"
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)