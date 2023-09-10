#decidir si un número es primo o no
def is_prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

control=0
n=0

while control==0:
    while n<=0:
        n=int(input("Introduce un número: "))

    if is_prime(n):
        print("El número introducido es primo")
    else:
        print("El número introducido no es primo")
    
    control=int(input("Quieres seguir introduciendo números? SÍ-0 NO-1: "))
    n=0


