import pandas as pd
from tqdm import trange
pd.options.mode.copy_on_write = True

file = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\resale-flat-prices1.xlsx'

df1 = pd.read_excel(file, engine='openpyxl')
# print(df1.shape)
# df11.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\test.xlsx')

df1['resale prices per square feet (psf)'] = df1['resale_price'] / df1['floor_area_sqm'] / 10.7639  # q1a
for i in trange(df1.shape[0]):
    split = df1.iloc[i]['remaining_lease'].split()
    if len(df1.iloc[i]['remaining_lease'])>9: #q12
        df1.loc[i,'remaining_lease_months'] = int(split[0])*12+int(split[2])
        # print(df1.iloc[i]['remaining_lease'])
        # print(df1.loc[i,'remaining_lease_months'])
        # print(df1.loc[i,'remaining_lease_months'])
    else:
        df1.loc[i, 'remaining_lease_months'] = int(split[0]) * 12
        # print(df1.iloc[i]['remaining_lease'])
        # print(df1.loc[i, 'remaining_lease_months'])
df2 = df1.drop_duplicates()
df2.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\resale-flat-prices_cleaned1.xlsx', index=False)