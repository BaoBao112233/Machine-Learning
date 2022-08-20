import numpy as np
import pandas as pd
# from sklearn.preprocessing import Imputer Đây là cho Version cũ
from sklearn.impute import SimpleImputer

data = pd.read_csv('data.csv', header= None) # Dữ liệu trả về sẽ là dạng Dataframe
# Pandas DataFrame là một cấu trúc chứa dữ liệu hai chiều và các nhãn tương ứng của nó

print(data)

x = data.values # Chuyển đổi dữ liệu dạng DataFrame sang Array

imp = SimpleImputer(missing_values= np.NaN, strategy = 'most_frequent')
# SimpleImputer là hàm dugnf để xử lyas các dữ liệu bị mất
# missing_values là để định nghĩa cho dữ liệu bị mất là gì
# strategy = 'mean' là lấy giá trị trung bình và điền vào chỗ bị mất dữ liệu
# strategy = 'most_frequent' là lấy giá trị xuất hiện nhiều nhất trong đata

# strategy : str, default='mean'
#         The imputation strategy.

#         - If "mean", then replace missing values using the mean along
#           each column. Can only be used with numeric data.
#         - If "median", then replace missing values using the median along
#           each column. Can only be used with numeric data.
#         - If "most_frequent", then replace missing using the most frequent
#           value along each column. Can be used with strings or numeric data.
#           If there is more than one such value, only the smallest is returned.
#         - If "constant", then replace missing values with fill_value. Can be
#           used with strings or numeric data.

#         .. versionadded:: 0.20
#            strategy="constant" for fixed value imputation.

imp.fit(x) # Chỉ là hàng cho dữ liệu vào và nhận tham số dạng Aray

result = imp.transform(x) # Thực hiện điền giá trị và vị trí bị mất  

print(result)