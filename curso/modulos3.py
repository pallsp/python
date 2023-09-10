#si importamos un modulo y no estamos conformes con el nombre del modulo en particular, podemos darle otro nombre, esto se llama 
#aliasing, y gracias a esto podremos identificar un modulo con un nombre diferente del original, también sirve para acortar los nombres originales
#la creacion de un alias se hace así:
import math as m
#después de esto, el nombre original del módulo se vuelve inaccesible, usaremos m 
#es igual cuando importamos una entidad concreta
from math import sin as seno, pi as PI #y se puede hacer tantas veces como queramos
