import sys

nombre = sys.argv[1]
manejar = open(nombre, 'r')
texto = manejar.read()
print(nombre, 'es de', len(texto), 'bytes')
