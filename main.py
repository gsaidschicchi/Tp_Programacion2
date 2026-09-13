"""
Nombre:
Legajo:
Comisión:
Día de cursada:
Descripción: Simulador de carrera urbana con semáforos
"""

import core.funciones as f
import core.GLOBALES as g


def main():

    carrera = f.crear_carrera()

    while carrera["autos"][0]["posicion"] < carrera["casa"]["posicion"]:
        f.mover_auto(carrera["autos"][0])
        print(carrera["autos"][0]["posicion"])

    f.cambiar_semaforo(carrera["semaforos"])
    for semaforo in carrera["semaforos"]:
        print(semaforo["id"], semaforo["estado"])

if __name__ == "__main__":
    main()