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

print(data.head())
# making new three column for order date
data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek
print(data.head())

# Monhly Sales Analysis
monthly_sales = data.groupby(['Order Month'])['Sales'].sum().reset_index()
print(monthly_sales.head())
fig = px.line(monthly_sales, x='Order Month', y='Sales', title='Monthly Sales Analysis')
#fig.show()

print(data.head())

# Sales by Category
sales_by_category = data.groupby(['Category'])['Sales'].sum().reset_index()
print(sales_by_category.head())
fig = px.pie(sales_by_category, names='Category', values='Sales', hole=0.5, color_discrete_sequence=px.colors.qualitative.Plotly)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales by Category', title_font=dict(size=20))
fig.show() 