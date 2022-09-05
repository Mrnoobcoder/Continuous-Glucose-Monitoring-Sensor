import pandas as pd
import plotly.express as px

df = pd.read_csv('day1(input).csv')

fig = px.line(df, x = 'Time', y = 'BG', title='Day 1 (INPUT)')
fig.show() 