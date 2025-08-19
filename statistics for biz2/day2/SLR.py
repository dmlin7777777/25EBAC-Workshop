import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

file = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 2\SFB Day 2 PM _Correlation and Simple Linear Regression v31.xlsx'
df = pd.read_excel(file, engine='openpyxl',sheet_name='FitElite_Gym')

y = df['Yearly Additional Spending (SGD)']
X = df['Yearly Gym Visits']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
residuals = model.resid
bp_test = het_breuschpagan(residuals,model.model.exog)
dw = durbin_watson(residuals)
print(model.summary())
print(bp_test)
print(dw)


# plt.scatter(X, y, color='blue', label='原始数据')
# plt.plot(X, model.predict(), color='red', label='回归线')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.title('SLR')
# plt.legend()
# plt.show()
