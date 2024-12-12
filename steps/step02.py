import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

# class Function:
#     def __call__(self, input):
#         x = input.data
#         y = x ** 2
#         output = Variable(y)
#         return output
# # call method: f=Function() 형태로 정의하고 f()로 call

# x = Variable(np.array(10))
# f = Function()
# y = f(x)

# print(type(y))
# print(y.data)

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output
    
    def forward(self, x):
        raise NotImplementedError
    
class Square(Function):
    def forward(self, x):
        return x ** 2

x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)