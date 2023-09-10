#hipótesis de collatz 

n=int(input("Introduce un número entero positivo: "))
pasos=0
while n<=0:
    n=int(input("Por favor, introduzca un número entero positivo: "))

while n!=1:
    print(n)
    if n%2==0:
        n//=2
    else:
        n=3*n+1
    pasos+=1
print(n)
print("Número de pasos:",pasos)