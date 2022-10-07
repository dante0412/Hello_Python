# formula cuadratica con input

a = int(input('Ingrese el valor de a:'))
b = int(input('Ingrese el valor de b:'))
c = int(input('Ingrese el valor de c:'))

raizt1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
raizt2 = (-b - (((b ** 2) - 4 * a * c)) ** 0.5) / 2 * a

print(raizt1)
print(raizt2)