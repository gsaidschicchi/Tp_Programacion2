# LIBRERIAS
import re

#-----------------------------------------------------------------------------

# Valida una patente con formato AA123BB
def validar_patente(patente):

    patron = r"^[A-Z]{2}[0-9]{3}[A-Z]{2}$"
    valida = False

    if re.match(patron, patente):
        valida = True

    return valida

#-----------------------------------------------------------------------------