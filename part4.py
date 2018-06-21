# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.tools as pt
import plotly.graph_objs as go
pt.set_credentials_file(username='akshat10', api_key='kC0RtOshT2D3LZhzWsQn')
# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
import csv




x=[]
y=[]
f = open("noun_data.csv", "r")

reader = csv.reader(f)
i = 0
for line in reader:
    if i > 0:
        x.append(line[0])
        y.append(line[1])
    i+=1




trace = go.Bar(x=x, y=y)
data = [trace]
layout = go.Layout(title='Nouns data', width=800, height=640)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='a-simple-plot.png')
