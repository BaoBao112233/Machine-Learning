from gettext import npgettext
from sklearn.datasets import load_iris
# Hàm load_iris là hàm trả về 1 object dict chứa các keys và values
from sklearn.model_selection import train_test_split
# Hàm train_test_split là hàm dùng để chia dữ liệu làm 4 phần (3 phần training, 1 phần checking)
from sklearn.tree import DecisionTreeClassifier
import numpy as np

flowerData = load_iris().data
flowerTarget = load_iris().target

# print(len(flowerData))
# print(len(flowerTarget))
# print(flowerTarget)
X_train, X_test, Y_train, Y_test = train_test_split(flowerData, flowerTarget, random_state= 0)
# Vì là hàm train_test_split trả về 1 list 4 tham số
# Để tham số random_state = 0 để mỗi lần chạy lại sẽ trả về cùng 1 kết quả
# Để tham số random_state = 1 để mỗi lần chạy lại sẽ trả về 1 kết quả khác nhau

# print(X_train)
# print(X_test)
# print(Y_train)
# print(Y_test)
# X sẽ là data và Y sẽ là Target

# Training Model

model = DecisionTreeClassifier()
my_modelX = model.fit(X_train, Y_train)

textX = my_modelX.predict(X_test)

# my_modelY = model.fit(Y_train, X_train) #error
# textY = my_modelY.predict(Y_test)

# X_new = np.array([[2.0, 4.8, 5.3, 3.6]]) # Dữ liệu thô
#print(my_modelY.predict(X_new))
print(textX)

accuracy = my_modelX.score(X_test, Y_test)
# Hàm score dùng để đo độ chinh xác của model

print(accuracy)