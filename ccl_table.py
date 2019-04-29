import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from get_ccl1_data import get_ccl1_data_from_excel



df=get_ccl1_data_from_excel("ccl.xlsx")
def generate_table(dataframe, max_rows=1000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='CCL Table'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)