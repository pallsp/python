#decidir el orden de mayor a menor de 3 números
n1=int(input("Introduce un número: "))
n2=int(input("Introduce un número: "))
n3=int(input("Introduce un número: "))

mayor=max(n1,n2,n3)
minimo=min(n1,n2,n3)

if n1!=mayor and n1!=minimo: print("El mayor es",mayor,"\nEl mediano es", n1,"\nEl minimo es", minimo)
if n2!=mayor and n2!=minimo: print("El mayor es",mayor,"\nEl mediano es", n2,"\nEl minimo es", minimo)
if n3!=mayor and n3!=minimo: print("El mayor es",mayor,"\nEl mediano es", n3,"\nEl minimo es", minimo)