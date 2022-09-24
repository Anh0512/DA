import pandas as pd
import numpy as np
df = pd.read_csv('D:\jupyter\OnlineRetail.csv')

#Tổng số lượng đơn hàng bán ra, tổng doanh thu
#df['tong doanh thu'] = np.nan

df['tong doanh thu'] = df['Quantity'] * df['UnitPrice']
df_quantity = df.groupby(by='Description')['Description','Quantity','tong doanh thu'].sum().sort_values(by='tong doanh thu',ascending = False)
#print(df_quantity)

#Top 10 mặt hàng có số lượng bán ra lớn nhất
df_soluong = df.groupby(by='Description')['Description','Quantity'].sum().sort_values(by='Quantity',ascending=False)
#print(df_soluong.head(10))

#Top 10 mặt hàng có doanh thu lớn nhất
df_doanhthu = df.groupby(by='Description')['Description','tong doanh thu'].sum().sort_values(by='tong doanh thu',ascending=False)
#print(df_doanhthu.head(10))