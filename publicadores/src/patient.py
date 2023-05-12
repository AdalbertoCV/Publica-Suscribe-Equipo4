from src.devices.xiaomi_my_band import XiaomiMyBand
from src.devices.accelerometer import Accelerometer
from src.devices.timer import Timer
from faker import Faker
import random, json

class Patient:

    def __init__(self):
        fake = Faker()
        self.age = self.heart_rate = random.randint(60, 120)
        self.name = fake.first_name()
        self.last_name = fake.last_name()
        self.ssn = fake.ssn()
        self.wearable = XiaomiMyBand()
        self.timer = Timer()
        self.accelerometer = Accelerometer()

    def check_devices(self):
        self.wearable.run()
        self.timer.run()
        self.accelerometer.run()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)