import json
import time
import sys
import telepot
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

    def on_message(self, headers, message):
        data = json.loads(message)
        print("ADVERTENCIA!!!")
        print(
            f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
        print(
            f"ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        print()

if __name__ == '__main__':
    monitor = Monitor()
    monitor.subscribe()