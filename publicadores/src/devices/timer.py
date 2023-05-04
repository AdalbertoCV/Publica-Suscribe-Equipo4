##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: timer.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el publicador que enviará mensajes hacia el distribuidor de mensajes
#
#   A continuación se describen los métodos que se implementaron en esta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |       __init__()       |  - self: definición de   |  - constructor de la  |
#           |                        |    la instancia de la    |    clase              |
#           |                        |    clase                 |                       |
#           +------------------------+--------------------------+-----------------------+
#           |          run()         |  - self: definición de   |  - simula la          |
#           |                        |    la instancia de la    |    alarma que         |
#           |                        |    clase                 |    determina el       |
#           |                        |                          |    momento en el que  |
#           |                        |                          |    se debe            |
#           |                        |                          |    administrar algún  |
#           |                        |                          |    medicamento a los  | 
#           |                        |                          |    adultos mayores    |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from faker import Faker
import random

class Timer:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")

    def run(self):
        """
        el suministro de un medicamento determinado
        se realiza al cumplirse un horario establecido
        para un grupo de adultos mayores

        un ejemplo de horario puede ser cada 8 horas
        -> numero_random % 8 == 0
        """
        self.medicine = random.choice(['Paracetamol', 'Dipirona magnésica', 'Dipirona hioscina', 'Tramadol', 'Antidepresivo', 'Aspirina', 'Antiarritmico', 'Diuretico'])