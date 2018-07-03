#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:29:51 2018

@author: rohithbharatha
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Hello Rohith'),
        
    html.Div(''' 
        Dash : a web application framework for python
        '''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x':[4,5,6], 'y':[3,4,9], 'type':'bar', 'name': 'Minneapolis'},
                {'x':[4,5,6], 'y':[2,1,1], 'type':'bar', 'name': 'Illinois'}
            ],
            'layout': {
                    'title':'Dash Data Visualization'
                    }
            }
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)