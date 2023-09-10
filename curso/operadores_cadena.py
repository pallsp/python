#podemos usar + y * en cadenas

cadena="hola buenas tardes " + "señor presidente"
print(cadena)
otra_cadena = ", qué tal se encuentra?"
cadena_nueva = cadena+otra_cadena
print(cadena_nueva)
#básicamente para usar + como concatenador hemos de asegurarnos que ambos elementos a concatenar sean cadenas

#* es el operador de replicación o repetición, es conmutativo
print("Pablo"*3)
nombre = "luis" *4 #si es negativo el número devolvera una cadena vacía
print(nombre)
num_cadena = 3 * "5"
print(num_cadena)

#str() permite transformar numeros a cadenas

print(str(4))