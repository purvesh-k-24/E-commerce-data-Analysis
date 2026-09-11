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
#fig.show() 

# Sales by Sub-Category
sales_by_subcategory = data.groupby(['Sub-Category'])['Sales'].sum().reset_index()
print(sales_by_subcategory.head())
fig = px.bar(sales_by_subcategory, x='Sub-Category', y='Sales', title='Sales by Sub-Category')
#fig.show()

# Monthly profit analysis
profit_by_month = data.groupby(['Order Month'])['Profit'].sum().reset_index()
print(profit_by_month.head())
fig = px.line(profit_by_month, x='Order Month', y='Profit', title='Monthly Profit Analysis')
#fig.show() 

# profit by category
profit_by_category = data.groupby(['Category'])['Profit'].sum().reset_index()
print(profit_by_category.head())
fig = px.pie(profit_by_category, names='Category', values='Profit', hole=0.5, color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
#fig.show()

# profit by sub-category
profit_by_subcategory = data.groupby(['Sub-Category'])['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory, x='Sub-Category', y='Profit', title='Profit by Sub-Category')
#fig.show()

# sales and profit customer segment
sales_profit_by_segment = data.groupby(['Segment'])[['Sales', 'Profit']].sum().reset_index()
color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'],
                        name='Sales',
                        marker_color=color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Profit'],   
                       name='Profit',
                         marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')
#fig.show()

# sales to profit ratio
sales_profit_segment = data.groupby(['Segment'])[['Sales', 'Profit']].sum().reset_index()
sales_profit_segment['Sales_to_Profit_Ratio'] = sales_profit_segment['Sales'] / sales_profit_segment['Profit']
print(sales_profit_segment[['Segment', 'Sales_to_Profit_Ratio']])
