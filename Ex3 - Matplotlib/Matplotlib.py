import matplotlib.pyplot as plt
import numpy as np

# x = [3, 4, 5]

# y = [2, 6, 8]
# # x = [x1, x2]: x1 là hoành độ của điểm thứ 1 và x2 là hoành độ của điểm 2
# # y = [y1, y2]: y1 là tung độ của điểm thứ 1 và y2 là hoành độ của điểm 2
# plt.plot(x,y) # Nối các điểm trong mảng x va y
# plt.show() # Hiển thị đường đi qua các điểm


image = np.random.rand(30, 30)
plt.imshow(image)
plt.show()