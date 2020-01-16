import numpy as np
class LogisticRegression:

    def __init__(self):
        self.X = None
        self.Y = None
        pass


    def _read_data(self, filename):
        with open(filename, mode='rt', encoding='utf-8') as f:
            for line in enumerate(f):
                [X1, X2, Y]  = line[1].split(',')
                if line[0] == 0:
                    X = np.array([[float(X1), float(X2)]])
                    Y_data = np.array([float(Y)])
                else:
                    X = np.append(X, [[float(X1), float(X2)],], axis = 0)
                    Y_data = np.append(Y_data, [float(Y)], axis = 0)

        self.X = X
        self.Y = Y_data
