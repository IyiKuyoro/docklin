import numpy as np
import matplotlib.pyplot as plt

class SingleVariableLinearRegression:

    def __init__(self, data_file, initial_theta, alpha, iterations):
        data = self._read_data(data_file)
        self.data_set = self._prepend_X0(data)
        self.X = self.data_set[:, 0:-1]
        self.y = self.data_set[:, -1:]
        [self.m, self.n] = self.data_set.shape
        self.theta = self._gradient_decent(initial_theta, alpha, iterations)

    def __call__(self, x):
        return ([[1, x]] @ self.theta)[0][0]

    def _read_data(self, filename):
        with open(filename, mode='rt', encoding='utf-8') as f:
            for line in enumerate(f):
                [x, y] = line[1].split(',')
                if line[0] == 0:
                    data_set = np.array([[float(x), float(y)],])
                else:
                    data_set = np.append(data_set, [[float(x), float(y)],], axis = 0)

            return data_set

    def _hOfX(self, theta):
        return self.X @ theta

    def _cost(self, theta):
        X = self.data_set[:, 0:-1]
        y = self.data_set[:, -1]

        [m, _] = X.shape
        hOfX = X @ theta
        return (1/(2*m)) * ((hOfX - y) ** 2).sum()

    def _gradient(self, theta):
        hOfX = self._hOfX(theta)
        return np.array((1/self.m) * (self.X[:,] * (hOfX[:,] - self.y[:,])).sum(axis=0))

    def _gradient_decent(self, theta, alpha, iterations):
        for _ in range(iterations):
            gradients = np.transpose([self._gradient(theta)])
            temp = theta - (alpha * gradients)

            theta = temp

        return theta

    def _prepend_X0(self, data):
        [m, _] = data.shape
        return np.append(np.ones((m, 1)), data[:,], axis=1)

    def plot_data(self, yLabel, xLabel):
        xDots = self.data_set[:, 1]
        y = self.data_set[:, -1]
        xLine = self.data_set[:, 1]

        plt.plot(xDots, y, 'rx')
        plt.plot(xLine, (self.data_set[:, 0:2] @ self.theta))
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.show()
