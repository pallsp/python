#factoriales

#forma 1
def factorial_function(n):
    if n<0:
        return None
    elif n==0:
        return 1
    
    factorial=1
    while n>1:
        factorial*=n
        n-=1
    return factorial

#forma 2
def factorial(n):
    if n<0:
        return None
    elif n<2:
        return 1
    producto=1
    for i in range(2,n+1):
        producto*=i
    return producto
    


factoriales= [factorial(i) for i in range(1,11)]
print(factoriales)