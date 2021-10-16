import csv
import pandas as pd
import plotly.figure_factory as pff

df=pd.read_csv('height_weight.csv')
weight=df['Weight'].tolist()

graph=pff.create_distplot([weight],["Weight"],show_hist=False)
graph.show()