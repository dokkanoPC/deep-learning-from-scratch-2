import numpy as np
D,N=8,7
x=np.random.rand(1,D)
y=np.repeat(x,N,axis=0)#forward
print(y)
dy=np.random.rand(N,D)
dx=np.sum(dy,axis=0,keepdims=True)#backward
print(dx)