import json, time, stomp, os #Cambio en importaciones, stomp es el protocolo usado por ActiveMQ para la comunicacion Publicador-subscriptor

class Record:

    def __init__(self): #Se inicializa la instancia y se abre la conexion.
        try:
            os.mkdir('records')
        except OSError as _:
            pass
        self.topic = "/topic/record"
        self.conn = stomp.Connection()

    def suscribe(self): # Metodo para inicialziar el monitoreo de los signos vitales.
        print("Esperando datos del paciente para actualizar expediente...")
        print()
        self.conn.set_listener("", self.listener)
        self.conn.start()
        self.conn.connect(wait=True)
        self.conn.subscribe(destination=self.topic, id=1, ack="auto")

    def callback(self, headers, message): # Este metodo se utiliza para escribir los datos recibidos en un archivo de texto.
        print("datos recibidos, actualizando expediente del paciente...")
        data = json.loads(message)
        record_file = open(f"./records/{data['ssn']}.txt", 'a')
        record_file.write(f"\n[{data['wearable']['date']}]: {data['name']} {data['last_name']}... ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}")
        record_file.close()
        time.sleep(1)

    # Se cierra la conexion
    def __del__(self):
        self.conn.disconnect()

if __name__ == '__main__':
    record = Record()
    record.suscribe()