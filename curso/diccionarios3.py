#un diccionario como tal no puede pasarse por un for 
#para ello utilizaremos un método: .keys(), que nos devuelve una lista con todas las claves del diccionario
#NOTA: PARECE QUE AHORA NO HACE FALTA USAR EL .keys()
dicc={
    "Matemáticas": 345,
    "Literatura": 389,
    "Química": 206,
    "Historia": 421
}

for i in dicc.keys():
    print(i)

#aunque realmente no hace falta explicitarlo

#for i in dicc:
    #print(i)

#aquí podríamos usar el .keys() pero lo omitimos por lo dicho antes
for i in dicc:
    print(i,"->",dicc[i])
#con el .items() obtenemos una tupla con la clave y el/los valores
for i in dicc.items():
    print(i)
#también 
for i,j in dicc.items():
    print(i,"->",j)