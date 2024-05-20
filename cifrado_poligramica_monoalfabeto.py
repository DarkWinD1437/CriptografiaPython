#Cifrado por sustitucion poligamica monoalfabeto

##Cifrado de Playfair
def generar_tabla(clave):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' está excluida
    tabla = []
    caracteres_usados = set()

    for char in clave.upper():
        if char not in caracteres_usados and char in alfabeto:
            tabla.append(char)
            caracteres_usados.add(char)

    for char in alfabeto:
        if char not in caracteres_usados:
            tabla.append(char)

    return [tabla[i:i + 5] for i in range(0, 25, 5)]


def preparar_texto(texto, para_cifrado=True):
    texto = texto.upper().replace("J", "I").replace(" ", "")
    preparado = ""
    i = 0

    while i < len(texto):
        preparado += texto[i]
        if para_cifrado:
            if i + 1 < len(texto) and texto[i] == texto[i + 1]:
                preparado += "X"
            elif i + 1 < len(texto):
                preparado += texto[i + 1]
                i += 1
            else:
                preparado += "X"
        i += 1

    return preparado

def encontrar_posicion(tabla, caracter):
    for fila in range(5):
        for col in range(5):
            if tabla[fila][col] == caracter:
                return fila, col
    return None

def cifrar_par(tabla, caracter1, caracter2):
    fila1, col1 = encontrar_posicion(tabla, caracter1)
    fila2, col2 = encontrar_posicion(tabla, caracter2)

    if fila1 == fila2:
        return tabla[fila1][(col1 + 1) % 5] + tabla[fila2][(col2 + 1) % 5]
    elif col1 == col2:
        return tabla[(fila1 + 1) % 5][col1] + tabla[(fila2 + 1) % 5][col2]
    else:
        return tabla[fila1][col2] + tabla[fila2][col1]

def descifrar_par(tabla, caracter1, caracter2):
    fila1, col1 = encontrar_posicion(tabla, caracter1)
    fila2, col2 = encontrar_posicion(tabla, caracter2)

    if fila1 == fila2:
        return tabla[fila1][(col1 - 1) % 5] + tabla[fila2][(col2 - 1) % 5]
    elif col1 == col2:
        return tabla[(fila1 - 1) % 5][col1] + tabla[(fila2 - 1) % 5][col2]
    else:
        return tabla[fila1][col2] + tabla[fila2][col1]

def cifrar(texto, clave):
    tabla = generar_tabla(clave)
    texto_preparado = preparar_texto(texto)
    texto_cifrado = ""

    for i in range(0, len(texto_preparado), 2):
        texto_cifrado += cifrar_par(tabla, texto_preparado[i], texto_preparado[i + 1])

    return texto_cifrado

def descifrar(texto, clave):
    tabla = generar_tabla(clave)
    texto_descifrado = ""

    for i in range(0, len(texto), 2):
        texto_descifrado += descifrar_par(tabla, texto[i], texto[i + 1])

    return texto_descifrado

def playfair():
    while True:
        print("\nBienvenido al Cifrado de Playfair")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            clave = input("Introduce la clave: ").strip().upper()
            clave = clave.replace("J", "I")
            clave = ''.join(sorted(set(clave), key=clave.index))

            mensaje = input("Ingrese el mensaje a cifrar: ")
            mensaje_cifrado = cifrar(mensaje, clave)
            print("Mensaje cifrado:", mensaje_cifrado)

        elif opcion == "2":
            clave = input("Introduce la clave: ").strip().upper()
            clave = clave.replace("J", "I")
            clave = ''.join(sorted(set(clave), key=clave.index))

            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            mensaje_descifrado = descifrar(mensaje_cifrado, clave)
            print("Mensaje descifrado:", mensaje_descifrado)
            print("\nRecordar que si el mensaje descifrado es diferente que el original ")
            print("es porque en la logica de Playfair se evita el uso de J y se sustituye por la i")
            print("tambien si el tamaño del mensaje descifrado es pequeño o diferente al original, se añadira 'X' para rellenar")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    playfair()

##Fin de Cifrado de Playfair

##Cifrado de Hill

#importamos la libreria numpy - pip install numpy
import numpy

def inversa_modular_matriz(matriz, modulo):
    # Calcular el determinante de la matriz
    det = int(round(numpy.linalg.det(matriz)))
    # Calcular la inversa modular del determinante
    det_inv = pow(det, -1, modulo)
    # Calcular la matriz adjunta (cofactor) y luego la transpuesta
    matriz_adjunta = numpy.round(numpy.linalg.inv(matriz) * det).astype(int)
    matriz_inversa_modular = (det_inv * matriz_adjunta) % modulo
    return matriz_inversa_modular

def cifrado_hill(mensaje, matriz):
    # Convertir el mensaje a bloques de tamaño n
    n = len(matriz)
    mensaje = mensaje.upper()
    bloques = []
    for i in range(0, len(mensaje), n):
        bloque = mensaje[i:i+n]
        if len(bloque) < n:
            bloque += 'X' * (n - len(bloque))  # Rellenar con 'X' si el bloque es incompleto
        bloques.append(bloque)

    # Cifrar cada bloque
    mensaje_cifrado = ""
    for bloque in bloques:
        bloque_numerico = [ord(letra) - ord('A') for letra in bloque]
        cifrado_numerico = numpy.dot(matriz, bloque_numerico) % 26
        bloque_cifrado = ''.join(chr(num + ord('A')) for num in cifrado_numerico)
        mensaje_cifrado += bloque_cifrado

    return mensaje_cifrado

def descifrado_hill(mensaje_cifrado, matriz_inversa):
    # Convertir el mensaje cifrado a bloques de tamaño n
    n = len(matriz_inversa)
    bloques = []
    for i in range(0, len(mensaje_cifrado), n):
        bloque = mensaje_cifrado[i:i+n]
        bloques.append(bloque)

    # Descifrar cada bloque
    mensaje_descifrado = ""
    for bloque in bloques:
        bloque_numerico = [ord(letra) - ord('A') for letra in bloque]
        descifrado_numerico = numpy.dot(matriz_inversa, bloque_numerico) % 26
        bloque_descifrado = ''.join(chr(num + ord('A')) for num in descifrado_numerico)
        mensaje_descifrado += bloque_descifrado

    return mensaje_descifrado

def hill():
    while True:
        print("\nBienvenido al Cifrado de Hill")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            matriz_str = input("Ingrese la matriz de cifrado (separando filas por comas y elementos de cada fila por espacios): ")
            matriz = numpy.array([[int(numero) for numero in fila.split()] for fila in matriz_str.split(",")])

            mensaje = input("Ingrese el mensaje a cifrar: ")
            mensaje_cifrado = cifrado_hill(mensaje, matriz)
            print("Mensaje cifrado:", mensaje_cifrado)

        elif opcion == "2":
            matriz_str = input("Ingrese la matriz de cifrado (separando filas por comas y elementos de cada fila por espacios): ")
            matriz = numpy.array([[int(numero) for numero in fila.split()] for fila in matriz_str.split(",")])

            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            try:
                matriz_inversa = inversa_modular_matriz(matriz, 26)
            except numpy.linalg.LinAlgError:
                print("La matriz de cifrado no es invertible. Por favor, ingrese una matriz válida.")
                continue
            mensaje_descifrado = descifrado_hill(mensaje_cifrado, matriz_inversa)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    hill()

##Fin de Cifrado de Hill

#Fin de Cifrado por sustitucion poligamica monoalfabeto

#Funcion principal de cifrado poligramica monoalfabeto
def main():
    while True:
        print("\nBienvenido al Cifrador por sustitucion poligramica monoalfabeto")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrador Playfair")
        print("2. Cifrador de Hill")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            playfair()

        elif opcion == "2":
            hill()

        # Agrega el resto de las opciones aquí
        elif opcion == "3":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
#Fin de Funcion principal de cifrado poligramica monoalfabeto