import pandas as pd
import plotly.express as px

df = pd.read_csv('day1(output).csv')

fig = px.line(df, x = 'Time', y = 'CGM', title='Day 1 (OUTPUT)')
fig.show()