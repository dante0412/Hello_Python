### Diccionarios ###

#Almacena datos de tipo clave - valor
from operator import le


my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Luis', 'Apellido':'Calderon', 'Edad':35, 1:'Python'}
my_dict = {
    'Nombre':'Luis',
    'Apellido':'Calderon',
    'Edad':35, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.77
    }

print(my_dict)
print(my_other_dict)
print(type(my_other_dict))

print(len(my_dict))
print(len(my_other_dict))

my_dict['Nombre'] = 'Dante' #actualizar datos
print(my_dict['Nombre'])
print(my_dict['Lenguajes'])

my_dict['Calle'] = 'Calle Calderon' #Insertar nuevo clave - valor
print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Nombre' in my_dict) # Ubica el nombre del campo mas no el valor
print('Calderon' in my_dict)
print('Camaron' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dict = dict.fromkeys(('Nombre',1,'Piso'))
print(my_new_dict)

