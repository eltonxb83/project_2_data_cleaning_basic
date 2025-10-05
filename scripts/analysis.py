import pandas as pd
import matplotlib.pyplot as plt
import os

#get to the folder where this scrip is located
script_dir = os.path.dirname(os.path.abspath(__file__))

#build full path to messy_sales_data.csv
csv_path = os.path.join(script_dir, 'messy_sales_data.csv')

#load the csv file
df = pd.read_csv(csv_path)

'''
#Inspecting Data
print(df.head())
print(df.info())
print(df.describe(include = "all"))
'''

#dropping duplicates
df = df.drop_duplicates()

#fixing column name
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

#fixing string format
columns_to_fixed = ['region','rep','item']
df[columns_to_fixed] = df[columns_to_fixed].apply(lambda col : col.str.strip().str.lower().str.replace(' ','_'))

#fixing date format
df['date'] = pd.to_datetime(df['date'],errors ='coerce')

'''
#check missing
print(df.isna().sum())
'''

#Fill or drop
df['region'] = df['region'].fillna('unknown')
df['rep'] = df['rep'].fillna('unknown')
df = df.dropna(subset = ['units','unit_cost'])

#verify 'total' information is correct
df['total_check'] = (df['units']*df['unit_cost']).round(2)
if not df['total'].round(2).equals(df['total_check']):
    df['total'] = df['total_check']
df.drop('total_check',axis =1, inplace = True)

#save cleaned data
df.to_csv('cleaned_sales.csv',index = False)

#Average unit cost per item
print(df.groupby('item')['unit_cost'].mean())

#total sales by month
df['month'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month')['total'].sum()
monthly_sales.to_csv('monthly_sales.csv', index = True)

#Visualize the Findings
#bar chart
df.groupby('region')['total'].sum().plot(kind='bar',title="Revenue by Region")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("revenue_by_region.png", dpi = 300)

#pie chart
item_counts = df['item'].value_counts()
plt.figure(figsize= (6,6))
plt.pie(
    item_counts,
    labels = item_counts.index,
    autopct = '%1.1f%%',
    startangle = 90,
    shadow = False,
    explode = [0.05]*len(item_counts)
)
plt.title('Item Distribution')
plt.axis('equal')
plt.tight_layout
plt.ylabel('')
plt.savefig("Item Distribution.png", dpi=300)


