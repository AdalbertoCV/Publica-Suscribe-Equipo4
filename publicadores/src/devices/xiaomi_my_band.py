##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: xiaomy_my_band.py
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
#           |                        |    la instancia de la    |    actividad de       |
#           |                        |    clase                 |    monitoreo de los   |
#           |                        |                          |    signos vitales     |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from faker import Faker
import random, datetime

class XiaomiMyBand:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")
        self.producer = "Xiaomi"
        self.model = "Xiaomi My Band 6"
        self.firmware_ver = "6.0.19"
        self.software_ver = "32.1.15"
        self.step_count = 0
        self.battery_level = 100

    def run(self):
        self.temperature = random.uniform(33, 39)
        self.step_count += random.randint(20, 200)
        self.battery_level -= random.randint(1, 5)
        self.sleep_hours = 7 - random.randint(1, 5)
        self.calories_burned = random.randint(1500, 2500)
        self.heart_rate = random.randint(60, 150)
        self.blood_pressure = random.randint(100, 200)
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")