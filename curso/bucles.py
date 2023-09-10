#un programa que lee una secuencia de números y cuenta cuantos son pares, cuantos impares
#el programa termina cuando encuentra un cero

numero = int(input("Introduce un número: "))
pares=0
impares=0
while numero!=0:
    if numero % 2==0:
        pares+=1
    else:
        impares+=1
    numero=int(input("Introduce un número: "))

print("La cantidad de números pares es:", pares,"\nLa cantidad de números impares es:",impares)