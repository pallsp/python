#Cifrado César encriptado

print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))

texto=input("Introduce un mensaje: ")
cifrado = " "
control = True
while control: 
    try:
        cambio=int(input("Introduce un valor de cambio entre 1 y 25: "))
        while cambio < 1 or cambio >25:
            cambio=int(input("Introduce un valor de cambio entre 1 y 25: "))
        control = False
    except ValueError:
        print("Lo sentimos, pero eso no es un valor correcto")


for letra in texto:
    if not letra.isalpha():
        continue
    code = ord(letra)+cambio
    if code>=123:
        code = (code-123)+ord("a")
    elif code>=91 and letra.isupper():
        code = (code-91)+ord("A")

    cifrado+=chr(code)


print(cifrado)