##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: monitor.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Adalberto Cerrillo, Viktoria Gómez, Brayan Domínguez, Hector González, Elliot Noriega
# Version: Mayo 2023
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y los mostrará al área interesada para su monitoreo continuo
#
#   Este archivo también define el punto de ejecución del Suscriptor
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
#           |       suscribe()       |  - self: definición de   |  - inicializa el      |
#           |                        |    la instancia de la    |    proceso de         |
#           |                        |    clase                 |    monitoreo de       |
#           |                        |                          |    signos vitales     |
#           +------------------------+--------------------------+-----------------------+
#           |     on_message()       |  - self: definición de   |  - muetra en pantalla |
#           |                        |    la instancia de la    |    los datos del      |
#           |                        |    clase                 |    adulto mayor       |
#           |                        |                          |    recibidos desde el |
#           |                        |                          |    distribuidor de    |
#           |                        |                          |    mensajes           |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------

import json
import time
import sys
import stomp

class Monitor(stomp.ConnectionListener):
    def __init__(self):
        self.topic = "monitor"

    def subscribe(self):
        try:
            print("Inicio de monitoreo de signos vitales...")
            print()
            conn = stomp.Connection()
            conn.set_listener("monitor", self)
            conn.connect('admin', 'admin', wait=True)
            conn.subscribe(destination=self.topic, id=1, ack="auto")
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            conn.disconnect()
            sys.exit("Conexión finalizada...")

    def on_message(self, message ):
        data = json.loads(message.body)
        print("ADVERTENCIA!!!")
        print(
            f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
        print(
            f"ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        print()

if __name__ == '__main__':
    monitor = Monitor()
    monitor.subscribe()