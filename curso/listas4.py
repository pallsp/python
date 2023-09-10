#podemos recorrer listas
mi_lista=[2,5,8,9,40]
print("Longitud de mi lista:",len(mi_lista))
for i in range(len(mi_lista)):
    print("Elemento mi_lista[",i,"]:",mi_lista[i])

total=0
for i in range(len(mi_lista)):
    total+=mi_lista[i]

print("El total es:", total)

#el for puede recorrer de forma automatica las listas

for i in mi_lista:
    print(i)

#intercambiar como un espejo elementos de una lista
#notar que otra_lista[len(otra_lista)-i-1] es el elemento espejo de otra_lista[i]
otra_lista=[2,3,5,-1,4]

for i in range(len(otra_lista)//2):
    otra_lista[i],otra_lista[len(otra_lista)-i-1] = otra_lista[len(otra_lista)-i-1], otra_lista[i]

print(otra_lista)