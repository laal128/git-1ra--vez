#calcular todo incluido resto y divicion entera con menu de opciones y con una unica variable
n=int(input('Seleccione la operacion (0:suma, 1:resta, 2:multiplicacion, 3:divicion, 4:exponete, 5=resto)\n'))
if n==0:
    n+=float(input('ínserte el primer valor: '))
    n+=float(input('ínserte el segundo valor: '))
    print('El resultado es ',n)
elif n==1:
    n-=1
    n+=float(input('ínserte un valor: '))
    n-=float(input('ínserte un valor: '))
    print('El resultado es ',n)
elif n==2:
    n-=2
    n+=float(input('ínserte un valor: '))
    n*=float(input('ínserte un valor: '))
    print('El resultado es ',n)
elif n==3:
    n-=3
    n+=float(input('ínserte un valor: '))
    n/=float(input('ínserte un valor: '))
    print('El resultado es ',n)
elif n==4:
    n-=4
    n+=float(input('ínserte un valor: '))
    n**=float(input('ínserte un valor: '))
    print('El resultado es ',n)
elif n==5:
    n-=5
    n+=float(input('ínserte un valor: '))
    n%=float(input('ínserte un valor: '))
    print('El resultado es ',n)
else:
    print('Opcion no disponible')