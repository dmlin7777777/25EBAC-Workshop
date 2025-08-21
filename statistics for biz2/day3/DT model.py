from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import trange

file1 = r'titanic_cleaned.csv'

df1 = pd.read_csv(file1)

features = ['Pclass','Sex',	'Age']

def gender1(gender):
    if gender == 'female':
        gendernew = 0
    else:
        gendernew = 1
    return gendernew

for i in trange(df1.shape[0]):
    gender = df1.iloc[i]['Sex']
    df1.loc[i, 'Sex'] = gender1(gender)

X = df1[features]
y = df1['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.2f}")

feature_names = X.columns.tolist()

if hasattr(y, 'cat.categories'):
    class_names = y.cat.categories.tolist()
else:
    class_names = [str(x) for x in y.unique()]

plt.figure(figsize=(30, 30))
plot_tree(
    clf,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    rounded=True,
    proportion=True,
    fontsize=10
)


plt.show()
