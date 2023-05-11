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
        print("Esperando datos del paciente para actualizar expediente...")
        print()
        self.conn.set_listener("record", self)
        self.conn.connect(wait=True)
        self.conn.subscribe(destination=self.topic, id=1, ack="auto")

    def on_message(self, headers, message):
        print("Datos recibidos, actualizando expediente del paciente...")
        data = json.loads(message)
        record_file = open(f"./records/{data['ssn']}.txt", 'a')
        record_file.write(f"\n[{data['wearable']['date']}]: {data['name']} {data['last_name']}... ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        record_file.close()
        time.sleep(1)

    def __del__(self):
        self.conn.disconnect()

if __name__ == '__main__':
    record = Record()
    record.subscribe()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit("Conexión finalizada...")