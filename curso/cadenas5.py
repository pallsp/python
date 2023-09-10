#como hemos dicho, las cadenas son inmutables, no todo lo que podemos hacer con las listas lo podemos 
#hacer con las cadenas

#no se puede usar del en una cadena para eliminar un elemento de la misma, sólo para eliminarla entera
#las cadenas tampoco tienen un método append() ni insert()

#para añadir elementos usaremos la concatenacion
cadena='hola'
for i in range(3):
    cadena+='a'

print(cadena)

#sin embargo, hay otras funciones que sí pueden usarse como 
#min()- devuelve el elmento mínimo de una cadena (su valor ASCII)
#max()- devuelve el elmento mayor de una cadena (su valor ASCII)

#el método .index() busca desde el principio de una cadena el valor que pasamos por argumento
#y nos devolverá el índice del primer elemento encontrado que coincida
#de no estar causará una excepción ValueError

#la función list() nos permite transformar una cadena, que se pasa como argumento, en una lista de carácteres
#el método .count() cuenta todas las apariciones de un elemento dentro de la secuencia, la ausencia de 
#ese elemento no genera errores