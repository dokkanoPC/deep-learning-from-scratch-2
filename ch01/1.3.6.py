class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr #learning rate

    def update(self, params, grads):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]
model=TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
optimizer=SGD()
for i in range(10000):
    x_batch, t_batch = get_mini_batch()
    loss = model.forward(x_batch, t_batch)
    model.backward()
    optimizer.update(model.params, model.grads)
    ...