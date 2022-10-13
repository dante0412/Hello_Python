
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.


palabra1 = input('Ingrese primera palabra: ')
palabra1 = palabra1.lower()
palabra2 = input('Ingrese segunda palabra: ')
palabra2 = palabra2.lower()

def esAnagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

print(esAnagrama(palabra1, palabra2))
