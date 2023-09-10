#diccionario que almacene como clave nombres de alumnos y como valores sus calificaciones, al final mostrar el alumno y su promedio de nota

notas={} 
medias={}
nombre=input("Introduce un nombre:")
while nombre != "":
    if nombre in notas:
        lista=[]
        for i in notas[nombre]:
            lista.append(i)
        lista.append(float(input("Introduce una calificación:")))
        notas[nombre] = lista[:]
    else:
        lista=[float(input("Introduce una calificación:"))]
        notas[nombre] = lista[:]
    nombre=input("Introduce un nombre:")

for i in notas:
    media=0
    for j in notas[i]:
        media+=j
    media/=len(notas[i])
    medias[i]=round(media,2)

print(medias)
