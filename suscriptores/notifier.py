#-------------------------------------------------------------------------
# Archivo: notifier.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Adalberto Cerrillo, Viktoria Gómez, Brayan Domínguez, Hector González, Elliot Noriega
# Version: Mayo 2023
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y lo notificará a un(a) enfermero(a) én particular para la atención del adulto mayor en
#   cuestión
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
import sys
import telepot

class Notifier(stomp.ConnectionListener):
    def __init__(self):
        self.topic = "notifier"
        self.token = ""
        self.chat_id = ""

    def subscribe(self):
        try:
            print("Inicio de gestión de notificaciones...")
            print()
            conn = stomp.Connection()
            conn.set_listener("", self)
            conn.connect()
            conn.subscribe(destination=self.topic, id=1, ack="auto")
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            conn.disconnect()
            sys.exit("Conexión finalizada...")

    def on_message(self, message):
        print("Enviando notificación de signos vitales...")
        if self.token and self.chat_id:
            data = json.loads(message.body)
            message = f"ADVERTENCIA!!!\n[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}...\nssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}"
            bot = telepot.Bot(self.token)
            bot.sendMessage(self.chat_id, message)
        time.sleep(1)

if __name__ == "__main__":
    notifier = Notifier()
    notifier.subscribe()