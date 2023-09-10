#indexación de cadenas

cadena='me llamo pablo'
#podemos acceder a cada carácter de una cadena indexando como si fuera una lista, y también sirven índices negativos
for i in range(len(cadena)):
    print(cadena[i], end="")

print()

#también podemos iterar a través de cadenas

otra_cadena='hoy hace buen día'

for letter in otra_cadena:
    print(letter, end="")
print()

#también podemos usar rebanadas

mas_cadena="que tal estás"
print(mas_cadena[:])
print(mas_cadena[1:4])
print(mas_cadena[2:])
print(mas_cadena[2:-1])
print(mas_cadena[:6])

#también se pueden utilizar los operadores in y not in como siempre