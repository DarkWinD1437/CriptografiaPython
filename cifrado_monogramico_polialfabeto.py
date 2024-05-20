import random
import base64
import secrets

#Cifrado por sustitucion monogramico polialfabeto
##polialfabeticos periodicos
###Cifrado autoclave
def cifrado_autoclave(mensaje, clave):
    mensaje_cifrado = ""
    for i, letra in enumerate(mensaje):
        shift = ord(clave[i % len(clave)])
        cifrado = (ord(letra) + shift - 32) % (126 - 32) + 32
        mensaje_cifrado += chr(cifrado)
    return mensaje_cifrado

def descifrado_autoclave(mensaje_cifrado, clave):
    mensaje_descifrado = ""
    for i, letra_cifrada in enumerate(mensaje_cifrado):
        shift = ord(clave[i % len(clave)])
        descifrado = (ord(letra_cifrada) - shift - 32) % (126 - 32) + 32
        mensaje_descifrado += chr(descifrado)
    return mensaje_descifrado

def autoclave():
    while True:
        print("\nBienvenido al Cifrado de Autoclave")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje que desea cifrar: ")
            clave = input("Ingrese la clave secreta: ")
            mensaje_cifrado = cifrado_autoclave(mensaje, clave)
            print("Mensaje cifrado:", mensaje_cifrado)

        elif opcion == "2":
            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            clave = input("Ingrese la clave secreta: ")
            mensaje_descifrado = descifrado_autoclave(mensaje_cifrado, clave)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    autoclave()

###Fin de cifrado autoclave

###Cifrado beaufort
def cifrado_beaufort(mensaje, alfabeto_mayusculas="ZYXWVUTSRQPONMLKJHGFEDCBA", alfabeto_minusculas="zyxwvutsrqponmlkjihgfedcba"):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isupper():
            indice_letra = ord(letra) - ord('A')
            letra_cifrada = alfabeto_mayusculas[indice_letra]
        else:
            indice_letra = ord(letra) - ord('a')
            letra_cifrada = alfabeto_minusculas[indice_letra]
        mensaje_cifrado += letra_cifrada
    return mensaje_cifrado

def descifrado_beaufort(mensaje_cifrado, alfabeto_mayusculas="ZYXWVUTSRQPONMLKJHGFEDCBA", alfabeto_minusculas="zyxwvutsrqponmlkjihgfedcba"):
    mensaje_descifrado = ""
    for letra_cifrada in mensaje_cifrado:
        if letra_cifrada.isupper():
            indice_letra = alfabeto_mayusculas.index(letra_cifrada)
            letra_original = chr(ord('A') + indice_letra)
        else:
            indice_letra = alfabeto_minusculas.index(letra_cifrada)
            letra_original = chr(ord('a') + indice_letra)
        mensaje_descifrado += letra_original
    return mensaje_descifrado

def beaufort():
    while True:
        print("\nBienvenido al Cifrado de Beaufort")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje que desea cifrar: ")

            usar_alfabeto_personalizado = input("¿Desea utilizar un alfabeto personalizado para el cifrado Beaufort? (si/no): ")

            if usar_alfabeto_personalizado.lower() == "si":
                # Solicitar al usuario el alfabeto para mayúsculas
                alfabeto_mayusculas = input("Ingrese el alfabeto para cifrar mayúsculas: ")

                # Solicitar al usuario el alfabeto para minúsculas
                alfabeto_minusculas = input("Ingrese el alfabeto para cifrar minúsculas: ")
            else:
                # Usar el alfabeto integrado por defecto
                alfabeto_mayusculas = "ZYXWVUTSRQPONMLKJHGFEDCBA"
                alfabeto_minusculas = "zyxwvutsrqponmlkjihgfedcba"

            mensaje_cifrado = cifrado_beaufort(mensaje, alfabeto_mayusculas, alfabeto_minusculas)
            print("Mensaje cifrado:", mensaje_cifrado)

        elif opcion == "2":
            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")

            usar_alfabeto_personalizado = input("¿Desea utilizar un alfabeto personalizado para el cifrado Beaufort? (si/no): ")

            if usar_alfabeto_personalizado.lower() == "si":
                # Solicitar al usuario el alfabeto para mayúsculas
                alfabeto_mayusculas = input("Ingrese el alfabeto para cifrar mayúsculas: ")

                # Solicitar al usuario el alfabeto para minúsculas
                alfabeto_minusculas = input("Ingrese el alfabeto para cifrar minúsculas: ")
            else:
                # Usar el alfabeto integrado por defecto
                alfabeto_mayusculas = "ZYXWVUTSRQPONMLKJHGFEDCBA"
                alfabeto_minusculas = "zyxwvutsrqponmlkjihgfedcba"

            mensaje_descifrado = descifrado_beaufort(mensaje_cifrado, alfabeto_mayusculas, alfabeto_minusculas)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    beaufort()

###Fin de cifrado beaufor

#Funcion main secundaria de polialfabeticos periodicos
def periodicos():
    while True:
        print("\nBienvenido al Cifrado polialafabetico periodico")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrador Autoclave")
        print("2. Cifrador Beaufort")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            autoclave()

        elif opcion == "2":
            beaufort()

        # Agrega el resto de las opciones aquí
        elif opcion == "3":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    periodicos()
#fin de Funcion main secundaria de polialfabeticos periodicos
##Fin de polialfabeticos periodicos

##polialfabeticos no periodicos
###Cifrado con clave continua
def generar_clave(longitud):
  alfabeto = "abcdefghijklmnopqrstuvwxyz"
  return ''.join(random.choice(alfabeto) for _ in range(longitud))

def cifrar_autoclave(mensaje, clave):
  mensaje_cifrado = ""
  for i in range(len(mensaje)):
    mensaje_cifrado += chr(ord(mensaje[i]) ^ ord(clave[i]))
  return mensaje_cifrado

def descifrar_autoclave(mensaje_cifrado, clave):
  mensaje_descifrado = ""
  for i in range(len(mensaje_cifrado)):
    mensaje_descifrado += chr(ord(mensaje_cifrado[i]) ^ ord(clave[i]))
  return mensaje_descifrado

def claveContinua():
    while True:
        print("\nBienvenido al Cifrado por Clave continua")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            clave = generar_clave(len(mensaje))
            mensaje_cifrado = cifrar_autoclave(mensaje, clave)
            mensaje_cifrado_base64 = base64.b64encode(mensaje_cifrado.encode()).decode()  #Convertir a Base64
            print("Mensaje cifrado (Base64):", mensaje_cifrado_base64)
            print("Clave:", clave)

        elif opcion == "2":
            mensaje_cifrado_base64 = input("Ingrese el mensaje cifrado (Base64): ")
            clave = input("Ingrese la clave: ")
            mensaje_cifrado = base64.b64decode(mensaje_cifrado_base64).decode()  # Convertir de Base64
            mensaje_descifrado = descifrar_autoclave(mensaje_cifrado, clave)
            print("Mensaje descifrado:", mensaje_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    claveContinua()

###Fin de cifrado con clave continua

###Cifrado con clave vernam
def cifrado_vernam(mensaje, clave):
    # Convertir el mensaje y la clave a bytes si no lo están
    if isinstance(mensaje, str):
        mensaje = mensaje.encode('utf-8')
    if isinstance(clave, str):
        clave = clave.encode('utf-8')

    # Verificar que la longitud de la clave sea igual a la del mensaje
    if len(mensaje) != len(clave):
        raise ValueError("La longitud de la clave debe ser igual a la del mensaje")

    # Cifrar el mensaje usando la operación XOR bit a bit
    mensaje_cifrado = bytes([a ^ b for a, b in zip(mensaje, clave)])

    # Devolver el mensaje cifrado
    return mensaje_cifrado

def descifrado_vernam(mensaje_cifrado, clave):
    # Convertir la clave a bytes si no lo está
    if isinstance(clave, str):
        clave = clave.encode('utf-8')

    if not isinstance(mensaje_cifrado, bytes):
        raise TypeError("El mensaje cifrado debe ser una secuencia de bytes")
    if not isinstance(clave, bytes):
        raise TypeError("La clave debe ser una secuencia de bytes")

    # Verificar que la longitud de la clave sea igual a la del mensaje cifrado
    if len(mensaje_cifrado) != len(clave):
        raise ValueError("La longitud de la clave debe ser igual a la del mensaje cifrado")

    # Descifrar el mensaje usando la operación XOR bit a bit
    mensaje_descifrado = bytes([a ^ b for a, b in zip(mensaje_cifrado, clave)])

    # Devolver el mensaje descifrado como una secuencia de bytes
    return mensaje_descifrado


def generar_clave_aleatoria(longitud):
    return secrets.token_bytes(longitud)


def vernam():
    while True:
        print("\nBienvenido al Cifrado por Vernam")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            clave = generar_clave_aleatoria(len(mensaje))
            mensaje_cifrado = cifrado_vernam(mensaje, clave)
            print("Mensaje cifrado (hexadecimal):", mensaje_cifrado.hex())
            print("Clave:", clave.hex())

        elif opcion == "2":
            mensaje_cifrado_hex = input("Ingrese el mensaje cifrado (hexadecimal): ")
            clave_hex = input("Ingrese la clave: ")
            try:
                mensaje_descifrado = descifrado_vernam(bytes.fromhex(mensaje_cifrado_hex), bytes.fromhex(clave_hex)).decode('utf-8')
                print("Mensaje descifrado:", mensaje_descifrado)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    vernam()
###Fin de Cifrado con clave vernam

##Fin de polialfabeticos no periodicos
#Funcion secundaria de polialfabetos no periodicos
def noPeriodicos():
    while True:
        print("\nBienvenido al Cifrado polialfabetico no periodicos")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrador con clave continua")
        print("2. Cifrador Vernam")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            claveContinua()

        elif opcion == "2":
            vernam()

        # Agrega el resto de las opciones aquí
        elif opcion == "3":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    noPeriodicos()
#Fin de Funcion secundaria de polialfabetos no periodicos

#Fin de cifrado por sustitucion monogramico polialfabeto

#Funcion principal
def main():
    while True:
        print("\nBienvenido al Cifrador por sustitucion monogramica polialfabeto")
        # Menú principal
        print("\nOpciones:")
        print("1. Poli alfabeticos periodicos")
        print("2. Poli alfabeticos no periodicos")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            periodicos()

        elif opcion == "2":
            noPeriodicos()

        # Agrega el resto de las opciones aquí
        elif opcion == "3":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
#Fin de Funcion principal