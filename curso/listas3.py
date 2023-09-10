lista=[] #creamos lista vacía

for i in range(5):   #la rellenamos pasandola por un for
    lista.append(i*2-1)
print(lista)

lista.clear() #limpiar una lista
print(lista)

for i in range(5):
   lista.append(int(input("Introduce un elemento de la lista: "))) #importante!!!!! usar .append() para añadir elementos, no podemos indexarlos con lista[i]

print(lista)