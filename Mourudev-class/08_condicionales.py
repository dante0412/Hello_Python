### Condicionales ###

my_condition = False

if my_condition: # es lo mismo que if my_condition == True
    print("Se ejecuta la condicion del if")

my_condition = 5 * 3

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condicion del tercer if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print('Es igual a 25')
else:
    print("Es menor o igual que 10 o mayor que 20 o distinto de 25")


print("La ejecución continua")

my_string = 'Mi cadena de texto'

if my_string:
    print('Mi cadena de texto no es vacia')


if my_string == "Mi cadena de textooo":
    print('Estas cadenas de texto coinciden')
    
my_string = ''
if not my_string:
    print('Mi cadena de texto es vacia')

