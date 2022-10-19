### Sets ###

my_set = set()
my_other_set = {}  #al estar vacio, inicialmente es un diccionario

print(type(my_set))  
print(type(my_other_set)) 

my_other_set = {'Luis', 'Calderon', 35}  #Al llenar los datos se vuelve un set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Dante") #agrega elementos 
print(my_other_set) #No es una estructura ordenada

my_other_set.add("Dante") # Un set no admite repetidos
print(my_other_set) 

print('Calderon' in my_other_set) #comprobas si un elemento existe dentro de un set
print('Camaron' in my_other_set)

my_other_set.remove('Calderon')
print(my_other_set)

my_other_set.clear() #elimina los elementos de la variable
print(my_other_set)

del my_other_set #elimina toda la variable
#print(my_other_set) #NameError: name 'my_other_set' is not defined

my_set = {'Luis', 'Calderon', 35}
my_list = list(my_set) #no se recomienda porque no tiene un orden claro
print(my_list)
print(my_list[0])

my_other_set = {'Python', 'HTML', 'CSS'}

my_new_set = my_set.union(my_other_set) #une 1 o mas sets en 1
print(my_new_set.union({'Java', 'C#'}))

print(my_new_set.difference(my_set))