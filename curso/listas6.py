lista1=[13,3,5]
lista2=lista1[:] #usamos las rebanadas para copiar listas, su contenido, no su dirección de memoria, así cuando modificamos la lista original no se altera la nueva
lista1[0] = 22
print(lista1)
print(lista2)

lista1.append(45)
print(lista1[1:3]) #se muestra desde 1 hasta el elemento 3-1=2, y también se pueden copiar