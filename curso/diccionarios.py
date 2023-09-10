#no son secuencias y son mutables

#para definir un diccionario

diccionario= {"Pablo": 23, "Laura": 20} #estructuras formadas por pares clave-valor, los pares se separan por comas y las claves y valores por dos puntos
dicc_vacio={} #puedo crear un diccionario vacío

print(diccionario)
print(dicc_vacio)

#las claves (keys) deben ser únicas y pueden ser de cualquier tipo de dato excepto una lista
#un diccionario no es una lista, una lista almacena un conjunto de valores numerados y un diccionario almacena pares de valores
#los diccionarios solo funcionan en el sentido clave->valor, no al revés
print(len(diccionario))

#para hacer el código más legible, un diccionario puede escribirse así

otro_dicc={
        "Barcelona": "Cataluña",
        "Zaragoza": "Aragón", 
        "València": "País Valencià",
        "Albacete": "Castilla-La Mancha"
}