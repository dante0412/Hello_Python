# conversion de moneda Asia
yuan = int(input('Cuanto te queda en yuan?'))
yen = int(input('Cuanto te queda en yen?'))
won = int(input('Cuanto te queda en won?'))

#yuan = 0.14
#yen = 0.0069
#won = 0.00071

total_dolares = (yuan * 0.14) + (yen * 0.0069) + (won * 0.00071)

print(total_dolares)