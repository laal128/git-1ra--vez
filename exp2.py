n=input('introdusca su nombre: ')
cct=int(input('introduca su cct: '))
t=int(input('introdusca su longevidad en el trabajo en años: '))
if cct==1:
    if t==1:
        print(n,' husted tiene derecho a 6 días de descanso')
    elif t>=2 and t<=6:
        print(n,' husted tiene derecho a 14 días de descanso')
    elif t>=7:
        print(n,' husted tiene derecho a 20 días de descanso')
elif cct==2:
    if t==1:
        print(n,' husted tiene derecho a 7 días de descanso')
    elif t>=2 and t<=6:
        print(n,' husted tiene derecho a 15 días de descanso')
    elif t>=7:
        print(n,' husted tiene derecho a 22 días de descanso')
elif cct==3:
    if t==1:
        print(n,' husted tiene derecho a 10 días de descanso')
    elif t>=2 and t<=6:
        print(n,' husted tiene derecho a 20 días de descanso')
    elif t>=7:
        print(n,' husted tiene derecho a 30 días de descanso')

print('esto es mi primer cambio')