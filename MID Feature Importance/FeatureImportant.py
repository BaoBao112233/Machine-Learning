from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
# RandomForestRegressor là 1 mô hình dạng cây ,một công cụ ước tính meta phù hợp với một số cây quyết định phân loại trên các mẫu phụ khác nhau của bộ dữ liệu và sử dụng tính trung bình để cải thiện độ chính xác và kiểm soát dự đoán quá mức.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load boston housing dataset as an example

boston = fetch_california_housing()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]
rf = RandomForestRegressor()
rf.fit(X,Y)
# print(boston)

forest_importances = pd.Series(rf.feature_importances_, index = boston.feature_names)
std = np.std([rf.feature_importances_ for tree in rf.estimators_], axis = 0)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr = std, ax = ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurty")
print(fig.tight_layout())