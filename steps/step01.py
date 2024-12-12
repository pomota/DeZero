import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

data = np.array(1.0)
x = Variable(data)
print(x.data)

# x = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(x.ndim)