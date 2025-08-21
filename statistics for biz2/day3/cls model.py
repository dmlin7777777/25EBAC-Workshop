import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tqdm import trange

file1 = r'C:\Users\12932\Desktop\nus\statistics for biz2\Day 3\titanic_cleaned.csv'
df = pd.read_csv(file1)

features = ['Pclass','Sex',	'Age']

def gender1(gender):
    if gender == 'female':
        gendernew = 0
    else:
        gendernew = 1
    return gendernew

for i in trange(df.shape[0]):
    gender = df.iloc[i]['Sex']
    df.loc[i, 'Sex'] = gender1(gender)

X = df[features]
X_scaled = StandardScaler().fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)


# def manual_pairplot(df, features, cluster_col):
#     n_features = len(features)
#     fig, axes = plt.subplots(n_features, n_features, figsize=(15, 15))
#
#     unique_clusters = df[cluster_col].unique()
#     colors = plt.cm.viridis(np.linspace(0, 1, len(unique_clusters)))
#
#     for i, feat_x in enumerate(features):
#         for j, feat_y in enumerate(features):
#             ax = axes[i, j]
#
#             if i == j:
#                 for k, cluster in enumerate(unique_clusters):
#                     cluster_data = df[df[cluster_col] == cluster]
#                     sns.kdeplot(data=cluster_data[feat_x], ax=ax,
#                                 color=colors[k], label=f'Cluster {cluster}')
#                 ax.set_ylabel('Density')
#             else:
#                 for k, cluster in enumerate(unique_clusters):
#                     cluster_data = df[df[cluster_col] == cluster]
#                     ax.scatter(cluster_data[feat_x], cluster_data[feat_y],
#                                color=colors[k], alpha=0.7, s=30, label=f'Cluster {cluster}')
#
#             if i == n_features - 1:
#                 ax.set_xlabel(feat_y)
#             if j == 0:
#                 ax.set_ylabel(feat_x)
#     handles, labels = axes[0, 0].get_legend_handles_labels()
#     fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(0.95, 0.95))
#
#     plt.suptitle('Manual Pairwise Scatter Plot Matrix', y=0.95)
#     plt.tight_layout()
#     plt.show()


# 使用
# manual_pairplot(df, features, 'cluster')
plot_df = df[features + ['cluster']].copy()
print(plot_df)