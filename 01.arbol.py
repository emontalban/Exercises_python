# Este programa genera un patrón visual basado en números binarios.
# Convierte el número actual a binario y reemplaza los 1 por '*'
# y los 0 por espacios para formar un dibujo.
# En cada iteración se usa una operación XOR con desplazamiento
# de bits (x ^= x << 1) para generar la siguiente fila del patrón.

x=1
size=8
for i in range(size):
    print((' ' * (size -i)) + bin (x)[2:]
    .replace ('0' , '  ').replace('1', ' *'))
    x ^= x << 1


