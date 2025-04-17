# Ejercicio 1 Sumar dos numeros y mostrar su resultado

# num1 = 2
# num2 = 2
# resultado = num1 + num2
# print("el resultado es:",resultado)

############################################################################################################33

# Ejercicio2: Calcula el area de un circulo con un radio dado
#  Formulapi x radio **2

# esta es mi primera solucion:
# Pi = 3.1416
# radio = 10JA Solar:
# Area_del_circulo = Pi*radio**2
# print(Area_del_circulo)

# Esta es otra solicuón llamando a la biblioteca math con la funcion import
# import math
# radio = 3
# Area_del_circulo = math.pi*radio**2
# print("el area es:", Area_del_circulo)


# ###############################################################################################################

# Ejercicio3: Concatena 2 cadenas de texto

# esta es mi pirmera forma de resolverlo , lo importante aquí es saber que se concatena con el + los textos

# cadena1 = "Mi libro"
# Cadena2 = "Luna de Plutón"
# print(cadena1+" "+Cadena2)

#Aquí es otra forna de reolverlo simplemente creé 3 variable que son las 2 cadenas mas otra variable que cancatena las dos frases 

# Cadena1 = "Mi libro "
# Cadena2 = "Luna de Plutón"
# Palabra_concatenada = Cadena1+ " "+ Cadena2
# print(Palabra_concatenada)

#######################################################################################################################

#Ejercicio 4: crea una lista con diferentes elementos e imprimela

# lo importante aqui es saber que las listas se crean con "[]" es una estructura de datos que puede almacenar múltiples valores en un 
# solo contenedor. Los elementos de una lista pueden ser de diferentes tipos (números, cadenas, booleanos, etc.), y se pueden modificar.

#esta es una lista con puros números
# Lista=[1,2,3,4,5,6,7,8,9,10]
# print(Lista)

#lista con puras palabras
# frutas = ["manzana", "pera", "uva"]
# print(frutas)

#lsita con diferentes tipos de valores (palabras, numeros, booleanos)
# mixta = [1, "hola", True, 3.5]
# print(mixta)

###############################################################################################################################
#Ejercicio 5 : relaizar una multiplicacion

# Num1 = 10
# Num2 = 2
# print(Num1*Num2)


###################################################################################################################################
# EJERCICOS ISRA
# este fue mi primer intento de diccionario pero me di cuenta que para que funcione el f string las skills deben de venir en una lista "[]""
# Student_dictonary = {

#     "first name": "omar",
#     "last name " :"Gonzalez",  
#     "Gender": "male",
#     "age": 25,
#     "marital status": "single",
#     "skills": "handsome" ", " "powerful" ", " "Harmonious",
#     "country": "Mexico",
#     "City": "Monterrey",
#     "Address": "South zone"
# }

# print(Student_dictonary)

Student_dictionary = {
    "first name": "Omar",
    "last name": "Gonzalez",  
    "Gender": "male",
    "age": 25,
    "marital status": "single",
    "skills": ["handsome", "powerful", "Harmonious"], 
    "country": "Mexico",
    "City": "Monterrey",
    "Address": "South zone"
}

del Student_dictionary["age"]
print(Student_dictionary)




#######################################################################################################################################
# Obtener las claves del diccionario como una lista 

# keys_list = list(Student_dictionary.keys())
# print("Lista de claves:", keys_list)




#################################################################################################################################
#btener el valor de skills y comprobar el tipo de dato, debe ser una lista 

# skills_value = Student_dictionary["skills"]

# if isinstance(skills_value, list):
#     print("El valor de 'skills' es una lista:", skills_value)
# else:
#     print("El valor de 'skills' NO es una lista.")

