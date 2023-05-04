import json, time, stomp #Cambio en importaciones, stomp es el protocolo usado por ActiveMQ para la comunicacion Publicador-subscriptor

class Monitor:

    def __init__(self): # Inicializamos la instancia
        self.topic = "/topic/monitor"

    def subscribe(self): # Inicializamos el monitoreo de los signos vitales
        print("Inicio de monitoreo de signos vitales...")
        print()
        conn = stomp.Connection()
        conn.set_listener("", self.listener)
        conn.start()
        conn.connect()
        conn.subscribe(destination=self.topic, id=1, ack="auto")

    def callback(self, headers, message): # Se muestran en pantalla los datos recibidos.
        data = json.loads(message)
        print("ADVERTENCIA!!!")
        print(f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
        print(f"ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        print()
        time.sleep(1)

if __name__ == '__main__':
    monitor = Monitor()
    monitor.subscribe()
    while True:
        pass