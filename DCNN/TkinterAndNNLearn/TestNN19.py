import numpy as np


def sigmoid(x):
    # Логистическая функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


# Создание класса одного нейрона
class Neuron:
    def __init__(self, weights, bias):
        # Объявление весов связей и нейрона смещения
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Вычисление выходного значения нейрона
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


weights = np.array([0, 1])  # w1 = 0, w2 = 1
bias = 4                    # c = 4
n = Neuron(weights, bias)

x = np.array([2, 3])        # x = 2, y = 3
print(n.feedforward(x))     # 0.9990889488055994


class OurNeuralNetwork:
    """
    Данные нейросети:
        - два входа
        - два нейрона в скрытых слоях (h1, h2)
        - выход (o1)
    Нейроны имеют идентичные веса и пороги:
        - w = [0, 1]
        - b = 0
    """
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        # Класс Neuron из предыдущего раздела
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        # Вычисление выходных значений для нейронов скрытого слоя
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        # Входы для o1 — это выходы h1 и h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        return out_o1


network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))  # 0.7216325609518421


def sigmoid_derivative(i):
    return i * (1-i)


# Класс нейронной сети
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        # Прямое распространение
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # Метод обратного распространения ошибки
        # application of the chain rule to find derivative
        # of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T,
                            (2 * (self.y - self.output)
                             * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,
                            (np.dot(2 * (self.y - self.output)
                                    * sigmoid_derivative(self.output),
                                    self.weights2.T)
                             * sigmoid_derivative(self.layer1)))
        # update the weights with the derivative (slope)
        # of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

