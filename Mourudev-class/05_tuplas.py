### Tuplas ###

from queue import PriorityQueue


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.80, 'Luis', 'Calderon')
my_other_tuple = (35, 60, 29)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count('Calderon')) #cuenta la cantidad de item especificado
print(my_tuple.index('Luis')) #ubicacion del primer indice encontrado en la tupla

# my_tuple[1] = 1.85 -- TypeError: 'tuple' object does not support item assignment
print(my_tuple)
#las tuplas son immutables

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[4:6])

#para modificar una tupla la coviertes en lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Dante0412"
my_tuple.insert(1,'Azul')
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) -- NameError: name 'my_tuple' is not defined

