#decidir el orden de mayor a menor de 3 números
n1=int(input("Introduce un número: "))
n2=int(input("Introduce un número: "))
n3=int(input("Introduce un número: "))

mayor=n1

if n2>=mayor: mayor=n2
if n3>=mayor: mayor=n3

if n1==mayor:
    mediano=n2
    peq=n3
    if mediano<=n3: 
        mediano=n3
        peq=n2

if n2==mayor:
    mediano=n1
    peq=n3
    if mediano<=n3: 
        mediano=n3
        peq=n1
        
if n3==mayor:
    mediano=n2
    peq=n1
    if mediano<=n1: 
        mediano=n1
        peq=n2
   

print("El mayor es", mayor,"\nEl mediano es", mediano,"\nEl pequeño es", peq)