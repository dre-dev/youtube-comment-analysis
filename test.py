import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children[html.H1('like counts'),
                              dcc.Graph(id='example',
                                       figure={
                                           'data':[
                                               {'x': [1,2,3], 'y':[5,6,7], 'type':'line', 'name':'boats'},
                                               {'x': [1,2,3], 'y':[8,2,3], 'type':'bar', 'name':'cars'},
                                           ],
                                           'layout': {
                                               'title':'Jokowi vs Prabowo'
                                           }
                                       })
                              ])

if __name__ == '__main__':
    app.run_server(debug=True)
