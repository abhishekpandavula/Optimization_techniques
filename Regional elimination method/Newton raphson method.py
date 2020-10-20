import numpy as np
def delta(a):
    if a< -0.01 or a>0.01:
        return 0.01*abs(a)
    else:
        return 0.0001

######################################
# Here is the function given in the question
def f(x):
    return np.cos(5*x)+(x**2)

#######################################
def f_dash(x):
    return (f(x+delta(x))-f(x-delta(x)))/(2*delta(x))

def f_ddash(x):
    return (f(x + delta(x))- 2*f(x) + f(x - delta(x)))/(delta(x)**2)

####################################
# first derivative value
print("f dash(x) = ", f_dash(19.24))

# Second derivative value
print("f double dash(x) = ",f_ddash(19.24))
