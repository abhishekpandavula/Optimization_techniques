import numpy as np

print("Enter the initial point")
print("x1 = ")
x1 = float(input())

print("Enter increment parameter")
print("v = ")
v = float(input())
x2 = x1 + v
####################
# epsilon e
e = 0.01
######################

############################
# Here is the function given in the question
def f(x):
    return (x**5)-5*(x**3)-20*x+5

##############################
f1 = f(x1)
print(f"x1 = ",x1)
print(f"f1 = {f1}")
f2 = f(x2)
print(f"x2 = ",x2)
print(f"f2 = {f2}")

if f(x1) >= f(x2):
    x3 = x1 + 2*v
    f3 = f(x3)
    print("f(x1) >= f(x2)")
    print("x3 = x1 + 2*v")
    print(f"x3 = ",x3)
    print(f"f3 = {f3}")

else:
    x3 = x1 - v
    f3 = f(x3)
    print("f(x1) < f(x2)")
    print("x3 = x1 - v")
    print(f"x3 = ",x3)
    print(f"f3 = {f3}")

a1 = (f2 - f1)/(x2 - x1)
print("a1 = (f2 - f1)/(x2 - x1)")
print(f"a1 = {a1}")

a2 = (1/(x3 - x2))*(((f3 - f1)/(x3 - x1)) - a1)
print(f"a2 = {a2}")

x_ = ((x1+x2)/2) - (a1/(2*a2))
print(f"x- = {x_}")

print(f"f(x-) = {f(x_)}")
    

################
print("\n")
print(f(1.6))
print(f(1.6))
print(f(1.6))