import pandas as pd
import plotly.express as px
import numpy as np
df= pd.read_csv("data.csv")
score=df["TOEFL Score"].tolist()
chance= df["Chance of Admit "].tolist()
fig= px.scatter(x=score, y=chance)
score_array=np.array(score)
chance_array=np.array(chance)
m,c=np.polyfit(score_array,chance_array,1)
y=[]
for x in score_array:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=score_array, y=chance_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(score_array), x1= max(score_array)
    )
])
x=250
y=m*x+c
print(f"Chance of Admit for score{x}is{y}")
fig.show()
