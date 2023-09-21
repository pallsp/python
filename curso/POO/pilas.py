#una pila es una estructura desarrollada para almacenar datos de una forma muy específica
#en inglés sus siglas son LIFO
#estas siglas representan su forma de comportarse: último en entrar-primero en salir
#last in-first out 

#una pila es un objeto con dos operaciones fundamentales, denominadas push (colocar un nuevo elemento en la parte superior) y 
#pop(retirar un elemento de la parte superior)
#se usan muy a menudo en muchos algoritmos clásicos



#definiremos una pila por medio del enfoque estructurado-procedimental

pila=[]

def push(valor):
    pila.append(valor)

def pop():
    val = pila[-1]
    del pila[-1]
    return val

#definiremos una pila por medio del enfoque orientado a objetos 

class Pila:
    def __init__(self):
        self.lista=[]

nueva_pila=Pila()
print(nueva_pila.lista)
