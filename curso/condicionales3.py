#decidir cuál es el mayor de tres números

n1=int(input("Introduce un número: "))
n2=int(input("Introduce un número: "))
n3=int(input("Introduce un número: "))
#versión tocha
if n1>=n2: 
    mayor=n1
    if mayor>=n3: print("El mayor es",mayor)
    else: print("El mayor es",n3)
else: 
    mayor=n2
    if mayor>=n3: print("El mayor es",mayor)
    else: print("El mayor es",n3)
#versión breve
mayor=n1
if n2>=mayor: mayor=n2
if n3>=mayor: mayor=n3

print("El mayor es",mayor)



