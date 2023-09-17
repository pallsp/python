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

#podemos controlar varias excepciones a la vez con 

try:
    n=int(input("Introduce un número positivo: "))
    print("Su inverso es:", round(1/n,2))
except (ValueError, ZeroDivisionError):
    print("Ha sucedido algo, lo siento")

#con raise podemos generar la excepción exc de forma natural
#raise exc  

#con assert expression evaluamos la expresión, y si esta es True, un valor numérico distinto de cero, una cadena no vacía, o cualquier otro valor diferente de None
#no pasará nada, de lo contrario generará una excepción llamada AssertionError