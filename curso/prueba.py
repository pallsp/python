lista=[3,1,-2]
print(lista[lista[-1]])

otra_lista=[1,2,3,4]
print(otra_lista[-3:-2])

vals=[0,1,2]
vals.insert(0,1)
del vals[1]
total=0
for i in vals:
    total+=i
print(total)
print(vals)

lista1=[1,2,3]
lista2=[]

for i in lista1:
    lista2.insert(0,i)
print(lista2)