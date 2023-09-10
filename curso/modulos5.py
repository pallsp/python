from random import random, seed

seed(0) #con seed puedo establecer un valor semilla a partir del cual se generarán los valores pseudoaleatorios, así, los valores serán siempre los mismos
#si no usamos seed los valores no serán los mismos porque se usará una semilla distinta cada vez
for i in range(5):
    print(random())

#seed lo podemos usar como seed(), y tomará como valor semilla la hora actual, o como seed(entero), y le pasaremos un valor entero que será la semilla fija
#también existe randrange(inicio, fin, incremento)
#choice(secuencia) elige un elemento aleatorio de la secuencia
#sample(secuencia, numero_elementos) crea una secuencia que consta de numero_elementos elementos, si no especificamos este segundo argumento el valor por defecto es 1
