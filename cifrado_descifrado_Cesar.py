#cifrado de cesar con alfabeto mixto (criptograma de la lapida del cementerio de trinity)
def cifrado_cesar_mixto(texto, desplazamiento, alfabeto_mixto):
  texto_cifrado = ""
  for caracter in texto:
    if caracter in alfabeto_mixto:
      indice_original = alfabeto_mixto.index(caracter)
      indice_cifrado = (indice_original + desplazamiento) % len(alfabeto_mixto)
      texto_cifrado += alfabeto_mixto[indice_cifrado]
    else:
      texto_cifrado += caracter
  return texto_cifrado

def descifrado_cesar_mixto(texto_cifrado, desplazamiento, alfabeto_mixto):
  texto_descifrado = ""
  for caracter_cifrado in texto_cifrado:
    if caracter_cifrado in alfabeto_mixto:
      indice_cifrado = alfabeto_mixto.index(caracter_cifrado)
      indice_original = (indice_cifrado - desplazamiento) % len(alfabeto_mixto)
      texto_descifrado += alfabeto_mixto[indice_original]
    else:
      texto_descifrado += caracter_cifrado
  return texto_descifrado

# Definición del alfabeto mixto
alfabeto_mixto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]|;:<>,.?/\\"


def cifrado_cesar_mixto(texto, desplazamiento, alfabeto_mixto):
  texto_cifrado = ""
  for caracter in texto:
    if caracter in alfabeto_mixto:
      indice_original = alfabeto_mixto.index(caracter)
      indice_cifrado = (indice_original + desplazamiento) % len(alfabeto_mixto)
      texto_cifrado += alfabeto_mixto[indice_cifrado]
    else:
      texto_cifrado += caracter
  return texto_cifrado


def descifrado_cesar_mixto(texto_cifrado, desplazamiento, alfabeto_mixto):
  texto_descifrado = ""
  for caracter_cifrado in texto_cifrado:
    if caracter_cifrado in alfabeto_mixto:
      indice_cifrado = alfabeto_mixto.index(caracter_cifrado)
      indice_original = (indice_cifrado - desplazamiento) % len(alfabeto_mixto)
      texto_descifrado += alfabeto_mixto[indice_original]
    else:
      texto_descifrado += caracter_cifrado
  return texto_descifrado


def main():
  alfabeto_mixto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]|;:<>,.?/\\"
  while True:
    print("\nBienvenido al Cifrado de Cesar")
    print("\nOpciones:")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
      mensaje = input("Ingrese el mensaje a cifrar: ")
      desplazamiento = int(input("Ingrese el desplazamiento: "))
      mensaje_cifrado = cifrado_cesar_mixto(mensaje, desplazamiento, alfabeto_mixto)
      print("Mensaje cifrado:", mensaje_cifrado)

    elif opcion == "2":
      mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
      desplazamiento = int(input("Ingrese el desplazamiento: "))
      mensaje_descifrado = descifrado_cesar_mixto(mensaje_cifrado, desplazamiento, alfabeto_mixto)
      print("Mensaje descifrado:", mensaje_descifrado)

    elif opcion == "3":
      print("Saliendo del programa...")
      break

    else:
      print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
  main()

#fin de Cifra de Cesar