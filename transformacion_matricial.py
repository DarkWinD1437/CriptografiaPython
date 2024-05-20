#transformacion matricial
###
import cifrado_poligramica_monoalfabeto


def main():
    while True:
        print("\nEl cifrado de Hill es una manera mas perfecta de la representacion de transformacion matricial")
        print("ya que esta lleva la logica en su interior, no es necesario replicarlo")
        print("\nOpciones:")
        print("1. Cifrador de hill")
        print("2. salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            cifrado_poligramica_monoalfabeto.hill()

        elif opcion == "2":
            print("\n¡Saliendo del programa...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
###
#Fin de transformacion matricial

if __name__ == "__main__":
    main()