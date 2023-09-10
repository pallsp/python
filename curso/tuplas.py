#las tuplas son como las listas pero inmutables: sus datos no se pueden modificar
#podemos definirlas de dos formas 

tupla_1 = (10,4,15,33) #las tuplas se definen con paréntesis
tupla_0=() #también se puede crear una tupla vacía
tupla_2 = "Luis","Juana","Andrea" #pero también se pueden definir separando sus valores por comas
print(tupla_1)
print(tupla_2)

#apuntar que si queremos crear una tupla de un solo elemento tendremos que poner una coma detrás del elemento, sino Python lo considerará como una variable
tupla=(2,)
print(tupla, type(tupla))

#como en las listas, los elementos de una tupla pueden ser de distinto tipo: enteros, cadenas, flotantes, booleanos, etc.
#podemos leer y acceder a los elementos de una tupla igual que en las listas
print(tupla_1[0])
print(tupla_2[2])

for nombre in tupla_2:
    print(nombre)



#PERO LAS TUPLAS NO SE PUEDEN ALTERAR
#no se puede: tupla_1.append(3)
#no se puede: tupla_2.remove("Juana")
#igual con .pop(), .insert(), .clear() etc.
#no se puede: del tupla_1[0]
#no se puede: tupla_1[0] = 5
del tupla_1 #sí se puede eliminar una tupla usando del
#print(tupla_1)

#los operadores son los mismos que en las listas
#se puede usar len()
print(len(tupla_2))

#además, las tuplas pueden aparecer en el lado izquierdo del operador de asignación

#podemos convertir una lista en una tupla con tuple() y una tupla en una lista con list()