import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))  # 内積
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # 行列の積

W1=np.random.randn(2, 4)  # 2行4列の行列をランダムに生成
print(W1)
b1=np.random.randn(4)  # 4次元のバイアスをランダムに生成
print(b1)
x=np.random.randn(10, 2)  # 10行2列の行列をランダムに生成
print(x)
h=np.dot(x, W1)+b1  # 行列の積とバイアスの加算
print(h)
print(h-(h-b1))