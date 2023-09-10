#operador igual ==
#operador no igual !=
#operador mayor y menor > <
#operador mayor o igual que y menor o igual que >= <=
n1 = int(input("Introduce un número: "))

if n1>=10: 
    #print("El número", n1,"es mayor o igual que 10")
    if n1 ==10:
        print("El número", n1,"es exactamente 10")
    else:
        print("El número",n1,"es mayor estricto que 10")
else:
    print("El número", n1,"es menor estricto que 10")


n2=int(input("Introduce otro número: "))

if n2>100:
    print("El número es muy grande")
elif n2<=100 and n2>75:
    print("El número es grande")
elif n2<=75 and n2>20:
    print("El número es normalillo")
else:
    print("El número es pequeño")