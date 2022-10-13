# String

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)


my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)


my_scape_string = "\\tEste es un string \n escapado" #agregar una tabulacion xtra para ignorar un camando
print(my_scape_string)


#formateo

name, last, edad = 'Dante', 'Calderon', 26

print("Mi nombre es {} {} y mi edad es {}".format(name, last, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, last, edad))
print("Mi nombre es " + name + " " + last + " y mi edad es " + str(edad))
print(f"Mi nombre es {name} {last} y mi edad es {edad}")


# Desempaquetado de caracteres

language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

#Reverse

reversed_lenguage = language[::-1]
print(reversed_lenguage) #invierte una cadena

# Funciones

print(language.capitalize()) #pone en mayuscula la primera letra
print(language.upper()) #pone toda la cadena de texto en mayuscula
print(language.count("t")) #cuenta algo que se le pida
print(language.isnumeric()) #pregunta si la variable es un numero
print('1'.isnumeric())
print(language.lower()) #convierte toda la cadena en minuscula
print(language.upper().isupper()) #comprueba si la cadena esta en mayuscula
print(language.startswith("Py")) #comprueba si la cadena empieza con lo solicitado
