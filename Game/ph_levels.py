#calificando el ph de un usuario

ph = int(input('Ingresu un valor entre 0 y 14 '))

if ph > 7:
    print('Básico')
elif ph < 7:
    print('Ácido')
else:
    print('Neutral')