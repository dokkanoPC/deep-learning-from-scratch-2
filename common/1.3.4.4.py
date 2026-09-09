import numpy as np
D,N=8,7
x=np.random.rand(N,D)
y=np.sum(x,axis=0,keepdims=True)#forward
print(y)
dy=np.random.rand(1,D)
dx=np.repeat(dy,N,axis=0)#backward
