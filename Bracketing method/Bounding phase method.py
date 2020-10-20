import numpy as np
def f(x):
    #here we have to enter the question
    return np.cos(x**2)+3*(x**2)+62


def x(k):
    if k == 0:
        #####################
        x_0= 1
        #######################
        return x_0
    else:
        #####################
        result = 1
        #######################
        result = result + (2**k)*v
        return result


print(f"x(0) = {x(0)}")
v = float(input("Enter the increment parameter:\n v =  "))
print(f"Increament parameter = {v}\n")
print(f"f(x(0) - abs(v)) = {f(x(0) - abs(v))}\n")
print(f" f(x(0)) = { f(x(0))}\n")
print(f"f(x(0)+ abs(v)) = {f(x(0)+ abs(v))}\n")

if f(x(0) - abs(v))>=f(x(0)) and f(x(0))>=f(x(0)+ abs(v)):
    print("delta is + ve\n")
elif f(x(0) - abs(v))<=f(x(0)) and f(x(0))<=f(x(0)+ abs(v)):
    print("delta is - ve \n")
elif f(x(0) - abs(v))>=f(x(0)) and f(x(0))<=f(x(0)+ abs(v)):
    print(f"minimum is between {x(0) - abs(v)} and {x(0)+ abs(v)}")
else:
    x(0)

print("Do x(k+1) = x(k) + 2**k * delta\n")
    


