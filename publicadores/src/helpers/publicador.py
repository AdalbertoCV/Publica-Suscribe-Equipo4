import stomp

class Publisher:
    
    def __init__(self):
        self.conn = stomp.Connection()
        self.conn.connect('admin', 'admin', wait=True)
    
    def publish(self, queue, data):
        self.conn.send(queue, data, persistent='true')
    
    def __del__(self):
        self.conn.disconnect()