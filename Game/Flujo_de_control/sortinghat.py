#Sombrero seleccionador de Hadward

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("============================")
print("   Sombrero Seleccionador   ")
print("============================")

#~~~~~~~~~~~~pregunta 1~~~~~~~~~~~~
print('Pregunta 1')
pregunta1 = 'Cual te gusta mas?'
a1 = '1. Dragon Ball'
b1 = '2. Naruto'

print(pregunta1)
print(a1)
print(b1)

answer1 = int(input('respuesta (1-2): '))

if answer1 == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif answer1 == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print('Entrada incorrecta')
print(' ')
#~~~~~~~~~~~~pregunta 2~~~~~~~~~~~~
print('Pregunta 2')
pregunta2 = 'Cuando mueras. Como quieres que te recuerde la gente?'
a2 = '1. Buena persona'
b2 = '2. Gran persona'
c2 = '3. El audaz'
d2 = '4. El Sabio'

print(pregunta2)
print(a2)
print(b2)
print(c2)
print(d2)

answer2 = int(input('respuesta (1-4): '))

if answer2 == 1:
    Hufflepuff = Hufflepuff + 1
elif answer2 == 2:
    Slytherin = Slytherin + 1
elif answer2 == 3:
    Ravenclaw = Ravenclaw + 1
elif answer2 == 4:
    Gryffindor = Gryffindor + 1
else:
    print('Entrada incorrecta')
print(' ')
#~~~~~~~~~~~~pregunta 3~~~~~~~~~~~~
print('Pregunta 3')
pregunta3 = 'Qué tipo de musica te gusta?'
a3 = '1. Rap'
b3 = '2. Bachata'
c3 = '3. Pop'
d3 = '4. Cumbia'

print(pregunta3)
print(a3)
print(b3)
print(c3)
print(d3)

answer3 = int(input('respuesta (1-4): '))

if answer3 == 1:
    Slytherin = Slytherin + 1
elif answer3 == 2:
    Hufflepuff = Hufflepuff + 1
elif answer3 == 3:
    Ravenclaw = Ravenclaw + 1
elif answer3 == 4:
    Gryffindor = Gryffindor + 1
else:
    print('Entrada incorrecta')

print(' ')
print('----------------Puntaje final--------------')
print('Gryffindor: ' , Gryffindor)
print('Ravenclaw: ' , Ravenclaw)
print('Hufflepuff: ' , Hufflepuff)
print('Slytherin: ' , Slytherin)
print(' ')
if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print("Ganador: 🦁 Gryffindor!")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print("Ganador: 🦅 Ravenclaw!")
elif Hufflepuff >= Slytherin:
    print("Ganador: 🦡 Hufflepuff!")
else:
    print("Ganador: 🐍 Slytherin!")