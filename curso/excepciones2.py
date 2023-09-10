#podemos capturar varias excepciones a la vez
try:
    n=int(input("Introduce un número positivo: "))
    print("Su inverso es:", round(1/n,2))
except ValueError:
    print("Has introducido un valor no entero")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except:
    print("Ha sucedido algo, lo siento")

#este último except es la excepción por defecto, la más general y siempre se tiene que situar al final