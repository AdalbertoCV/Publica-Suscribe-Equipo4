import stomp #Cambio en importaciones, stomp es el protocolo usado por ActiveMQ para la comunicacion Publicador-subscriptor

class Publisher:
    
    def __init__(self): # Inicializamos la instancia y abrimos la conexion
        self.conn = stomp.Connection()
        self.conn.start()
        self.conn.connect('admin', 'admin', wait=True)
    
    # Envia los datos a la cola
    def publish(self, queue, data):
        self.conn.send(queue, data, persistent='true')
    
    # Se cierra la conexion
    def __del__(self):
        self.conn.disconnect()