#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[3]:


from sqlalchemy import create_engine


# In[4]:


def extract()-> dict:
    """ This API extracts data from
    http://universities.hipolabs.com
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).csv()
    return data


# In[ ]:







# In[ ]:







# In[ ]:







# # Framework
# 
# 

# In[8]:


get_ipython().system('pip install dash')




# In[1]:


import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go
import logging


# # LOG Format

# In[2]:


logging.basicConfig(filename='sample.txt',
                    filemode='a',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%y-%m-%d')
logging.warning('import warning for dcc')
logging.warning('import warning for html')


# In[2]:


app = dash.Dash()
app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='Dash Framework: A web application framework for Python')])


# In[3]:


df = pd.read_csv('mm8.csv')
df['Date']=pd.to_datetime(df['Date'])
logging.warning('date format is set to yyyy-mm-dd format')
def generate_table(dataframe, max_rows=10):
    return html.Table(
      # Header
      [html.Tr([html.Th(col) for col in dataframe.columns])] +
      # Body
      [html.Tr([
         html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
      ]) for i in range(min(len(dataframe), max_rows))]
   )
app = dash.Dash()
app.layout = html.Div(children=[
   html.H4(children='Material Management Data'),
   generate_table(df)
])
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:





# # Interactive data visualization

# In[5]:


app.layout = html.Div([
   dcc.Graph(
      id='Material Management',
      figure={
         'data': [
            go.Scatter(
               x=df[df['Equipment'] == i]['Target_TPH'],
               y=df[df['Equipment'] == i]['Actual TPH'],
               text=df[df['Equipment'] == i],
               mode='markers',
               opacity=0.7,
               marker={
                  'size': 15,
                  'line': {'width': 0.5, 'color': 'white'}
               },
               name=i
            ) for i in df.Equipment.unique()
         ],
         'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Expected TPH'},
            yaxis={'title': 'Actual TPH'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
         )
      }
   )
])

if __name__ == '__main__':
    app.run_server()


# In[ ]:





