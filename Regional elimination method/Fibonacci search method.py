import numpy as np

#####################################
def f(x):
    return -3*(x**3)*np.sin(2*x)+4*x*np.cos(3*x)+2*x
########################################

print("Enter the interval")
print("Enter Lower Boundary a = ")
a=float(input())
print("Enter Upper Boundaryb = ")
b=float(input())
print(f"a = {a}, b = {b}")

L=b-a
print(f"Length of the interval = {L} ")

k=2
print("set value of k = ",k)

print("if desired number of function evaluation is given then press '0'\n else if number of iterations press 1")
condition=int(input())

if (condition==0):
    print("Enter number of function evaluations m =")
    m=float(input())
elif (condition==1):
    print("Enter number of iterations =")
    m=float(input())+1
    
def fib(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else :
        return fib(n-2)+fib(n-1)
i = 1
while (k!=m+1):
    Lk=fib(m-k+1)/fib(m+1)
    Lk1=(Lk)*L
    print(f"Iteration {i}")
    print("value of L{}* = {}".format(k,Lk1))
    x1=a+Lk1
    print(f"value of x1 ={x1} and f(x1) ={f(x1)} is")
    x2=b-Lk1
    print(f"value of x2 = {x2} and f(x2) ={f(x2)} is")
    
    if (f(x1)>f(x2)):
        print(f"f(x1)>f(x2) so eliminate({a},{x1})")
        a=x1 #Eliminating region between (a,x1)
    else :
        if (f(x1)<f(x2) ):
            print(f"f(x1)<f(x2) so eliminate({x2},{b})")
            b=x2 #Eliminating region between (x2,b)
    print(f"New interval is (a,b) = ({a},{b})\n")
    i = i+1        
    k=k+1
                          
        
        
   
print (f"Minimum is in ({a},{b})")