# -----------------------------------------------------------------------------

# LIBRERIAS
import random

# MODULOS PROPIOS
import core.GLOBALES as g

# -----------------------------------------------------------------------------

# FUNCIONES DEL PROYECTO


# Muestra el título principal del programa
def mostrar_mensaje():
    print("Quien llega primero a casa")

#-----------------------------------------------------------------------------

# Crea los dos autos que participan de la carrera
def crear_autos():

    # Creo un Diccionario
    # Auto 1 parte desde el extremo izquierdo y avanza hacia la derecha
    auto1 = {
        "nombre": "Auto Rojo",
        "duenio": "Gera",
        "posicion": 0,
        "direccion": 1,
        "llego": False
    }

    # Auto 2 parte desde el extremo derecho y avanza hacia la izquierda
    auto2 = {
        "nombre": "Auto Azul",
        "duenio": "Pao",
        "posicion": 28,
        "direccion": -1,
        "llego": False
    }

    # Se agrupan ambos autos en una lista
    autos = [auto1, auto2]

    return autos

#-----------------------------------------------------------------------------

# Crea los cuatro semáforos ubicados sobre el recorrido
def crear_semaforos():

    semaforo1 = {
        "id": 1,
        "posicion": 5,
        "estado": "Rojo"
    }

    semaforo2 = {
        "id": 2,
        "posicion": 10,
        "estado": "Rojo"
    }

    semaforo3 = {
        "id": 3,
        "posicion": 18,
        "estado": "Rojo"
    }

    semaforo4 = {
        "id": 4,
        "posicion": 23,
        "estado": "Rojo"
    }

    # Se agrupan todos los semáforos en una lista
    semaforos = [semaforo1, semaforo2, semaforo3, semaforo4]

    return semaforos

#-----------------------------------------------------------------------------

# Crea la casa, que representa el punto de llegada de ambos autos
def crear_casa():

    casa = {
        "posicion": 14
    }

    return casa

#-----------------------------------------------------------------------------

# Creo la carrera, que agrupa todos los elementos

def crear_carrera():
    autos = crear_autos()
    semaforos = crear_semaforos()
    casa = crear_casa()

    carrera = {
        "idCarrera" : 1,
        "autos" : autos,
        "semaforos" : semaforos,
        "casa" : casa,
        "activa": True,
        "ganador": "",
        "tiempo": 0.0
    }

    return carrera

#-----------------------------------------------------------------------------

# Agrego movimiento a los autos

def mover_auto(auto):
    auto["posicion"] = auto["posicion"] + auto["direccion"]

#-----------------------------------------------------------------------------

# Cambio la luz de los semaforos

def cambiar_semaforo(semaforos):
    for semaforo in semaforos:
        semaforo["estado"] = random.choice(g.ESTADO_SEMAFORO)

#-----------------------------------------------------------------------------

# Veo si el auto puede avanzar o no
