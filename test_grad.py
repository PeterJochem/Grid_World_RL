import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import grad

# a named Python function
def sin(w):
    return np.sin(w)

g = lambda w: np.sin(w)

# np.maximum returns the element wise maximum across multipl arrays
# each value array will be one dimensional - so the elementwise maximum will
# simly return the maximum
f = lambda w: np.maximum( w * 10, w * 4 )

# create a sample of points to plot over
w_vals = np.linspace(-5, 5 ,200)


# test function input
def my_function(w):                 
    y = np.sin(w**3)
    return y

# create instance, inputting function on creation
test = grad(my_function)

