diccionario={"Pablo":23, "Andrea":17, "Laura":20,"Antonio":22}
for i in diccionario:
    print(i,"->",diccionario[i])

diccionario["Laura"]=21
print()
for i in diccionario:
    print(i,"->", diccionario[i])

print("\nSALIDA ORDENADA\n")
#podemos ordenar la salida usando la función sorted() para ordenar por clave
for i in sorted(diccionario):
    print(i,"->",diccionario[i])

#al igual que .keys(), existe .values(), que nos permite obtener una lista de valores
for i in diccionario.values():
    print(i)