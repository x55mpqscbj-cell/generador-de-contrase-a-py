import string
minusculas = string.ascii_lowercase
masyusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation
print(minusculas )
print(masyusculas)
print(numeros)
print(simbolos)
import random
longitud =15
todos_los_caracteres = minusculas + masyusculas + numeros + simbolos
contraseña = ''.join(random.choices(todos_los_caracteres, k=longitud))
print(contraseña) 
