#ordenamiento burbuja caso ascendente (de menor a mayor)
lista=[4,15,1,2,-5]

swapped= True #variable que controla los intercambios

while swapped:
    swapped=False

    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]: 
            swapped=True
            lista[i],lista[i+1] = lista[i+1],lista[i]


print(lista)
