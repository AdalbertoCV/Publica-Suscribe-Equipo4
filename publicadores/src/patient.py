##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: patient.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define los a un adulto mayor, incluye los datos generales del adulto así 
#   como los dispositivos asignados
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
#           |    check_devices()     |  - self: definición de   |  - realiza la         |
#           |                        |    la instancia de la    |    consulta de los    |
#           |                        |    clase                 |    datos de los       |
#           |                        |                          |    dispositivos       |
#           |                        |                          |    asignados en un    |
#           |                        |                          |    determinado        |
#           |                        |                          |    momento            |
#           +------------------------+--------------------------+-----------------------+
#           |        to_json()       |  - self: definición de   |  - genera la          |
#           |                        |    la instancia de la    |    representación     |
#           |                        |    clase                 |    de los datos del   |
#           |                        |                          |    adulto mayor       |
#           |                        |                          |    en una cadena de   |
#           |                        |                          |    texto que sigue el |
#           |                        |                          |    formato JSON       | 
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from src.devices.xiaomi_my_band import XiaomiMyBand
from src.devices.accelerometer import Accelerometer
from src.devices.timer import Timer
from faker import Faker
import random, json

class Patient:

    def __init__(self):
        fake = Faker()
        self.age = self.heart_rate = random.randint(60, 120)
        self.name = fake.first_name()
        self.last_name = fake.last_name()
        self.ssn = fake.ssn()
        self.wearable = XiaomiMyBand()
        self.timer = Timer()
        self.accelerometer = Accelerometer()

    def check_devices(self):
        self.wearable.run()
        self.timer.run()
        self.accelerometer.run()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)