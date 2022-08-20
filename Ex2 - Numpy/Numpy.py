import numpy as np

a = np.array([1, 3, 4, 5, 3, 8]) # Khởi tạo mảng

A = a.ndim # Hiển thị số chiều của mảng
# print(A)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

c = np.array([[1, 3, 5, 7], [ 2, 4, 6, 8]])

B = b.ndim
# print(B)

# print(a[:4]) # Lấy dữ liệu từ đầu cho đến vị trí n - 1 (n = 4)
# print(b[0][:3]) # Dùng cho mảng 2 chiều

# print(a[2:4]) # Lấy dữ liệu từ vị trí m đến vị trí n - 1 (m = 2, n = 4)

# print(b.shape) # Hiển thị (số hàng, số cột) <=> (2, 4);

# print(len(a)) # Hiểu thị độ dài của mảng

# print(np.arange(3, 4, 0.1)) # Khởi tạo 1 mảnh ngẫu nhiên từ m đến n - a (m = 3, n = 4, a = 0.1)

# print(b[0] + b[1]) # Cộng từng phần tử của cả 2 mảng lại với nhau

# print(b[0] - b[1]) # Các phần tử của mảng trước trừ các phần tử của mảng sau

# print(b[0] * b[1]) # Các phần tử của mảng trước nhân với các phần tử của mảng sau

# print(b[0] / b[1]) # Các phần tử của mảng trước chia cho các phần tử của mảng sau

# Các phép tính trên chỉ có tác dụng với các mảng cùng hình dạng
# print(b / c)