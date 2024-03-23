#solicitar 3 numeros enteros y mostar cual numero es más grande
x=int(input('Inserte el 1er valor: '))
y=int(input('Inserte el 2do valor: '))
z=int(input('Inserte el 3er valor: '))
if x>y and x>z:
    print('El numero más grande es ',x)
elif y>x and y>z:
    print('El numero más grande es ',y)
elif z>x and z>y:
    print('El numero más grande es',z)