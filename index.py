#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        for line in enumerate(f):
            [x, y] = line[1].split(',')
            if line[0] == 0:
                data_set = np.array([[float(x), float(y)],])
            else:
                data_set = np.append(data_set, [[float(x), float(y)],], axis = 0)

        return data_set


def plot_data(data_set, theta):
    plt.plot(data_set[:, 1], data_set[:, 2], 'rx')
    plt.plot(data_set[:, 1:2], (data_set[:, 0:2] @ theta))
    plt.ylabel('Profit in $10,000s')
    plt.xlabel('Population of City in 10,000s')
    plt.show()


def append_X0(data_set):
    '''
    This functions adds the arbitrary X value for theta zero.
    '''
    [m, _] = data_set.shape
    return np.append(np.ones((m, 1)), data_set[:,], axis=1)


def cost_function(X, y, theta):
    [m, _] = X.shape
    hOfX = X @ theta
    return (1/(2*m)) * ((hOfX - y) ** 2).sum()


def gradient(X, y, theta):
    [m, _] = X.shape
    hOfX = X @ theta
    return np.array((1/m) * (X[:,] * (hOfX[:,] - y[:,])).sum(axis=0))


def gradient_decent(X, y, theta, alpha, iterations):
    for _ in range(iterations):
        gradients = np.transpose([gradient(X, y, theta)])
        temp = theta - (alpha * gradients)

        theta = temp
    return theta

def main(filename):
    data_set = read_data(filename)
    data_set = append_X0(data_set)
    initial_theta = np.array([[-1], [2]])
    cost_function(data_set[:, 0:2], data_set[:, 2:3], initial_theta)
    theta = gradient_decent(data_set[:, 0:2], data_set[:, 2:3], np.zeros((2, 1)), 0.01, 1500)
    plot_data(data_set[:,0:3], theta)


if __name__ == "__main__":
    main('data_set.txt')
