#métodos, funciones e instrucciones de listas

print("---DEFINICIÓN LISTAS---")
lista=[] #defino lista vacía
otra_lista=["Pablo","Laura","Anna"] #defino lista con elementos 
print(lista)
print(otra_lista)
print("---.APPEND()---")
lista.append(4) #añado al final de la lista
print(lista)
lista.append(11)
print(lista)
print("---.INSERT()---")
lista.insert(1,20) #insertar en una determinada posición (posicion primer argumento y el valor a insertar segundo argumento)
print(lista)
print("---MOSTRAR LONGITUD CON LEN---")
len(lista) #contar el número de elementos de la lista ó la longitud de la lista
print(len(lista))
print("---ACCEDO A ELEMENTOS---")
print(lista[0], lista[1], lista[2]) #puedo acceder a los elementos de una lista
print("---SLICES---")
print(lista[:]) #puedo mostrar todos los elementos
print(lista[0:2]) #puedo mostrar elementos desde start hasta end-1 con [start:end]
print(lista[:3], lista[1:]) #si omito start empezará desde el elemento 0 y si omito el end terminará en el último elemento
print("---MODIFICO ELEMENTOS---")
lista[0] = 25 #puedo modificar elementos de una lista
print(lista)
print("---.SORT()---")
lista.sort() #puedo ordenar una lista (si sus elementos son comparables)
print(lista)
print("---.REVERSE()---")
lista.reverse() #puedo ordenar de forma inversa una lista (si sus elementos son comparables)
print(lista)
print("---SORTED---")
print(sorted(lista)) #puedo ordenar una lista de forma que no altere la lista original, es decir, sólo la imprime ordenada
print(lista)
print("---.CLEAR()---")
lista.clear() #limpio la lista de elementos
print(lista)
print("---.INDEX()---")
print(otra_lista.index("Anna")) #puedo encontrar el índice de un elemento
print("---.POP()---")
nombre=otra_lista.pop(1) #puedo eliminar elementos de la lista por índice a la vez que nos permite guardar eso que eliminamos en una variable
print(otra_lista) #si no pasamos ningún argumento a .pop() entonces eliminará el último
print(nombre)
otra_lista.insert(1,"Laura")
print("---.REMOVE()---")
otra_lista.remove("Anna") #puedo eliminar elementos de la lista por valor
print(otra_lista)
otra_lista.append("Anna")
print("---DEL---") #es una instruccion!!!!!!!!!!
del otra_lista[0] #puedo eliminar elementos de la lista
print(otra_lista)
del otra_lista[:] #puedo eliminar todos los elementos de la lista
print(otra_lista)
del otra_lista #puedo eliminar la lista
#si hacemos esto nos dará error print(otra_lista)
lista.append(32)
lista.append(56)
lista.append(-7)
print("---COPIAR ELEMENTOS---")
lista_nueva=lista[:] #puedo copiar elementos, copiar el contenido
lista_alterada=lista #puedo copiar la direccion de memoria donde se almacena la lista
print(lista_nueva) 
lista.append(45)
print(lista_nueva)
print(lista_alterada)




#operadores

#+ para unir listas
#* para multiplicar (replicar) listas
#in/ not in operadores de inclusión 