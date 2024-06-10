#Cifra por sustitucion polialfabetica, Cifrado Homofonos(primer orden, Orden mayor, Segundo orden)
#Cifrado por sustitucion polialfabetica
def cifrado_polialfabetico(texto, claves):
  texto_cifrado = ""
  indice_clave = 0
  for caracter in texto:
    clave_actual = claves[indice_clave]
    if caracter.isalpha() and caracter.lower() in clave_actual:
      # Mantener la mayúscula o minúscula original
      if caracter.isupper():
        texto_cifrado += clave_actual[caracter.lower()].upper()
      else:
        texto_cifrado += clave_actual[caracter]
    else:
      texto_cifrado += caracter
    indice_clave = (indice_clave + 1) % len(claves)
  return texto_cifrado


def descifrado_polialfabetico(texto_cifrado, claves):
  texto_descifrado = ""
  indice_clave = 0
  for caracter_cifrado in texto_cifrado:
    clave_actual = claves[indice_clave]
    for clave_caracter, clave_valor in clave_actual.items():
      if caracter_cifrado.lower() == clave_valor.lower():
        # Mantener la mayúscula o minúscula original
        if caracter_cifrado.isupper():
          texto_descifrado += clave_caracter.upper()
        else:
          texto_descifrado += clave_caracter
        break
    else:
      texto_descifrado += caracter_cifrado
    indice_clave = (indice_clave + 1) % len(claves)

  return texto_descifrado


# Definición de claves (ampliadas para cubrir todo el alfabeto)
clave1 = {"a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T", "h": "S", "i": "R", "j": "Q", "k": "P",
          "l": "O", "m": "N", "n": "M", "o": "L", "p": "K", "q": "J", "r": "I", "s": "H", "t": "G", "u": "F", "v": "E",
          "w": "D", "x": "C", "y": "B", "z": "A"}
clave2 = {"a": "M", "b": "N", "c": "O", "d": "P", "e": "Q", "f": "R", "g": "S", "h": "T", "i": "U", "j": "V", "k": "W",
          "l": "X", "m": "Y", "n": "Z", "o": "A", "p": "B", "q": "C", "r": "D", "s": "E", "t": "F", "u": "G", "v": "H",
          "w": "I", "x": "J", "y": "K", "z": "L"}
clave3 = {"a": "X", "b": "Y", "c": "Z", "d": "A", "e": "B", "f": "C", "g": "D", "h": "E", "i": "F", "j": "G", "k": "H",
          "l": "I", "m": "J", "n": "K", "o": "L", "p": "M", "q": "N", "r": "O", "s": "P", "t": "Q", "u": "R", "v": "S",
          "w": "T", "x": "U", "y": "V", "z": "W"}

claves = [clave1, clave2, clave3]


def mainPoliAlfabetico():
  print("\nBienvenido al Cifrado Polialfabético")
  while True:
    print("\nOpciones:")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
      texto = input("Ingrese el texto a cifrar: ")
      texto_cifrado = cifrado_polialfabetico(texto, claves)
      print("Texto cifrado:", texto_cifrado)

    elif opcion == "2":
      texto = input("Ingrese el texto a descifrar: ")
      texto_descifrado = descifrado_polialfabetico(texto, claves)
      print("Texto descifrado:", texto_descifrado)

    elif opcion == "3":
      print("Saliendo del programa...")
      break

    else:
      print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
  mainPoliAlfabetico()

#fin de cifrado por sustitucion polialfabetica

#Cifrado por sustitucion homofono de primer orden, orden mayor y segundo orden
##cifrado por sustitucion homofono de primer orden
import random
random.seed(42)

def descifrar_palabra(palabra_cifrada, clave):
    palabra_descifrada = ''
    for caracter in palabra_cifrada:
        if caracter in clave:
            homofono = clave[caracter]
            palabra_descifrada += homofono
        else:
            palabra_descifrada += caracter
    return palabra_descifrada

def generar_clave_descifrado(clave_cifrado):
    clave_descifrado = {homofono: letra for letra, homofono in clave_cifrado.items()}
    return clave_descifrado

def generar_clave():
    clave = {}
    letras = 'abcdefghijklmnopqrstuvwxyz'
    homofonos_disponibles = list(range(10))
    for letra in letras:
        if homofonos_disponibles:  # Verificar si la lista no está vacía
            homofono = homofonos_disponibles.pop(0) % 10
            clave[letra] = str(homofono)
        else:
            break
    return clave

def cifrarPO(texto_plano, clave):
    texto_cifrado = ''
    for caracter in texto_plano.lower():
        if caracter in clave:
            homofono = clave[caracter]
            texto_cifrado += homofono
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrarPO(texto_cifrado, clave):
    texto_descifrado = ''
    for caracter in texto_cifrado:
        for letra, homofono in clave.items():
            if caracter == homofono:
                texto_descifrado += letra
                break
        else:
            texto_descifrado += caracter
    return texto_descifrado

def primerOrden():
    while True:
        print("\nBienvenido al Cifrado por Sustitución Homófona de primer orden")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")
        clave = generar_clave()
        if opcion == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            texto_cifrado = cifrarPO(mensaje, clave)
            print("Texto cifrado:", texto_cifrado)

        elif opcion == "2":
            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            texto_descifrado = descifrarPO(mensaje_cifrado, clave)
            print("Texto descifrado:", texto_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    primerOrden()

##fin de cifrado por sustitucion homofono de primer orden

##Cifrado por sustitucion homofono de orden mayor
def cifrarOM(mensaje_om, orden_om, diccionario_om):
    mensaje_cifrado_om = ""
    for caracter in mensaje_om:
        if caracter in diccionario_om:
            homofonos = diccionario_om[caracter]
            mensaje_cifrado_om += random.choice(homofonos) * orden_om
        else:
            mensaje_cifrado_om += caracter * orden_om  # Mantener caracteres no definidos
    return mensaje_cifrado_om

def construir_diccionario_inverso_om(diccionario_om, orden_om):
    diccionario_inverso_om = {}
    for clave, valores in diccionario_om.items():
        for valor in valores:
            clave_repetida = valor * orden_om
            if clave_repetida not in diccionario_inverso_om:
                diccionario_inverso_om[clave_repetida] = []
            diccionario_inverso_om[clave_repetida].append(clave)
    return diccionario_inverso_om

def backtrack(mensaje_cifrado_om, diccionario_inverso_om, path, start, orden_om, mensaje_original_om):
    if start == len(mensaje_cifrado_om):
        posible_descifrado_om = ''.join(path)
        return posible_descifrado_om if posible_descifrado_om == mensaje_original_om else None

    homofono = mensaje_cifrado_om[start:start+orden_om]
    if homofono in diccionario_inverso_om:
        for opcion in diccionario_inverso_om[homofono]:
            path.append(opcion)
            resultado = backtrack(mensaje_cifrado_om, diccionario_inverso_om, path, start + orden_om, orden_om, mensaje_original_om)
            if resultado:
                return resultado
            path.pop()
    else:
        path.append(homofono[0])  # Agregar el primer caracter si no hay homófono
        resultado = backtrack(mensaje_cifrado_om, diccionario_inverso_om, path, start + orden_om, orden_om, mensaje_original_om)
        if resultado:
            return resultado
        path.pop()
    return None

def descifrarOM(mensaje_cifrado_om, orden_om, diccionario_om, mensaje_original_om):
    diccionario_inverso_om = construir_diccionario_inverso_om(diccionario_om, orden_om)
    mensaje_descifrado_om = backtrack(mensaje_cifrado_om, diccionario_inverso_om, [], 0, orden_om, mensaje_original_om)
    return mensaje_descifrado_om if mensaje_descifrado_om else "No se pudo descifrar correctamente."

def ordenMayor():
    diccionario_om = {
        "a": ["a", "e"],
        "b": ["b", "v"],
        "c": ["c", "k"],
        "d": ["d", "t"],
        "e": ["e", "i"],
        "f": ["f"],
        "g": ["g", "j"],
        "h": ["h"],
        "i": ["i", "y"],
        "j": ["j", "g"],
        "k": ["k", "c"],
        "l": ["l"],
        "m": ["m"],
        "n": ["n"],
        "ñ": ["ñ"],
        "o": ["o", "u"],
        "p": ["p"],
        "q": ["q"],
        "r": ["r", "rr"],
        "s": ["s", "z"],
        "t": ["t", "d"],
        "u": ["u", "o"],
        "v": ["v", "b"],
        "w": ["w"],
        "x": ["x"],
        "y": ["y", "i"],
        "z": ["z", "s"]
    }

    mensaje_original = None


    while True:
        print("\nBienvenido al Cifrado por Sustitución Homófona de Orden Mayor")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje_original_om = input("Ingrese el mensaje a cifrar: ")
            while True:
                try:
                    orden_om = int(input("Ingrese el orden del cifrado (número entero positivo): "))
                    if orden_om > 0:
                        break
                    else:
                        print("El orden del cifrado debe ser un número entero positivo.")
                except ValueError:
                    print("Entrada no válida. Ingrese un número entero.")
            texto_cifrado_om = cifrarOM(mensaje_original_om, orden_om, diccionario_om)
            print("Texto cifrado:", texto_cifrado_om)

        elif opcion == "2":
            if mensaje_original_om is None:
                print("Primero debe cifrar un mensaje.")
                continue

            mensaje_cifrado_om = input("Ingrese el mensaje cifrado: ")
            while True:
                try:
                    orden_om = int(input("Ingrese el orden del cifrado (número entero positivo): "))
                    if orden_om > 0:
                        break
                    else:
                        print("El orden del cifrado debe ser un número entero positivo.")
                except ValueError:
                    print("Entrada no válida. Ingrese un número entero.")
            texto_descifrado_om = descifrarOM(mensaje_cifrado_om, orden_om, diccionario_om, mensaje_original_om)
            print("Texto descifrado:", texto_descifrado_om)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ordenMayor()

##Fin de Cifrado por sustitucion homofono de orden mayor

##Cifrado por sustitucion homofono de segundo orden

def cifrarSO(mensaje, diccionario):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter in diccionario:
            homofonos = diccionario[caracter]
            mensaje_cifrado += random.choice(homofonos)
        else:
            mensaje_cifrado += caracter  # Mantener caracteres no definidos
    return mensaje_cifrado

def construir_diccionario_inverso(diccionario):
    diccionario_inverso = {}
    for clave, homofonos in diccionario.items():
        for homofono in homofonos:
            if homofono not in diccionario_inverso:
                diccionario_inverso[homofono] = []
            diccionario_inverso[homofono].append(clave)
    return diccionario_inverso

def backtrackSO(mensaje_cifrado, diccionario_inverso, path, start, mensaje_original):
    if start == len(mensaje_cifrado):
        posible_descifrado = ''.join(path)
        return posible_descifrado if posible_descifrado == mensaje_original else None

    homofono = mensaje_cifrado[start]
    if homofono in diccionario_inverso:
        for opcion in diccionario_inverso[homofono]:
            path.append(opcion)
            resultado = backtrackSO(mensaje_cifrado, diccionario_inverso, path, start + 1, mensaje_original)
            if resultado:
                return resultado
            path.pop()
    else:
        path.append(homofono)  # Agregar el caracter original si no hay homófono
        resultado = backtrackSO(mensaje_cifrado, diccionario_inverso, path, start + 1, mensaje_original)
        if resultado:
            return resultado
        path.pop()
    return None

def descifrarSO(mensaje_cifrado, diccionario, mensaje_original):
    diccionario_inverso = construir_diccionario_inverso(diccionario)
    mensaje_descifrado = backtrackSO(mensaje_cifrado, diccionario_inverso, [], 0, mensaje_original)
    return mensaje_descifrado if mensaje_descifrado else "No se pudo descifrar correctamente."

def segundoOrden():
    diccionario = {
        "a": ["a", "e", "á", "à"],
        "b": ["b", "v"],
        "c": ["c", "k", "q"],
        "d": ["d", "t"],
        "e": ["e", "i", "é", "è"],
        "f": ["f"],
        "g": ["g", "j"],
        "h": ["h"],
        "i": ["i", "y", "í", "ì"],
        "j": ["j", "g"],
        "k": ["k", "c", "q"],
        "l": ["l", "ll"],
        "m": ["m"],
        "n": ["n"],
        "ñ": ["ñ"],
        "o": ["o", "u", "ó", "ò"],
        "p": ["p"],
        "q": ["q", "c", "k"],
        "r": ["r", "rr"],
        "s": ["s", "z"],
        "t": ["t", "d"],
        "u": ["u", "o", "ú", "ù"],
        "v": ["v", "b"],
        "w": ["w"],
        "x": ["x"],
        "y": ["y", "i"],
        "z": ["z", "s"]
    }

    mensaje_original = None

    while True:
        print("\nBienvenido al Cifrado por Sustitución Homófona de segundo orden")
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mensaje_original = input("Ingrese el mensaje a cifrar: ")
            texto_cifrado = cifrarSO(mensaje_original, diccionario)
            print("Texto cifrado:", texto_cifrado)

        elif opcion == "2":
            if mensaje_original is None:
                print("Primero debe cifrar un mensaje.")
                continue

            mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
            texto_descifrado = descifrarSO(mensaje_cifrado, diccionario, mensaje_original)
            print("Texto descifrado:", texto_descifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    segundoOrden()

##Fin de Cifrado por sustitucion homofono de segundo orden
#fin de Cifrado por sustitucion homofono de primer orden, orden mayor y segundo orden
#funcion secundaria cifrador homofonos
def homofono():
    while True:
        print("\nBienvenido a Cifrador Homofonos")
        # Menú principal
        print("\nOpciones:")
        print("1. Primer Orden")
        print("2. Orden Mayor")
        print("3. Segundo Orden")
        print("4. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            primerOrden()

        elif opcion == "2":
            ordenMayor()

        elif opcion == "3":
            segundoOrden()

        # Agrega el resto de las opciones aquí
        elif opcion == "4":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    homofono()

#fin de funcion secundaria cifrador homofonos
#Funcion principal de cifra por sustitucion
def main():
    while True:
        print("\nBienvenido a Cifra por Sustitucion")
        # Menú principal
        print("\nOpciones:")
        print("1. Poli alfabetica")
        print("2. Cifrador Homofonos")
        print("3. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            mainPoliAlfabetico()

        elif opcion == "2":
            homofono()

        # Agrega el resto de las opciones aquí
        elif opcion == "3":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

#Fin de Funcion principal de cifra por sustitucion