import pandas as pd
from numpy.ma.extras import average
from tqdm import trange

file1 = r'titanic.csv'

df = pd.read_csv(file1)
df = df[['PassengerId','Survived',	'Pclass','Sex',	'Age']]
df['Age'] = round(df.groupby('Pclass')['Age'].transform(
    lambda x: x.fillna(x.mean())

df.to_csv(r'titanic_cleaned.csv',index = False)

