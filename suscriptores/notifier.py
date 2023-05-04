import json,time,stomp,sys #Cambio en importaciones, stomp es el protocolo usado por ActiveMQ para la comunicacion Publicador-subscriptor
import telepot

class Notifier:

    def __init__(self): # Inicializamos la instancia
        self.topic = "/queue/notifier"
        self.token = ""
        self.chat_id = ""

    def suscribe(self): # Inicializamos el monitoreo de los signos vitales.
        print("Inicio de gestión de notificaciones...")
        print()
        conn = stomp.Connection()
        conn.set_listener('', self)
        conn.start()
        conn.connect()
        conn.subscribe(destination=self.topic, ack='auto')

    def callback(self, headers, message): # Este metodo envia a traves de telegram los datos recibidos. (Usamos la libreria telepot).
        print("enviando notificación de signos vitales...")
        if self.token and self.chat_id:
            data = json.loads(message)
            message = f"ADVERTENCIA!!!\n[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}...\nssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}, dispositivo: {data['wearable']['id']}"
            bot = telepot.Bot(self.token)
            bot.sendMessage(self.chat_id, message)
        time.sleep(1)

if __name__ == '__main__':
    notifier = Notifier()
    notifier.suscribe()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit("Conexión finalizada...")