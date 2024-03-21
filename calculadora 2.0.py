x=float(input('Inserte el primer valor: '))
y=float(input('Inserte el segundo valor: '))
z=int(input('''Inserte un valor de la lista:
0=suma
1=resta
2=multiplicacion
3=divicion
4=exponente
'''))
if z==0:
    print('El resultado es ',x+y)
elif z==1:
    print('El resultado es ',x-y)
elif z==2:
    print('El resultado es ',x*y)
elif z==3:
    print('El resultado es ',x/y)
elif z==4:
    print('El resultado es ',x**y)
else:
    print('Opcion no disponible')