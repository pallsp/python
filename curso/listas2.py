#añadir elementos a listas: append() e insert()
#añadir un elemento al final de una lista usamos append(): list.append(value) SIEMPRE AL FINAL
#añadir un elemento en el lugar que queramos de la lista usamos insert(): list.insert(pos,value) EN LA POSICION POS

lista= [23,14,7]
print(lista) #[23,14,7]
lista.append(30)
print(lista) #[23,14,7,30]
lista.insert(2,16)
print(lista) #[23,14,16,7,30]