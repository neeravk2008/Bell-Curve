import csv
import pandas as pd
import plotly.figure_factory as pff

df=pd.read_csv('height_weight.csv')
height=df['Height'].tolist()

graph=pff.create_distplot([height],["Height"],show_hist=False)
graph.show()