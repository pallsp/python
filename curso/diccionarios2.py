diccionario={"Andrea":24, "Pablo":23, "Anna":26, "Luis":18, "Joana":4}
print(diccionario["Pablo"]) #puedo acceder a un valor a través de su clave, parecido a la indexación

nombres=["Antonio", "Andrea", "Luis", "Anna", "Pablo"]

for nombre in nombres:
    if nombre in diccionario:
        print("Nombre:", nombre,", Edad:", diccionario[nombre])