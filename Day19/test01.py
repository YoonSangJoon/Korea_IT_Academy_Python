from pylab import *

# x = linspace(-1.6, 1.6, 10000)
# f = lambda x: (sqrt(cos(x)) * cos(200*x) + sqrt(abs(x)) - 0.7) * \
#                 pow((4 - x * x), 0.01)
x = linspace(10, -10, 100)
f = lambda x: 2 * x + 6
plot(x, list(map(f, x)))
show()