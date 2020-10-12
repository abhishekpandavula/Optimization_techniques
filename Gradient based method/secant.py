import numpy as np
def delta(a):
    if a< -0.01 or a>0.01:
        return 0.01*abs(a)
    else:
        return 0.0001

###################
# Here is the function given in the question
def f(x):
    return np.cos(x) + 3*(x**2) - 25*x

####################
def f_dash(x):
    return (f(x+delta(x))-f(x-delta(x)))/(2*delta(x))
print("Enter the intervel \n")
print("Enter a")
a = float(input())
print("Enter b")
b= float(input())
print("Enter the number of iterations \n"
      "if iterations is not mentioned then enter '0'\n "
      "if no of iterations is mentioned then enter no. of iterations")
iterations = int(input())
####################
# epsilon e
e = 0.5

##################
print(f"f'({a}) = (f({a}+{delta(a)}) - f({a}-{delta(a)})) / 2({delta(a)}) = {f_dash(a)}")
print(f"f'({b}) = (f({b}+{delta(b)}) - f({b}-{delta(b)})) / 2({delta(b)}) = {f_dash(b)}\n")
i=1

if (f_dash(a) < 0 and f_dash(b) > 0) or (f_dash(a) > 0 and f_dash(b) < 0):
    z = b -((b-a)/(f_dash(b)-f_dash(a)))*f_dash(b)

    while True:
        if iterations!=0 and i >iterations:
            break
        z = b -((b-a)/(f_dash(b)-f_dash(a)))*f_dash(b)
        print("Iteration ",i)
        print(f"z = {b} -(({b}-{a})/({f_dash(b)}-({f_dash(a)})))*{f_dash(b)} = {z}")
        if f_dash(z) > 0:
            a, b = a, z
        else:
            a, b = z, b
        print(f"f'({z}) = (f({z}+{delta(z)}) - f({z}-{delta(z)})) / 2({delta(z)}) = {f_dash(z)}")
        print("minimum is in ({},{})".format(a,b))
        i+=1
        if (abs(f_dash(z)) < e):
            print(f"|f'({z})|< eplilon")
            print("min at z = ",z)
            print("\n")
            if (iterations ==0):
                break
        else:
            print(f"|f'({z})|> eplilon")
            print("\n")


