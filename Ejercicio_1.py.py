import sys

print(sys.argv)
operacion1 = int(sys.argv[1]) % 2
operacion2 = int(sys.argv[2]) % 2
operacion3 = int(sys.argv[3]) % 2

if operacion1 == 0:
    print("el primer valor es multiplo de 2")
else:
    print("el primer valor no es multiplo de 2")

if operacion2 == 0:
    print("el segundo valor es multiplo de 2")
else:
    print("el segundo valor no es multiplo de 2")

if operacion3 == 0:
    print("el tercer valor es multiplo de 2")
else:
    print("el tercer valor no es multiplo de 2")
