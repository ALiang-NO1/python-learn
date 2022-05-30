import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron():
    def __init__(self, weights, bias):      # 初始化权重和偏置
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):  # 输入，然后通过激活函数处理输出
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

# weights = np.array([0, 1])
# bias = 4
# n = Neuron(weights, bias)
# x = np.array([2, 3])    # 0*2 + 3*1 + 4
# print(n.feedforward(x))

class NeuralNetworks():
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        self.h1 = Neuron(weights, bias)     # 声明两个神经元（输入层）
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)     # 用于获取结果（输出层）

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)     # 调用方法，获得两个输入[h1, h2)
        out_h2 = self.h2.feedforward(x)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))      # 以前馈结果为输入获得新前馈结果（隐藏层）
        return out_o1

network = NeuralNetworks()
x = np.array([2, 3])
print(network.feedforward(x))