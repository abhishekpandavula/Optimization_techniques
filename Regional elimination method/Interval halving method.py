import numpy as np
#######################################
def f(x):
    return x**4 - 5*(x**3) + 2*np.exp(x) - 5*np.cos(3*x)
#######################################

print("Enter a ")
a = float(input())
print("Enter b ")
b = float(input())

#choose termination parameter
e = 0.4
#################################

L = b-a

xm = (a + b)/2
print(f"xm = {xm} and f(xm) = {f(xm)}\n")

i = 0
while True:
    if abs(L)>=e:
        i = i+1
        print(f"Iteration {i}")
        print(f"L = {L}")
        x1 = a+ (L/4)
        if(f(x1)<f(xm)):
            print("f(x1)<f(xm)")
            print(f"Eliminate ({xm},{b})")
            b = xm
            xm = x1
            print(f"min is in ({a},{b})\n")
            L = b-a
        else:
            
            x2 = b - (L/4)
            print(f"x1 = {x1} and f(x1) = {f(x1)}")
            print("f(x1)>f(xm), so find x2")
            print(f"x2 = {x2} and f(x2) = {f(x2)}")
            if f(x2)<f(xm):
                print("f(x2)<f(xm)")
                print(f"Eliminate ({a},{xm})")
                a = xm
                xm = x2
                print(f"min is in ({a},{b})\n")
                L = b-a
            else:
                print("f(x2)>f(xm)")
                print(f"Eliminate ({a},{x1}) and ({x2},{b})")
                a = x1
                b = x2
                L = b-a
                print(f"min is in ({a},{b})\n")


            
    else:
        break






