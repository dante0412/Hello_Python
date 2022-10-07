print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))


while pin != 1234:
    pin = int(input('PIN incorrecto. Ingresa tu PIN otra vez: '))

    if pin == 1234:
        print('PIN aceptado!')