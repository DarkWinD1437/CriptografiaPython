#Cifrado por sustitucion
##Transposicion por grupos
def cifrado_transposicion_grupos(mensaje, tam_grupo, permutacion):
    # Validar argumentos
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")
    if not isinstance(permutacion, list) or len(permutacion) != tam_grupo:
        raise ValueError("La permutación debe ser una lista con el mismo tamaño que el grupo.")

    # Dividir el mensaje en grupos
    grupos = []
    for i in range(0, len(mensaje), tam_grupo):
        grupo = mensaje[i:i + tam_grupo]
        if len(grupo) < tam_grupo:
            grupo += ' ' * (tam_grupo - len(grupo))  # Rellenar con espacios si el grupo es incompleto
        grupos.append(grupo)

    # Aplicar la permutación a cada grupo
    mensaje_cifrado = ""
    for grupo in grupos:
        grupo_cifrado = [grupo[i] for i in permutacion]
        mensaje_cifrado += "".join(grupo_cifrado)

    return mensaje_cifrado


def generar_permutacion_inversa(permutacion):
    permutacion_inversa = [0] * len(permutacion)
    for i, p in enumerate(permutacion):
        permutacion_inversa[p] = i
    return permutacion_inversa

def descifrado_transposicion_grupos(mensaje_cifrado, tam_grupo, permutacion):
    # Validar argumentos
    if not isinstance(mensaje_cifrado, str):
        raise TypeError("El mensaje cifrado debe ser una cadena de texto.")
    if not isinstance(tam_grupo, int) or tam_grupo <= 0:
        raise ValueError("El tamaño del grupo debe ser un entero positivo.")
    if not isinstance(permutacion, list) or len(permutacion) != tam_grupo:
        raise ValueError("La permutación debe ser una lista con el mismo tamaño que el grupo.")

    # Generar la permutación inversa
    permutacion_inversa = generar_permutacion_inversa(permutacion)

    # Agrupar el mensaje cifrado
    grupos_cifrados = []
    for i in range(0, len(mensaje_cifrado), tam_grupo):
        grupo_cifrado = mensaje_cifrado[i:i + tam_grupo]
        if len(grupo_cifrado) < tam_grupo:
            grupo_cifrado += ' ' * (tam_grupo - len(grupo_cifrado))  # Rellenar con espacios si el grupo es incompleto
        grupos_cifrados.append(grupo_cifrado)

    # Descifrar cada grupo
    mensaje_descifrado = ""
    for grupo_cifrado in grupos_cifrados:
        grupo_descifrado = [grupo_cifrado[permutacion_inversa[i]] for i in range(tam_grupo)]
        mensaje_descifrado += "".join(grupo_descifrado)

    return mensaje_descifrado.rstrip()  # Eliminar espacios al final del mensaje descifrado


def grupos():
    while True:
        print("\nBienvenido al Cifrado por Transposicion por grupos")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            # Cifrar mensaje
            mensaje = input("Ingrese el mensaje a cifrar: ")
            tam_grupo = int(input("Ingrese el tamaño del grupo: "))
            permutacion = [int(x) for x in input("Ingrese la permutación (separada por espacios): ").split()]

            mensaje_cifrado = cifrado_transposicion_grupos(mensaje, tam_grupo, permutacion)
            print(f"\nMensaje cifrado: {mensaje_cifrado}")

        elif opcion == 2:
            # Descifrar mensaje
            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            tam_grupo = int(input("Ingrese el tamaño del grupo: "))
            permutacion = [int(x) for x in input("Ingrese la permutación (separada por espacios): ").split()]

            mensaje_descifrado = descifrado_transposicion_grupos(mensaje_cifrado, tam_grupo, permutacion)
            print(f"\nMensaje descifrado: {mensaje_descifrado}")

        elif opcion == 3:
            # Salir
            print("\n¡Saliendo del programa!")
            break

        else:
            # Opción inválida
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    grupos()

##Fin de Transposicion por grupos

##Cifrado de doble transposicion por columnas
def cifrar_doble_transposicion(mensaje, clave1, clave2):
    texto_cifrado_ronda1 = cifrar_transposicion_columnar(mensaje, clave1)
    texto_cifrado_final = cifrar_transposicion_columnar(texto_cifrado_ronda1, clave2)
    return texto_cifrado_final

def cifrar_transposicion_columnar(texto, clave):
    longitud_texto = len(texto)
    numero_columnas = len(clave)
    numero_filas = (longitud_texto + numero_columnas - 1) // numero_columnas

    # Rellenar la tabla con caracteres 'X'
    tabla = [['X' for _ in range(numero_columnas)] for _ in range(numero_filas)]

    # Insertar el texto en la tabla por columnas según la clave
    for i, c in enumerate(texto):
        fila = i // numero_columnas
        columna = clave[i % numero_columnas] - 1  # Restar 1 para convertir de 1-indexado a 0-indexado
        if fila < numero_filas and columna < numero_columnas:
            tabla[fila][columna] = c

    # Leer el texto cifrado de la tabla reorganizada
    texto_cifrado = ''.join(''.join(fila) for fila in tabla)

    return texto_cifrado.rstrip('X')  # Eliminar los caracteres 'X' adicionales al final

def descifrar_doble_transposicion(texto_cifrado, clave1, clave2):
    texto_descifrado_ronda1 = descifrar_transposicion_columnar(texto_cifrado, clave2)
    mensaje_descifrado = descifrar_transposicion_columnar(texto_descifrado_ronda1, clave1)
    return mensaje_descifrado

def descifrar_transposicion_columnar(texto_cifrado, clave):
    longitud_texto = len(texto_cifrado)
    numero_columnas = len(clave)
    numero_filas = (longitud_texto + numero_columnas - 1) // numero_columnas

    # Calcular el número de caracteres en cada columna
    num_chars_per_column = [numero_filas] * numero_columnas
    for i in range(longitud_texto % numero_columnas):
        num_chars_per_column[-(i + 1)] -= 1

    # Crear una lista vacía para las columnas
    columnas = ['' for _ in range(numero_columnas)]
    indice_texto = 0
    for i, col_len in enumerate(num_chars_per_column):
        columnas[i] = texto_cifrado[indice_texto:indice_texto + col_len]
        indice_texto += col_len

    # Reorganizar las columnas según la clave
    clave_invertida = sorted(range(len(clave)), key=lambda k: clave[k])
    tabla = [['' for _ in range(numero_columnas)] for _ in range(numero_filas)]
    for i, columna in enumerate(clave_invertida):
        for fila in range(len(columnas[i])):
            tabla[fila][columna] = columnas[i][fila]

    # Leer el texto descifrado de la tabla
    texto_descifrado = ''.join(''.join(fila) for fila in tabla).rstrip('X')

    return texto_descifrado

def columnas():
    while True:
        print("\nBienvenido al Cifrado de doble transposicion por columnas")
        print("\nMenú:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje que desea cifrar: ")
            print("la cantidad de digitos para la clave tiene que ser igual a la cantidad de letras que el mensaje")
            clave1 = list(map(int, input("Ingrese la clave de cifrado para la primera ronda (separada por espacios): ").split()))
            print("tambien los digitos deben pertenecer del mismo grupo que la clave anterior pero de diferente mezcla")
            clave2 = list(map(int, input("Ingrese la clave de cifrado para la segunda ronda (separada por espacios): ").split()))

            texto_cifrado = cifrar_doble_transposicion(mensaje, clave1, clave2)
            print("Texto cifrado:", texto_cifrado)

        elif opcion == "2":
            texto_cifrado = input("Ingrese el texto cifrado que desea descifrar: ")
            print("ocupar las mismas claves que uso para el cifrado")
            clave1 = list(map(int, input("Ingrese la clave de cifrado para la primera ronda (separada por espacios): ").split()))
            clave2 = list(map(int, input("Ingrese la clave de cifrado para la segunda ronda (separada por espacios): ").split()))

            mensaje_descifrado = descifrar_doble_transposicion(texto_cifrado, clave1, clave2)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    columnas()

##fin de cifrado de doble transposicion por columnas

##Cifrado de transposicion por filas
import math

def calcular_num_filas(mensaje):
    mensaje_sin_espacios = mensaje.replace(" ", "").upper()
    longitud = len(mensaje_sin_espacios)

    # Encuentra el número más cercano al cuadrado de la longitud que es un número entero
    num_filas = math.ceil(math.sqrt(longitud))
    return num_filas

def cifrado_transposicion_filas(mensaje, clave_reordenamiento):
    # Eliminar espacios en blanco y convertir a mayúsculas
    mensaje_sin_espacios = mensaje.replace(" ", "").upper()

    # Calcular el número de columnas y filas
    num_columnas = len(clave_reordenamiento)
    num_filas = -(-len(mensaje_sin_espacios) // num_columnas)  # Redondear hacia arriba

    # Crear la tabla y rellenarla con el mensaje
    tabla = [['' for _ in range(num_columnas)] for _ in range(num_filas)]
    for i, letra in enumerate(mensaje_sin_espacios):
        fila = i // num_columnas
        columna = i % num_columnas
        tabla[fila][columna] = letra

    # Reordenar las filas según la clave
    clave_reordenamiento = [i for i in clave_reordenamiento if i < num_filas]
    tabla_reordenada = [None] * num_filas
    for i, fila_idx in enumerate(clave_reordenamiento):
        if fila_idx < num_filas:
            tabla_reordenada[i] = tabla[fila_idx]

    # Leer el texto cifrado de izquierda a derecha
    texto_cifrado = ""
    for columna in range(num_columnas):
        for fila in range(num_filas):
            if tabla_reordenada[fila][columna]:
                texto_cifrado += tabla_reordenada[fila][columna]

    return texto_cifrado

def descifrado_transposicion_filas(texto_cifrado, clave_reordenamiento):
    # Calcular el número de filas y columnas
    num_columnas = len(clave_reordenamiento)
    num_filas = -(-len(texto_cifrado) // num_columnas)  # Redondear hacia arriba

    # Crear una tabla vacía
    tabla = [['' for _ in range(num_columnas)] for _ in range(num_filas)]

    # Ajustar la clave de reordenamiento para que sea un índice válido (base 0)
    clave_reordenamiento = [i for i in clave_reordenamiento if i < num_filas]

    # Llenar la tabla con el texto cifrado
    contador = 0
    for columna in range(num_columnas):
        for fila_idx in clave_reordenamiento:
            if contador < len(texto_cifrado):
                tabla[fila_idx][columna] = texto_cifrado[contador]
                contador += 1

    # Leer el mensaje original de izquierda a derecha
    mensaje_descifrado = ""
    for fila in range(num_filas):
        for columna in range(num_columnas):
            if tabla[fila][columna]:
                mensaje_descifrado += tabla[fila][columna]

    return mensaje_descifrado

def filas():
    while True:
        print("\nBienvenido a la transposicion por filas")
        print("\nOpciones:")
        print("1. Calcular primero el número de filas")
        print("2. Cifrar mensaje")
        print("3. Descifrar mensaje")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje para calcular el número de filas: ")
            num_filas = calcular_num_filas(mensaje)
            print("El número recomendado de filas es:", num_filas)

        elif opcion == "2":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            clave_reordenamiento = [int(numero) for numero in input("Ingrese la clave de reordenamiento (separada por espacios): ").split()]

            texto_cifrado = cifrado_transposicion_filas(mensaje, clave_reordenamiento)
            print("Texto cifrado:", texto_cifrado)

        elif opcion == "3":
            texto_cifrado = input("Ingrese el texto cifrado a descifrar: ")
            clave_reordenamiento = [int(numero) for numero in input("Ingrese la clave de reordenamiento (separada por espacios): ").split()]

            mensaje_descifrado = descifrado_transposicion_filas(texto_cifrado, clave_reordenamiento)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    filas()

##fin de Cifrado de transposicion por filas
#Fin de cifrado por sustitucion

#Funcion principal de Cifrador por sustitucion
def main():
    while True:
        print("\nBienvenido a Cifrador por Sustitucion")
        # Menú principal
        print("\nOpciones:")
        print("1. Transposicion por grupos")
        print("2. Cifrador de doble transposicion por columnas")
        print("3. Transposicion por filas")
        print("4. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            grupos()

        elif opcion == "2":
            columnas()

        elif opcion == "3":
            filas()

        # Agrega el resto de las opciones aquí
        elif opcion == "4":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
#Fin de Funcion principal de Cifrador por sustitucion