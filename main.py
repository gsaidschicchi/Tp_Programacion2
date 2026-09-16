"""
Nombre:
Legajo:
Comisión:
Día de cursada:
Descripción: Simulador de carrera urbana con semáforos
"""

import core.funciones as f
import core.validaciones as v


def main():

    opcion = 0

    while opcion != 3:

        print()
        print("=============================")
        print("       CARRERA URBANA")
        print("=============================")
        print("1. Iniciar carrera")
        print("2. Ver historial")
        print("3. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:

                patente_valida = False

                while patente_valida == False:

                    patente = input("Ingrese una patente: ").upper()

                    if v.validar_patente(patente):
                        patente_valida = True
                    else:
                        print("Patente inválida. Formato esperado: AA123BB")

                carrera = f.crear_carrera()
                ganador = f.empezar_carrera(carrera)

                print()
                print("GANADOR:", ganador)

                f.guardar_resultado(carrera, ganador)

            elif opcion == 2:
                f.mostrar_historial()

            elif opcion == 3:
                print("Fin del programa")

            else:
                print("Opción inválida")

        except ValueError:
            print("Debe ingresar un número")


if __name__ == "__main__":
    main()