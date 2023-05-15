#-------------------------------------------------------------------------
# Archivo: record.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Adalberto Cerrillo, Viktoria Gómez, Brayan Domínguez, Hector González, Elliot Noriega
# Version: Mayo 2023
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y los almacena en un archivo de texto que simula el expediente de los pacientes
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
import stomp
import os
import sys

class Record(stomp.ConnectionListener):
    def __init__(self):
        try:
            os.mkdir('records')
        except OSError as _:
            pass
        self.topic = "record"
        self.conn = stomp.Connection()

    def subscribe(self):
        try:
            print("Esperando datos del paciente para actualizar expediente...")
            print()
            self.conn.set_listener("record", self)
            self.conn.connect(wait=True)
            self.conn.subscribe(destination=self.topic, id=1, ack="auto")
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            self.conn.disconnect()
            sys.exit("Conexión finalizada...")


    def on_message(self, message):
        print("Datos recibidos, actualizando expediente del paciente...")
        data = json.loads(message.body)
        record_file = open(f"./records/{data['ssn']}.txt", 'a')
        record_file.write(f"\n[{data['wearable']['date']}]: {data['name']} {data['last_name']}... ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        record_file.close()
        time.sleep(1)

    def __del__(self):
        self.conn.disconnect()

if __name__ == '__main__':
    record = Record()
    record.subscribe()