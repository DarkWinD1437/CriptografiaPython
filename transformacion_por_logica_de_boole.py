#transformacion por logica de boole
def convertir_palabra_a_binario(palabra):
    palabra_binaria = ""
    for caracter in palabra:
        palabra_binaria += bin(ord(caracter))[2:].zfill(8)
    return palabra_binaria

def ajustar_longitud_cadena(cadena1, cadena2):
    longitud_maxima = len(cadena1)
    cadena2 = (cadena2 * ((longitud_maxima // len(cadena2)) + 1))[:longitud_maxima]
    return cadena1, cadena2

def cifrar_palabra(palabra, clave, operacion):
    palabra_binaria = convertir_palabra_a_binario(palabra)
    clave_binaria = convertir_palabra_a_binario(clave)

    palabra_binaria, clave_binaria = ajustar_longitud_cadena(palabra_binaria, clave_binaria)

    palabra_cifrada = ""
    for i in range(len(palabra_binaria)):
        if operacion == 'AND':
            palabra_cifrada += str(int(palabra_binaria[i]) & int(clave_binaria[i]))
        elif operacion == 'OR':
            palabra_cifrada += str(int(palabra_binaria[i]) | int(clave_binaria[i]))
        elif operacion == 'XOR':
            palabra_cifrada += str(int(palabra_binaria[i]) ^ int(clave_binaria[i]))
        else:
            print(f"Operación '{operacion}' no es válida. Use AND, OR o XOR.")
            return None

    return palabra_cifrada

def binario_a_texto(binario):
    caracteres = [binario[i:i+8] for i in range(0, len(binario), 8)]
    palabra = ''.join([chr(int(caracter, 2)) for caracter in caracteres])
    return palabra

def descifrar_palabra(palabra_cifrada, clave, operacion):
    if operacion != 'XOR':
        print(f"La operación '{operacion}' no es reversible. Solo se puede descifrar con XOR.")
        return None

    clave_binaria = convertir_palabra_a_binario(clave)
    palabra_cifrada, clave_binaria = ajustar_longitud_cadena(palabra_cifrada, clave_binaria)

    palabra_descifrada_binaria = ""
    for i in range(len(palabra_cifrada)):
        palabra_descifrada_binaria += str(int(palabra_cifrada[i]) ^ int(clave_binaria[i]))

    return binario_a_texto(palabra_descifrada_binaria)

def main():
    print("\nBienvenido a la transformacion por logica de Boole")
    while True:
        print("\nOpciones:")
        print("1. Cifrar")
        print("2. Descifrar (XOR)")
        print("3. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            palabra = input("Ingrese la palabra a cifrar: ")
            clave = input("Ingrese la clave: ")
            print("las logicas AND y OR no tienen descifrado por problemas de ambiguedad")
            operacion = input("Ingrese la operación lógica a utilizar (AND, OR, XOR): ").upper()
            palabra_cifrada = cifrar_palabra(palabra, clave, operacion)
            if palabra_cifrada:
                print("Palabra cifrada:", palabra_cifrada)

        elif opcion == "2":
            palabra_cifrada = input("Ingrese la palabra cifrada: ")
            clave = input("Ingrese la clave: ")
            operacion = input("Ingrese la operación lógica a utilizar (XOR): ").upper()
            if operacion not in ['XOR']:
                print("La operación no es reversible. Solo se puede descifrar con XOR.")
                continue
            palabra_descifrada = descifrar_palabra(palabra_cifrada, clave, operacion)
            if palabra_descifrada:
                print("Palabra descifrada:", palabra_descifrada)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#Fin de transformacion por logica de boole