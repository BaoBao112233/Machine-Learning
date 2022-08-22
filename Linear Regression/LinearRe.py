import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('Advertising.csv',header=0)

X = dataFrame.values[:, 2] # Lấy dữ liệu ở cột số 2(Radio), tất cả các dòng
Y = dataFrame.values[:, 4] # Lấy dữ liệu ở cột số 4(Sales), tất cả các dòng

# plt.scatter(X, Y, marker='o')
# plt.show() # Không thể chạy trên Pycham, hãy chạy trên Command Promtp hoặc PowerShell

def predict(new_radio, weight, bias):
    return weight * new_radio + bias

def cost_function(arrayX, arrayY, weight, bias): # MSE function (MSE_function.png)
    n = len(arrayX)
    sum_error = 0
    for i in range(n):
        sum_error += (arrayY[i] - (weight*arrayX[i] + bias))**2

    return sum_error / n

def update_weight(arrayX, arrayY, weight, bias, learning_rate):
    n = len(X)
    weight_temp = 0.0
    bias_temp = 0.0
    for i in range(n):
        weight_temp += -2*arrayX[i]*(arrayY[i] - (weight*arrayX[i] + bias))
        bias_temp += -2*(arrayY[i] - (weight*arrayX[i] + bias))
    
    weight -= (weight_temp/n)*learning_rate
    bias -= (bias_temp/n)*learning_rate

    return weight, bias

def train(arrayX, arrayY, weight, bias, learning_rate, times): #times: số lần lập
    save_his = []
    for i in range(times):
        weight, bias = update_weight(arrayX, arrayY, weight, bias, learning_rate)
        cost = cost_function(arrayX, arrayY, weight, bias)
        save_his.append(cost)
    
    return weight, bias, save_his


weight, bias, history = train(X, Y, 0.03, 0.0014, 0.0001, 60)
# print("Result:")
# print(weight)
# print(bias)
# print(history)
# print("Predictable value:")
# print(predict(19,weight,bias))

times = [i for i in range(60)]

plt.plot(times, history)
plt.show()

# print(X)
# print(Y)

# print(dataFrame)