import pandas as pd
pd.options.mode.copy_on_write = True
file1 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\injuries_log_10K_cleaned.xlsx'
file2 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\injuries_descriptions_10K.csv'
file3 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\injuries_products.csv'

df1 = pd.read_excel(file1,engine="openpyxl")
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

result1 = pd.merge(
    left = df1,
    right = df2,
    how = 'left',
    on = 'case_num')

result2 = pd.merge(
    left = result1,
    right = df3,
    how = 'left',
    left_on = 'prod',
    right_on = 'code')

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

result2['month_num'] = result2['trmt_date'].map(month_map)


df_sorted = result2.sort_values(['month_num', 'age'], ascending=[True, True])
df_sorted = df_sorted.drop('month_num', axis=1)

fingerdf = df_sorted[(df_sorted['body_part'] == 'Finger')]
fracturedf = df_sorted[(df_sorted['diag'] == 'Fracture')]

df_sorted.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\Combined_dataset2.xlsx',index = False)
fingerdf.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\Combined_dataset2_finger.xlsx',index = False)
fracturedf.to_excel(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 1\PM Session\Combined_dataset2_fracture.xlsx',index = False)
