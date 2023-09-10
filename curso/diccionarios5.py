#para agregar una nueva clave con su valor lo haremos como si cambiásemos el valor de una clave, pero poniendo como clave una que no exista

diccionario={"Pablo":23, "Andrea":17, "Laura":20,"Antonio":22}
print(diccionario)
diccionario["Anna"] = 26
print(diccionario)


#pero también podremos insertar pares clave-valor con el método .update()
diccionario.update({"Marc":13})
print(diccionario)


#también podemos eliminar una clave (y por tanto su valor) con la instrucción del
del diccionario["Pablo"]
print(diccionario)

#puedo usar también .popitem() para eliminar el último par
diccionario.popitem()
print(diccionario)

#puedo eliminar también por clave
diccionario.pop("Antonio")
print(diccionario)

#puedo obtener un valor a partir de una clave
print(diccionario.get("Andrea"))

#puedo eliminar todos los elementos de un diccionario con .clear()
#puedo copiar los elementos de un diccionario en otro con .copy()