import numpy as np
import pandas as pd

datafame = pd.read_csv('test.csv', header = None)
# header = None: Để tự động lấy header
# header = n(int): Lấy dòng thứ n làm header
# print(datafame[3])
df = datafame[3]

df.to_csv('print.csv')
#Hàm to_csv('name.csv') dùng để tạo file name.csv để lưu trữ giá trị trả về của biến df
