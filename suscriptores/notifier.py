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