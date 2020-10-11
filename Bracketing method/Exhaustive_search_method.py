import numpy as np
def f(x):
    #here we have to enter the question
    return 10-(x**(1/2))*np.sin(x)
    
condition = input("Enter 'n' or 'l'")
if condition == 'n':
    # n = number of intervals into which the given interval is divided
    n = int(input("Enter the value of n: "))
    print(f"n = {n}\n")
    a,b = map(float,input("Enter the limits in the format a space b").split())
    print(f"a = {a}\n b = {b}")
    x1 = a 
    delta_x = (b-a)/n

else:
    # Enter the value of l over here
    ls = input("Enter the length l =")
    l = float(ls)
    print(f"l = {l}")
    print("Enter the limits in the format a space b \na b \n")
    a,b = map(int,input().split())
    print(f"a = {a}\n b = {b}")
    x1 = a 
    delta_x = l/2


x2 = x1 + delta_x
x3 = x2 + delta_x
i=1
print(f"delta_x = {delta_x}\n")
while x3<=b:
    print(f"Iteration {i}\n x1 ={x1}\t x2={x2}\t x3 = {x3}\n f(x1) = {f(x1)}\tf(x2) = {f(x2)}\tf(x3) = {f(x3)}\n")
    i = i+1
    if f(x1)>=f(x2) and f(x2)<=f(x3):
        print("f(x1) > f(x2) < f(x3)\n")
        print(f" Minimum point lies in the interval (x1,x3) = ({x1},{x3})\n")
        break

    else:
        print("f(x1) > f(x2) > f(x3)\n")
        temp = x2
        x1 = temp
        x2 = x3
        x3 = x2 + delta_x

if x3>b:      
    print(f"No minimum in ({a},{b}) or\n boundary point is the minimum point\n")