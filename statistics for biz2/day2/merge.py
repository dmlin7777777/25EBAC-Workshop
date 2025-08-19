import pandas as pd
pd.options.mode.copy_on_write = True
file1 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\Table1_Sales_Order.xlsx'
file2 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\Table2_Region.xlsx'
file3 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\Table3_Product.xlsx'

df1 = pd.read_excel(file1,engine="openpyxl")
df2 = pd.read_excel(file2,engine="openpyxl")
df3 = pd.read_excel(file3,engine="openpyxl")

result1 = pd.merge(
    left = df1,
    right = df2,
    how = 'left',
    on = 'Order ID')

result2 = pd.merge(
    left = result1,
    right = df3,
    how = 'left',
    on = 'Product ID'
    )

result2['TOTAL'] = result2['Units'] * result2['Price']


result2.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\merge.xlsx',index = False)
