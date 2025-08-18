import pandas as pd
import openpyxl
import re
from tqdm import trange
pd.options.mode.copy_on_write = True
file = r'injuries_log_10K.xlsx'
df = pd.read_excel(file,engine="openpyxl")

def ageband(age):
    if age<21:
        band = 'Minor'
    elif age>=65:
        band = 'Senior'
    else:
        band = 'Adult'
    return band

def gender1(gender):
    gender = re.sub(r'\s+', '', gender)
    if gender == 'F':
        gendernew = 'Female'
    elif gender == 'M':
        gendernew = 'Male'
    else:
        gendernew = gender
    return gendernew

for i in trange(df.shape[0]):
    age = df.iloc[i]['age']
    df.loc[i, 'age'] = round(age)

    date = df.iloc[i]['trmt_date']
    df.loc[i, 'trmt_date'] = date.strftime("%B")

    gender = df.iloc[i]['gender']
    df.loc[i, 'gender'] = gender1(gender)

    id = df.iloc[i]['ID']
    df.loc[i,'ID'] = id[:2]+'*****'+id[6:]

    df.loc[i,'ageband'] = ageband(round(age))

df = df.dropna(subset='prod')
df = df[df['age']<=116]

df.to_excel(r'injuries_log_10K_cleaned.xlsx',index=False)
