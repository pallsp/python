numeros = [10,-5,22,13,-43]
print(numeros)
print(numeros[0]) #acceso a valores de la lista
numeros[2] = 36 #indexar y cambiar valores de la lista
print(numeros)
print(len(numeros)) #la función len nos devuelve la longitud de la lista
del numeros[0] #eliminar elementos, es una instruccion
print(numeros)

#los índices negativos sirven y son útiles
print(numeros[-1]) #el índice -1 nos devuelve el último elemento de la lista
#de igual forma el -2 nos devolverá el penúltimo, el -3 el antepenúltimo, y así sucesivamente hasta llegar al primer elemento de la lista, 
#y de ahí no se podrá ir más allá

#las listas admiten datos de diferentes tipos:

lista=[2,3,-2.1,"hola",[2,5.3]]
print(lista)