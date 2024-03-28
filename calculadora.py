x=float(input('Inserte el primer valor: '))
y=float(input('Inserte el segundo valor: '))
a=int(input('Inserte un valor de la lista: (0:suma, 1:resta, 2:multiplicacion, 3=:divicion, 4:exponente, 5:resto)\n'))
if a==0:
    print('El resultado es',x+y)
elif a==1:
    print('El resultado es',x-y)
elif a==2:
    print('El resultado es',x*y)
elif a==3:
    print('El resultado es',x/y)
elif a==4:
    print('El resultado es',x**y)
elif a==5:
    print('El resultado es',x%y)