import plotly.express as px
import pandas as pd

data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Temperature': [28, 30, 29, 32, 31]
}

df = pd.DataFrame(data)

fig = px.line(df, x='Day', y='Temperature',
              title='Temperature Line Plot', markers=True)

fig.show()