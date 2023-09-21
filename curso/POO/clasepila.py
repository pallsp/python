#clase pila con sus atributos y métodos

class Pila:
    def __init__(self):
        self.__lista=[]
    
    def push(self,valor):
        self.__lista.append(valor)
    
    def pop(self):
        val = self.__lista[-1]
        del self.__lista[-1]
        return val

#una subclase

class AddingPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__suma=0
    def push(self, valor):
        self.__suma+=valor
        Pila.push(self,valor)
    def pop(self):
        val= Pila.pop(self)
        self.__suma-=val
        return val
    def get_suma(self):
        return self.__suma