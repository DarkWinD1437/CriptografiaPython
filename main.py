# Importa tus módulos
import cifrado_descifrado_Cesar
import cifra_por_sustitucion
import cifrado_monogramico_polialfabeto
import cifrado_poligramica_monoalfabeto
import cifrado_por_sustitucion
import transformacion_por_conversion_de_base
import transformacion_por_logica_de_boole
import transformacion_matricial
# Importa los demás módulos aquí
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
# Función principal
def main():
    while True:
        limpiar_pantalla()
        print("\nBienvenido al programa de cifrado")
        # Menú principal
        print("\nOpciones:")
        print("1. Cifra de Cesar")
        print("2. Cifra por sustitución")
        print("3. Cifrado por sustitucion monogramico polialfabeto")
        print("4. Cifrado por sustitucion poligramica monoalfabeto")
        print("5. Cifrador por sustitución")
        print("6. Transformacion por conversion de Base")
        print("7. Transformacion por logica de Boole")
        print("8. Transformacion Matricial")
        print("9. Salir")

        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            cifrado_descifrado_Cesar.main()

        elif opcion == "2":
            cifra_por_sustitucion.main()

        elif opcion == "3":
            cifrado_monogramico_polialfabeto.main()

        elif opcion == "4":
            cifrado_poligramica_monoalfabeto.main()

        elif opcion == "5":
            cifrado_por_sustitucion.main()

        elif opcion == "6":
            transformacion_por_conversion_de_base.main()

        elif opcion == "7":
            transformacion_por_logica_de_boole.main()

        elif opcion == "8":
            transformacion_matricial.main()

        # Agrega el resto de las opciones aquí
        elif opcion == "9":
            print("\n¡Saliendo del programa!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
