import random
import plotly.express as px
import plotly.figure_factory as pff

#print(d1)

result=[]
count=[]

for i in range(0,100):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    sum=d1+d2
    result.append(sum)
    count.append(i)
#print(result)

graph=pff.create_distplot([result],["Result"],show_hist=False)
graph.show()