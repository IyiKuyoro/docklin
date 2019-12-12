#! /usr/bin/env python3

import numpy as np
from LinearRegression import SingleVariableLinearRegression as LR

def single_variable_prediction(training_data_file, alpha, iterations, value):
    initial_theta = np.array([[-1], [2]])
    model = LR('data_set.txt', initial_theta, alpha, iterations)
    print('For a population of 70,000 we predict a profit of:', model(value)*10000)
    # model.plot_data('Profit in $10,000s', 'Population of City in 10,000s')


if __name__ == '__main__':
    single_variable_prediction('data_set.txt', 0.01, 2500, 7)
