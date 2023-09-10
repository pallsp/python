#listas por comprensión

#de los 10 primeros cubos

cubos=[i**3 for i in range(1,11)]
cuadrados=[i**2 for i in range(1,11)]
impares=[i for i in cuadrados if i%2 !=0]
print(cubos)
print(cuadrados)
print(impares)