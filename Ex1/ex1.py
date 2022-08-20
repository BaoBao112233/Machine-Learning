from unittest import result
from sklearn import tree

def inputData(x):
    if x == "nhẹ":
        return 1
    elif x == "thấp":
        return 2
    elif x == "trung bình":
        return 3
    elif x == "cao":
        return 4
    elif x == "nặng":
        return 5
    elif x == "ít":
        return 6
    elif x == "nhiều":
        return 7

def training(a, b, c, d):
    #Bước 1: Thu thập dữ liệu
    #Bước 2: Xử lý dữ liệu
    #Bước 3: Xây dựng model
    #Bước 4: Dự đoán kết quả
    #Bước 5: Đánh giá thuật toán/ model

    # Khởi tạo 1 cây quyết định tên là my tree
    my_tree = tree.DecisionTreeClassifier()
    #Bước 1: Thu thập dữ liệu
    feature = [[1, 3, 3, 7],
            [5, 2, 4, 6],
            [1, 2, 4, 6],
            [5, 4, 4, 3],
            [1, 4, 4, 7],
            [3, 2, 3, 7],
            [3, 3, 3, 6],
            [5, 2, 2, 7],]

    label = [0, 1, 1, 0, 0, 0, 0, 1]
    #Bước 2: Xử lý dữ liệu
    result = my_tree.fit(feature, label).predict([[a, b, c, d]])
    return result
    

#Bước 4: Dự đoán kết quả
# prResult1 = result.predict([[1, 4, 3, 6]])
# prResult2 = result.predict([[1, 4, 3, 7]])

def functions(prResult):
    if prResult == 0:
        return "Không"
    elif prResult == 1:
        return "Có"

# print("Bệnh nhân 1" + str(prResult1))
# functions(prResult1)
# print("Bệnh nhân 2" + str(prResult2))
# functions(prResult2)

if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(0, 4):
        if i == 0:
            x = str(input("Nhập cân nặng: ")).lower()
            a = inputData(x)
        elif i == 1:
            x = str(input("Nhập chiều cao: ")).lower()
            b = inputData(x)
        elif i == 2:
            x = str(input("Nhập huyết áp: ")).lower()
            c = inputData(x)
        elif i == 3:
            x = str(input("Nhập vận động: ")).lower()
            d = inputData(x)

    result = training(a, b, c, d)
    print(functions(result) + " bị bệnh tim!!!")