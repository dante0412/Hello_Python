# Bola magica 8

import random

pregunta = input('Pregunta a la Bola Magica xD ... ')

res = random.randint(0,6)

if res == 0:
    print('Si')
elif res == 1:
    print('Sin duda')
elif res == 2:
    print('Intenta otra vez')
elif res == 3:
    print('No se, tu dimelo')
elif res == 4:
    print('Mejor no decirte ahora')
elif res == 5:
    print('Mis fuentes dicen k no')
elif res == 6:
    print('Definitivamente no')
else:
    print('Error')


#Otra solucion

# import random

# question = input("Question: ")

# random_number = random.randint(1, 9)
# # print(random_number)

# if random_number == 1:
#   answer = "Yes - definitely"
# elif random_number == 2:
#   answer = "It is decidedly so"
# elif random_number == 3:
#   answer = "Without a doubt"
# elif random_number == 4:
#   answer = "Reply hazy, try again"
# elif random_number == 5:
#   answer = "Ask again later"
# elif random_number == 6:
#   answer = "Better not tell you now"
# elif random_number == 7:
#   answer = "My sources say no"
# elif random_number == 8:
#   answer = "Outlook not so good"
# elif random_number == 9:
#   answer = "Very doubtful"
# else:
#   answer = "Error"

# print("Question:      " + question)
# print("Magic 8 Ball:  " + answer)


