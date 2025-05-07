# Diccionario para guardar estudiantes
estudiantes = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

# Bucle principal del programa
while True:
    mostrar_menu()  # Llama a la función que muestra el menú
    opcion = input("Elige una opción: ")  # Espera a que el usuario escriba algo

    if opcion == "1":
        # Aquí irá el código para agregar estudiante
        pass
    elif opcion == "2":
        # Aquí irá el código para mostrar estudiantes
        pass
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Sale del bucle y termina el programa
    else:
        print("Opción no válida. Intenta de nuevo.")
