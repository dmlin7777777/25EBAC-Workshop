import pandas as pd
from numpy.ma.extras import average
from tqdm import trange

file1 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 3\titanic.csv'

df = pd.read_csv(file1)
df = df[['PassengerId','Survived',	'Pclass','Sex',	'Age']]
# def gender1(gender):
#     if gender == 'female':
#         gendernew = 0
#     else:
#         gendernew = 1
#     return gendernew

df['Age'] = round(df.groupby('Pclass')['Age'].transform(
    lambda x: x.fillna(x.mean())
))

# for i in trange(df.shape[0]):
#     gender = df.iloc[i]['Sex']
#     df.loc[i, 'Sex'] = gender1(gender)



# df = df.dropna(subset='prod')
# df = df[df['age']<=116]
df = df.drop_duplicates()
df.to_csv(r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 3\titanic_cleaned.csv',index = False)