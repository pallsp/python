#MÉTODOS DE CADENAS

#.capitalize() el primer carácter de la cadena lo convierte en mayúscula y el resto en minúsculas
print("hOla".capitalize())
#.center(num) centra la cadena agregando num/2 espacios antes y después de la cadena
#podemos pasarle otro argumento, que será el carácter con el que se rellenarán los espacios
print('['+'hola'.center(20)+']')

#.endswith() comprueba si la cadena termina con el argumento que le pasamos y devuelve True o False
#.startswith() comprueba si la cadena comienza con la subcadena especificada y devuelve True o False

#.find() similar a index(), devolverá un índice, pero más seguro, busca una subcadena y devuelve el índice del primer elemento encontrado de la subcadena
#si no lo encuentra devuelve -1, podemos indicarle la posición en la que empieza a buscar pasándole un segundo argumento con la posición
#e incluso podemos indicarle un tercer argumento que será el primer índice a partir del cuál no buscará
#.rfind() igual que .find() pero empieza a buscar desde el final de la cadena

#.isalnum() comprueba si la cadena contiene sólo carácteres alfanuméricos (True) o algo más (False)
print("hola".isalnum())
print("tengo 14 años".isalnum())
print("paco33".isalnum())
print("Buenos días, qué tal va todo?".isalnum())

#.isalpha() devuelve True si contiene sólo letras y False si contiene algo más (como espacios)
print("Soy pablo".isalpha())
print("asfjasasfasfgs".isalpha())
print("lucia342342".isalpha())

#.isdigit() devolverá True si sólo encuentra dígitos, y False para lo demás

#.islower() devolverá True si está todo en minúsculas y False si hay alguna mayúscula
#.isupper() devolverá True si está todo en mayúsculas y False si hay alguna minúscula
#.isspace() devovlerá True si sólo hay espacios en blanco y False si encuentra algún otro carácter

#.join() es un método que espera una lista de cadenas, de no ser todos los elementos cadenas generará un error TypeError
#todos los elementos de la lista será unidos en una sola cadena, pero que tendrá como elemento separador la cadena desde la que se 
#invoca al método 

print(",".join(["hola", "soy", "pablo"]))
print("-".join(["hola", "soy", "pablo"]))

#.lower() devuelve la cadena con todas sus letras en minúsculas

#.lstrip() devuelve la cadena sin espacios en blanco iniciales
print("            Hola buenos días".lstrip())
#le podemos pasar como argumento todos los carácteres que queremos que elimine también a parte de los espacios en blanco, es decir, eliminará
#todos los carácteres que le indiquemos en el argumento hasta que encuentre uno distinto
print("www.cisco.com".lstrip("w."))
#existe una variante conocida coo .rstrip(), que hace lo mismo pero afectando al lado derecho de la cadena
#.strip() combina los dos métodos anteriores y crea una nueva cadena sin los espacios en blanco iniciales y finales
print("  EEEE   ".strip())
#pero también funciona con otros carácteres
print("hghghghEEEEEEEEhghghghgh".strip("hg"))

#.replace() devuelve una copia de la cadena en la que todas las apariciones del primer argumento son reemplazadas por el segundo argumento
print("Me llamo Pablo".replace("e","icelio"))
#se le puede pasar un tercer argumento en el que indicamos el número de reemplazos
print("me le de se pe".replace("e","a", 3))

#.split() divide una cadena y crea una lista de todas las subcadenas detectadas
#el método asume que las subcadenas están delimitadas por espacios en blanco y no se copian 
print("hola buenos días".split())
#pero también podemos separar de forma arbitraria por el carácter que queramos, que no lo cogerá
print("hola buenos días".split("o"))

#.swapcase() crea una nueva cadena intercambiando las mayúsculas por minúsculas y viceversa

#.title() cambia la primera letra de cada palabra a mayúscula, y el resto las hace minúsculas. De cada palabra!!!!

#.upper() devuelve una copia de la cadena de origen en la que todas las minúsculas las hace mayúsculas