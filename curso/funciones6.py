#recursividad con fibonacci y factoriales


#factorial
#si n=1 entonces n! = 1, si n no es 1 entonces n! =n*(n-1)!
#n! = n*(n-1)*(n-2)*(n-3)*...*1 = n(n-1)! = n(n-1)(n-2)! = ... = n*(n-1)*(n-2)*(n-3)*...*1! = n*(n-1)*(n-2)*(n-3)*...*1
def factorial(n):
    if n==1: return 1
    else:
        return n*factorial(n-1)



#fibonacci
#si n=0 entonces fibo(n)=0, si n=1 entonces fibo(1)=1, si n no es 0 y no es 1 entonces fibo(n) = fibo(n-1) + fibo(n-2)
def fibonacci(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(factorial(11))
for i in range(1,20):
    print(fibonacci(i))