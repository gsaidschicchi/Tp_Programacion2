# -----------------------------------------------------------------------------

# LIBRERIAS
import random
import time

# MODULOS PROPIOS
import core.GLOBALES as g
import core.pantalla as p

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

    numero_carrera = obtener_numero_carrera()

    carrera = {
        "idCarrera": numero_carrera,
        "autos": autos,
        "semaforos": semaforos,
        "casa": casa,
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
        semaforo["estado"] = random.choice(g.ESTADOS_SEMAFORO)

#-----------------------------------------------------------------------------

# Veo si el auto puede avanzar o no

def puede_avanzar(auto, semaforos):

    avanzar = True
    proxima_posicion = auto["posicion"] + auto["direccion"]

    for semaforo in semaforos:

        if proxima_posicion == semaforo["posicion"]:

            if semaforo["estado"] == "Rojo":
                avanzar = False

    return avanzar

#-----------------------------------------------------------------------------

def procesar_auto(auto, semaforos):

    if puede_avanzar(auto, semaforos):
        mover_auto(auto)
    else:
        print(auto["nombre"], "espera en semáforo rojo")

#-----------------------------------------------------------------------------

def verificar_ganador(carrera):

    posicion_llegada = carrera["casa"]["posicion"]
    auto1 = carrera["autos"][0]
    auto2 = carrera["autos"][1]

    ganador = None

    if auto1["posicion"] == posicion_llegada and auto2["posicion"] == posicion_llegada:
        ganador = "EMPATE"

    elif auto1["posicion"] == posicion_llegada:
        ganador = auto1["nombre"]

    elif auto2["posicion"] == posicion_llegada:
        ganador = auto2["nombre"]

    return ganador

#-----------------------------------------------------------------------------

def empezar_carrera(carrera):

    ganador = None
    ciclos = 0

    auto1 = carrera["autos"][0]
    auto2 = carrera["autos"][1]

    while ganador == None:

        procesar_auto(auto1, carrera["semaforos"])
        procesar_auto(auto2, carrera["semaforos"])

        p.limpiar_pantalla()

        ciclos = ciclos + 1

        print("Ciclo:", ciclos)

        p.mostrar_pista(carrera)

        ganador = verificar_ganador(carrera)

        if ciclos % g.CICLOS_CAMBIO_SEMAFORO == 0:
            cambiar_semaforo(carrera["semaforos"])

        time.sleep(g.DURACION_CICLO)

    return ganador

#-----------------------------------------------------------------------------

def mostrar_estado_semaforo(semaforos):

    for semaforo in semaforos:
        print("Semáforo", semaforo["id"], "-", semaforo["estado"])

#-----------------------------------------------------------------------------

# Guarda el resultado de una carrera en un archivo plano
def guardar_resultado(carrera, ganador, ruta="datos/historial.txt"):

    id_carrera = carrera["idCarrera"]

    archivo = open(ruta, "a", encoding="utf-8")

    archivo.write(
        "Carrera: " + str(id_carrera) +
        " - Ganador: " + ganador + "\n"
    )

    archivo.close()

#-----------------------------------------------------------------------------
    # Muestra el historial guardado en el archivo plano
def mostrar_historial(ruta="datos/historial.txt"):

    archivo = open(ruta, "r", encoding="utf-8")

    contenido = archivo.read()

    archivo.close()

    print()
    print("HISTORIAL DE CARRERAS")
    print("----------------------")
    print(contenido)

#-----------------------------------------------------------------------------

# Obtiene el número de la próxima carrera según el historial
def obtener_numero_carrera(ruta="datos/historial.txt"):

    numero_carrera = 1

    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    numero_carrera = len(lineas) + 1

    return numero_carrera