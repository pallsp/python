#números fibonacci
#n>=0
#una forma, esta te genera una lista con todos los elementos de la serie 
def fibonacci(n):
    nums_fibo=[0,1]
    i=2
    if n<0:
        print("Error, el número tiene que ser natural")
        return None
    
    while i<=n:
        nums_fibo.append(nums_fibo[i-1]+nums_fibo[i-2])
        i+=1
    return nums_fibo[n], nums_fibo

#otra forma, esta te devuelve solo el elemento buscado
def fibo(n):
    if n<0:
        print("Error, el número tiene que ser natural")
        return None
    elemento1=0
    elemento2=1
    if n==0: return elemento1
    if n==1: return elemento2
    suma=0
    for i in range(2,n+1):
        suma=elemento1+elemento2
        elemento1,elemento2=elemento2,suma
    return suma
       
     


for i in range(1,20):
    print(fibo(i))