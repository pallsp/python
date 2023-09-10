#hay dos tipos de errores principales a tener en cuenta
#código correcto pero alimentado de datos incorrectos, como por ejemplo que un programa espere recibir un entero pero el usuario introduzca una cadena
#código incorrecto o con efectos indeseados, denominados bugs
#aquí a estos errores los denominaremos excepciones

#n=input("Introduce un número positivo: ")
#if type(n) is int and n!=0:
   # print("Su inverso es:", 1/n)
#else:
    #print("Error. Vuelva a intentarlo de nuevo")

#esta es una posible solución, pero Python no la recomienda
#la solución es try-except

#try:
    #aquí se pone el codigo que es sospechoso de producir fallos
#except:
    #aqui se soluciona o capturan esos fallos

#el código del bloque except se ejecuta solo cuando se ha encontrado una excepcion dentro del bloque try
#cuando el bloque try o except se ejecutan con éxito, el control vuelve al proceso normal de ejecución y el programa sigue corriendo normal
try:
    n=int(input("Introduce un número positivo: "))
    print("Su inverso es:",1/n)
except:
    print("Hola. Ha habido un error")