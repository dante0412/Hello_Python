# Variables
my_variable = 'My string variable'
print(my_variable)


#datos personales en variables
firt_name = 'Luis'
last_name = 'Calderon'
country = 'Perú'
city = 'Lima'
age = 26
is_married = False
skills = ['HTML', 'JAVA', 'Python']
person_info = {
    'firtsname' : 'Luis',
    'lastname' : 'Calderon',
    'country' : 'Perú',
    'city' : 'Lima' 
}

#concatenacion de variables en un print
print(firt_name, last_name, ',' , country, ',' , city, ',' ,age)
print(person_info)


#Algunas funciones del sistema
print(len(firt_name)) # "len "Cuanta la cantidad de caracteres

#variables en una sola linea
name, last, alias, age = 'Luis', 'Calderon', 'Dante', 26
print(name, last,'Mi edad es:', age, 'Mi alias es:', alias)

#solicitar datos con input
nombre = input('Como te llamas?')
edad = input('Cuantos años tienes?')

print(nombre)
print(edad)

