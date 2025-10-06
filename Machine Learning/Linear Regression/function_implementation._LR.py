# x= training eg features , x_train
# y=training eg targets, y_train
# m - Number of training examples'
# w= parameter weights
# b= parameter bias
#x_i and y_i is the ith training data 


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

# x_train is size in 1000 square feet
# y_train is price in 1000s of dollars

x_train= np.array([1.0,2.0])
y_train= np.array([300.0,500.0])
print(f"x_train={x_train}")
print(f"y_train={y_train}")
print(f"x.train.shape: {x_train.shape}")
#defining total number of data
m=len(x_train)
print(f"total number of training egs={m}")
#m=x_train.shape[0]
# print (f"m={m}")

# Acccesing zeroth record as python is indexed zero
i=0
x_i=x_train[i]
y_i=y_train[i]
print(f"(x_^{i}, y_^{i})=({x_i}. {y_i})")

#Plotting the data
plt.scatter(x_train,y_train, marker='x', c='r')
plt.title("housing Prices")
plt.ylabel("Price in 1000s of dollars")
plt.xlabel("Size in 1000 square feet")
plt.show()

w=100
b=100
print(f"w={w}, b={b}")


def compute_model(x,w,b):
    """
    Computes the prediction of y given x and parameters w,b

    Args:
        x (ndarray (m,)): Input data, m examples
        w (scalar): weight parameter
        b (scalar): bias parameter
        both are model paramters


    Returns:
        f_wb (ndarray (m,)): The prediction of y given x and parameters w,b
    """
    m=x.shape[0]
    f_wb= np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b
    return f_wb

temp_f_wb= compute_model(x_train,w,b)
plt.plot(x_train,temp_f_wb, c='b', label='Our prediction')
plt.scatter(x_train,y_train, marker='x', c='r', label='Actual data')
plt.title("housing Prices")
plt.ylabel("Price in 1000s of dollars")
plt.xlabel("Size in 1000 square feet")
plt.legend()
plt.show()



