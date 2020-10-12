import numpy as np
def delta(a):
    if a< -0.01 or a>0.01:
        return 0.01*abs(a)
    else:
        return 0.0001

######################################
# Here is the function given in the question
def f(x):
    return (0.5)*(x**3)-1.75*(x**2)+2*x-9

#######################################
def f_dash(x):
    return (f(x+delta(x))-f(x-delta(x)))/(2*delta(x))

def f_ddash(x):
    return (f(x + delta(x))- 2*f(x) + f(x - delta(x)))/(delta(x)**2)

####################################
# first derivative value
print("f dash(x) = ", f_dash(1.5992))

# Second derivative value
print("f double dash(x) = ",f_ddash(2))
