#break y continue
print()
print("La instrucción break")
print()
for i in range(6):
    if i==3:
        break
    print("El valor de i es:",i)
print()
print("La instrucción continue")
print()
for i in range(6):
    if i==3:
        continue
    print("El valor de i es:",i)