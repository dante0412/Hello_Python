#adivina el numero

# guess = 0

# while guess !=6:
#     guess = (int(input('Adivina el numero: ')))

# print('Lo lograste')

#segundo ejercicio

numero = 0
intento = 0

print('~~~~~~Adivina el número~~~~~~~~')

while numero != 6 and intento < 3:
    numero = (int(input('Adivina el número: ')))
    intento += 1
    
if numero != 6:
    print('Te quedaste sin intentos')
else:
        print('Lo lograste')
