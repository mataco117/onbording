# # from utils.helper import multiply
# # print (multiply(5,3))

# import pandas as pd

# # Leer el archivo CSV
# df = pd.read_csv("data/data.csv")

# # Mostrar las primeras filas
# print(df.head())

# a = [1, 3, 2]

# def order_list(a):
#     for index in range(len(a)-1):
#         # print(a[index],a[index+1])
#         if a[index] > a[index + 1]:
#             continue
#         else:
#             a[index] = a[index+1]

# order_list(a)

##########################################################################################################

#quicksort 
# def quicksort(lista, nivel=0):
#     # Indentación para visualizar niveles de recursión
#     indent = "  " * nivel  

#     # Caso base: lista vacía o con un solo elemento
#     if len(lista) <= 1:
#         print(f"{indent}Retornando lista base: {lista}")
#         return lista

#     # Elegimos el pivote del medio
#     pivote = lista[len(lista) // 2]
#     print(f"{indent}Lista actual: {lista}")
#     print(f"{indent}Pivote elegido: {pivote}")

#     # Dividimos la lista
#     menores = [x for x in lista if x < pivote]
#     iguales = [x for x in lista if x == pivote]
#     mayores = [x for x in lista if x > pivote]

#     print(f"{indent}Menores: {menores}")
#     print(f"{indent}Iguales: {iguales}")
#     print(f"{indent}Mayores: {mayores}\n")

#     # Recursión para cada parte

#     return quicksort(menores, nivel + 1) + iguales + quicksort(mayores, nivel + 1)


# # 🔢 Lista ordenada de ejemplo
# lista = [1, 2, 3, 4, 5, 6, 7]

# # 🔍 Ejecutar y ver el proceso
# print("Ordenando con QuickSort (pivote del medio):\n")
# resultado = quicksort(lista)

# # ✅ Mostrar resultado final
# print("\nResultado final ordenado:", resultado)
# ##################################################################################################################

import requests

api_key = "e717aa7b50f6c32f42a796df8a87b207"
ciudad = "Monterrey"
pais = "MX" 

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric&lang=es"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Clima actual en {ciudad}, México:")
    print(f"Temperatura: {data['main']['temp']}°C")
    # print(f"Sensación térmica: {data['main']['feels_like']}°C")
    print(f"Descripción: {data['weather'][0]['description'].capitalize()}")
    print(f"Humedad: {data['main']['humidity']}%")
    # print(f"Viento: {data['wind']['speed']} m/s")
else:
    print("Error al obtener los datos:", response.status_code)
