# LIBRERIAS
import subprocess
from colorama import Fore, Style

# FUNCIONES DE PANTALLA

# Limpia la consola antes de mostrar un nuevo ciclo
def limpiar_pantalla():
    subprocess.run("cls", shell=True)

def mostrar_pista(carrera):

    auto1 = carrera["autos"][0]
    auto2 = carrera["autos"][1]
    semaforos = carrera["semaforos"]
    casa = carrera["casa"]

    for posicion in range(29):

        if posicion == auto1["posicion"]:
            print(Fore.RED + "A1" + Style.RESET_ALL, end=" ")

        elif posicion == auto2["posicion"]:
            print(Fore.BLUE + "A2" + Style.RESET_ALL, end=" ")

        elif posicion == casa["posicion"]:
            print(Fore.YELLOW + "CA" + Style.RESET_ALL, end=" ")

        else:
            hay_semaforo = False

            for semaforo in semaforos:

                if posicion == semaforo["posicion"]:

                    if semaforo["estado"] == "Rojo":
                        print(
                            Fore.RED + "S" + str(semaforo["id"]) + Style.RESET_ALL,
                            end=" "
                        )
                    else:
                        print(
                            Fore.GREEN + "S" + str(semaforo["id"]) + Style.RESET_ALL,
                            end=" "
                        )

                    hay_semaforo = True

            if hay_semaforo == False:
                print("--", end=" ")

    print()

        
