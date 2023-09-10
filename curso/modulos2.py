#también se puede importar directamente una entidad/entidades  
from math import pi,sin
#podremos acceder a estas entidades sin necesidad de utilizar un .
#no se importará ninguna otra entidad, unicamente las especificadas y no podremos utilizar el punto con el nombre del módulo para importar otra nueva
print(sin(pi/2)) #notar que ahora no ha hecho falta usar el math.
#otra forma de importar es importarlo todo de un módulo, que se hace así
from math import * #aquí importamos todo del módulo math