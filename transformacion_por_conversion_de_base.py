#Transformacion por conversion a base
def decimal_a_base(decimal, base):
    if decimal == 0:
        return '0'
    digitos = []
    while decimal:
        digitos.append(hex(decimal % base)[2:] if base == 16 else str(decimal % base))
        decimal //= base
    return ''.join(digitos[::-1])

def base_a_decimal(num, base):
    return int(num, base)

def cifrado_cesar_base(texto, clave, base):
    base_nueva = int(base)
    texto_cifrado = ""

    for char in texto:
        digito_actual = ord(char)
        digito_cifrado = (digito_actual + clave) % 256
        texto_cifrado += decimal_a_base(digito_cifrado, base_nueva).zfill(2 if base_nueva == 16 else 8)

    return texto_cifrado

def descifrado_cesar_base(texto, clave, base):
    base_nueva = int(base)
    tamaño_chunk = 2 if base_nueva == 16 else 8
    texto_descifrado = ""

    for i in range(0, len(texto), tamaño_chunk):
        chunk_actual = texto[i:i+tamaño_chunk]
        digito_actual = base_a_decimal(chunk_actual, base_nueva)
        digito_descifrado = (digito_actual - clave) % 256
        texto_descifrado += chr(digito_descifrado)

    return texto_descifrado

def main():
    while True:
        print("\nBienvenido a la transformacion por conversion de Base")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            # Cifrar texto
            texto = input("Ingrese el texto a cifrar: ").strip()
            clave = int(input("Ingrese la clave de cifrado (número entero): "))
            base = int(input("Ingrese la base en la que desea cifrar (entre 2 y 16): "))

            texto_cifrado = cifrado_cesar_base(texto, clave, base)
            print(f"\nTexto cifrado en base {base}: {texto_cifrado}")

        elif opcion == 2:
            # Descifrar texto
            texto_cifrado = input("Ingrese el texto cifrado: ").strip()
            clave = int(input("Ingrese la clave de cifrado (número entero): "))
            base = int(input("Ingrese la base en la que se cifró el texto (entre 2 y 16): "))

            texto_descifrado = descifrado_cesar_base(texto_cifrado, clave, base)
            print(f"\nTexto descifrado en base {base}: {texto_descifrado}")

        elif opcion == 3:
            # Salir
            print("\n¡Hasta luego!")
            break

        else:
            # Opción inválida
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()


#fin de Transformacion por conversion a base