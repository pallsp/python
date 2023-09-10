#a partir de un año y un mes obtener los días
def days(anyo, mes):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        return 31
    elif mes==4 or mes==6 or mes==9 or mes==11:
        return 30
    else: 
        if anyo%4==0 and anyo%100==0:
            if anyo%400==0: return 29
            else: return 28 
        elif anyo%4==0: return 29
        else: return 28 

anyo=0
mes=0 
while anyo<=0:
    anyo=int(input("Introduce un año: "))
while mes<=0 or mes>12:
    mes=int(input("Introduce un mes: "))

print("El número de días es:",days(anyo,mes))