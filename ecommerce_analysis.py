import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors  
pio.templates.default = "plotly_white"

data = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
print(data.head())

data.describe()
data.info()

#converting date column to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])
data.info()

